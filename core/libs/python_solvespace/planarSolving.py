# -*- coding: utf-8 -*-

"""Python-Solvespace wrapper for PMKS expression."""

__author__ = "Yuan Chang"
__copyright__ = "Copyright (C) 2016-2018"
__license__ = "AGPL"
__email__ = "pyslvs@gmail.com"

from .cad import create2DSystem
from .slvs import (
    #Entities & Constraint
    Point2d,
    LineSegment2d,
    Constraint,
    #Result flags
    SLVS_RESULT_OKAY,
    SLVS_RESULT_INCONSISTENT,
    SLVS_RESULT_DIDNT_CONVERGE,
    SLVS_RESULT_TOO_MANY_UNKNOWNS,
)
from core.libs import VPoint
from math import radians, cos, sin
from typing import Tuple, List


def slvsProcess(
    vpoints: Tuple[VPoint],
    constraints: Tuple[Tuple[int, str, str, float]]
) -> Tuple[List[Tuple[float, float]], int]:
    """Use element module to convert into solvespace expression."""
    #Define VLinks here.
    vlinks = {}
    for i, vpoint in enumerate(vpoints):
        for linkName in vpoint.links:
            if linkName in vlinks:
                if i not in vlinks[linkName]:
                    vlinks[linkName].append(i)
            else:
                vlinks[linkName] = [i]
    
    #Limitation of Solvespacce kernel sys.
    pointCount = 0
    sliderCount = 0
    for vpoint in vpoints:
        pointCount += len(vpoint.c)
        if (vpoint.type == 1) or (vpoint.type == 2):
            sliderCount += 1
    constraintCount = len(constraints)
    
    sys, wp1, h_line = create2DSystem(pointCount*2 + sliderCount*2 + constraintCount*2)
    
    solved_points = []
    
    for vpoint in vpoints:
        """Append all points first.
        
        This is the point recorded in the table.
        """
        if vpoint.type == 0:
            #Has only one coordinate.
            solved_points.append(Point2d(
                wp1,
                sys.add_param(vpoint.cx),
                sys.add_param(vpoint.cy)
            ))
        elif (vpoint.type == 1) or (vpoint.type == 2):
            #Has two coordinates.
            solved_points.append((
                Point2d(
                    wp1,
                    sys.add_param(vpoint.c[0][0]),
                    sys.add_param(vpoint.c[0][1])
                ),
                Point2d(
                    wp1,
                    sys.add_param(vpoint.c[1][0]),
                    sys.add_param(vpoint.c[1][1])
                ),
            ))
    
    for i, vpoint in enumerate(vpoints):
        """P and RP Joint:
        
        If the point has a sliding degree of freedom.
        """
        if (vpoint.type == 1) or (vpoint.type == 2):
            """Make auxiliary line as a slider slot (The length is 10.0)."""
            p_base = solved_points[i][0]
            p_assist = Point2d(
                wp1,
                sys.add_param(vpoint.cx + 10.*cos(radians(vpoint.angle))),
                sys.add_param(vpoint.cy + 10.*sin(radians(vpoint.angle)))
            )
            l_slot = LineSegment2d(wp1, p_base, p_assist)
            Constraint.distance(10., wp1, p_base, p_assist)
            
            def relateWith(linkName: str):
                """Angle constraint function."""
                if linkName == 'ground':
                    """Angle can not be zero."""
                    if (vpoint.angle == 0.) or (vpoint.angle == 180.):
                        Constraint.parallel(wp1, h_line, l_slot)
                    else:
                        Constraint.angle(wp1, vpoint.angle, h_line, l_slot)
                    return
                relate = vlinks[linkName]
                relate_n = relate[relate.index(i) - 1]
                relate_vp = vpoints[relate_n]
                p_main = solved_points[i][vpoint.links.index(linkName)]
                if (relate_vp.type == 1) or (relate_vp.type == 2):
                    p_link_assist = solved_points[relate_n][
                        0 if (linkName == relate_vp.links[0]) else 1
                    ]
                else:
                    p_link_assist = solved_points[relate_n]
                l_link = LineSegment2d(wp1, p_main, p_link_assist)
                angle_base = vpoint.slopeAngle(relate_vp)
                if (angle_base == 0.) or (angle_base == 180.):
                    Constraint.parallel(wp1, l_link, l_slot)
                else:
                    Constraint.angle(wp1, angle_base, l_link, l_slot)
            
            #The slot has an angle with base link.
            relateWith(vpoint.links[0])
            #All point should on the slot.
            Constraint.on(wp1, solved_points[i][1], l_slot)
            #P Joint: The point do not have freedom of rotation.
            if vpoint.type == 1:
                for linkName in vpoint.links[1:]:
                    relateWith(linkName)
        
        for j, linkName in enumerate(vpoint.links):
            """vlinks to other points on the same link.
            
            If the joint is a slider, defined its base.
            """
            if (vpoint.type == 1) or (vpoint.type == 2):
                p_base = solved_points[i][0 if (j == 0) else 1]
            else:
                p_base = solved_points[i]
            
            #If this link is on the ground.
            if linkName == 'ground':
                Constraint.dragged(wp1, p_base)
                continue
            relate = vlinks[linkName]
            relate_n = relate.index(i)
            
            #Pass if this is the first point.
            if relate_n == 0:
                continue
            
            def getConnection(index: int) -> (float, Point2d):
                """Connect function, and return the distance."""
                n = relate[index]
                p = vpoints[n]
                d = p.distance(vpoint)
                if (p.type == 1) or (p.type == 2):
                    p_contact = solved_points[n][
                        0 if (linkName == p.links[0]) else 1
                    ]
                else:
                    p_contact = solved_points[n]
                return (d, p_contact)
            
            def ConnectTo(d: float, p_contact: Point2d):
                if d:
                    Constraint.distance(d, wp1, p_base, p_contact)
                else:
                    Constraint.on(wp1, p_base, p_contact)
            
            #Connection of the first point in this link.
            connect_1 = getConnection(0)
            if relate_n > 1:
                #Conection of the previous point.
                connect_2 = getConnection(relate_n-1)
                if bool(connect_1[0])!=bool(connect_2[0]):
                    #Same point. Just connect to same point.
                    ConnectTo(*(connect_1 if connect_1[0]==0. else connect_2))
                elif min(
                    abs(2*connect_1[0] - connect_2[0]),
                    abs(connect_1[0] - 2*connect_2[0]),
                ) < 0.001:
                    #Collinear.
                    Constraint.on(
                        wp1,
                        p_base,
                        LineSegment2d(wp1, connect_1[1], connect_2[1])
                    )
                    ConnectTo(*connect_1)
                else:
                    #Normal status.
                    ConnectTo(*connect_1)
                    ConnectTo(*connect_2)
            else:
                ConnectTo(*connect_1)
    
    for shaft, base_link, drive_link, angle in constraints:
        """The constraints of drive shaft.
        
        Simulate the input variables to the mechanism.
        The 'base points' are shaft center.
        """
        if vpoints[shaft].type != 0:
            p_base = solved_points[shaft][0]
        else:
            p_base = solved_points[shaft]
        
        #Base link slope angle.
        if base_link != 'ground':
            relate_base = vlinks[base_link]
            newRelateOrder_base = relate_base.index(shaft)-1
            angle -= vpoints[shaft].slopeAngle(vpoints[newRelateOrder_base])
            angle %= 360.
        
        x = sys.add_param(round(vpoints[shaft].cx + 10.*cos(radians(angle)), 8))
        y = sys.add_param(round(vpoints[shaft].cy + 10.*sin(radians(angle)), 8))
        p_hand = Point2d(wp1, x, y)
        Constraint.dragged(wp1, p_hand)
        #The virtual link that dragged by "hand".
        leader = LineSegment2d(wp1, p_base, p_hand)
        #Make another virtual link that should follow "hand".
        relate_drive = vlinks[drive_link]
        newRelateOrder_drive = relate_drive[relate_drive.index(shaft)-1]
        if vpoints[newRelateOrder_drive].type != 0:
            p_drive = solved_points[newRelateOrder_drive][0]
        else:
            p_drive = solved_points[newRelateOrder_drive]
        link = LineSegment2d(wp1, p_base, p_drive)
        Constraint.angle(wp1, .5, link, leader)
    
    #Solve
    result_flag = sys.solve()
    if result_flag == SLVS_RESULT_OKAY:
        resultList = []
        for p in solved_points:
            if type(p) == Point2d:
                resultList.append((p.u().value, p.v().value))
            else:
                resultList.append((
                    (p[0].u().value, p[0].v().value),
                    (p[1].u().value, p[1].v().value)
                ))
        return resultList, sys.dof
    elif result_flag == SLVS_RESULT_INCONSISTENT:
        error = "Inconsistent."
    elif result_flag == SLVS_RESULT_DIDNT_CONVERGE:
        error = "Did not converge."
    elif result_flag == SLVS_RESULT_TOO_MANY_UNKNOWNS:
        error = "Too many unknowns."
    raise Exception(error)
