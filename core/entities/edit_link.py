# -*- coding: utf-8 -*-

"""The option dialog use to create or edit the link."""

__author__ = "Yuan Chang"
__copyright__ = "Copyright (C) 2016-2018"
__license__ = "AGPL"
__email__ = "pyslvs@gmail.com"

from re import match
from typing import List, Union, Optional
from core.QtModules import (
    pyqtSlot,
    Qt,
    QDialog,
    QIcon,
    QPixmap,
    QListWidgetItem,
    QDialogButtonBox,
    QColorDialog,
    QWidget,
)
from core.graphics import (
    colorNames,
    colorQt,
    colorIcon,
)
from core.libs import VPoint, VLink
from .Ui_edit_link import Ui_Dialog


class EditLinkDialog(QDialog, Ui_Dialog):
    
    """Option dialog.
    
    Only edit the target path after closed.
    """
    
    def __init__(
        self,
        vpoints: List[VPoint],
        vlinks: List[VLink],
        row: Union[int, bool],
        parent: QWidget
    ):
        """Input data reference from main window.
        
        + Needs VPoints and VLinks information.
        + If row is false: Create action.
        """
        super(EditLinkDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.vpoints = vpoints
        self.vlinks = vlinks
        icon = self.windowIcon()
        self.PointIcon = QIcon(QPixmap(":/icons/bearing.png"))
        for i, e in enumerate(colorNames):
            self.color_box.insertItem(i, colorIcon(e), e)
        for i in range(len(self.vpoints)):
            self.noSelected.addItem(
                QListWidgetItem(self.PointIcon, f'Point{i}')
            )
        if row is False:
            self.name_box.addItem(icon, "New link")
            self.name_box.setEnabled(False)
            self.color_box.setCurrentIndex(self.color_box.findText('Blue'))
        else:
            for i, vlink in enumerate(self.vlinks):
                self.name_box.insertItem(i, icon, vlink.name)
            self.name_box.setCurrentIndex(row)
        self.name_edit.textChanged.connect(self.__isOk)
        self.__isOk()
    
    @pyqtSlot()
    def __isOk(self):
        """Set button box enable if options are ok."""
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(
            self.__legalName(self.name_edit.text())
        )
    
    def __legalName(self, name: str) -> bool:
        """Return this name is usable or not."""
        if not match("^[A-Za-z0-9_-]*$", name):
            return False
        for i, vlink in enumerate(self.vlinks):
            if (i != self.name_box.currentIndex()) and (name == vlink.name):
                return False
        return True
    
    @pyqtSlot(int, name='on_name_box_currentIndexChanged')
    def __setName(self, index: int):
        """Load the parameters of the link."""
        if not self.name_box.isEnabled():
            return
        if len(self.vlinks) > index:
            vlink = self.vlinks[index]
            self.name_edit.setText(vlink.name)
            color_text = vlink.colorSTR
            color_index = self.color_box.findText(color_text)
            if color_index > -1:
                self.color_box.setCurrentIndex(color_index)
            else:
                self.color_box.addItem(colorIcon(color_text), color_text)
                self.color_box.setCurrentIndex(self.color_box.count() - 1)
            self.noSelected.clear()
            self.selected.clear()
            for p in vlink.points:
                self.selected.addItem(
                    QListWidgetItem(self.PointIcon, f'Point{p}')
                )
            for p in range(len(self.vpoints)):
                if p in vlink.points:
                    continue
                self.noSelected.addItem(
                    QListWidgetItem(self.PointIcon, f'Point{p}')
                )
        not_ground = index > 0
        for widget in (self.name_edit, self.color_box, self.colorpick_button):
            widget.setEnabled(not_ground)
    
    @pyqtSlot(int, name='on_color_box_currentIndexChanged')
    def __setColor(self, index: int):
        """Change the color icon of pick button."""
        del index
        self.colorpick_button.setIcon(self.color_box.itemIcon(
            self.color_box.currentIndex()
        ))
    
    @pyqtSlot(name='on_colorpick_button_clicked')
    def __setRGB(self):
        """Add a custom color from current color."""
        color = QColorDialog.getColor(
            colorQt(self.color_box.currentText()),
            self
        )
        if not color.isValid():
            return
        rgb_str = str((color.red(), color.green(), color.blue()))
        self.color_box.addItem(colorIcon(rgb_str), rgb_str)
        self.color_box.setCurrentIndex(self.color_box.count() - 1)
    
    @pyqtSlot(QListWidgetItem, name='on_noSelected_itemDoubleClicked')
    def __addSelected(self, item: QListWidgetItem):
        """Add item to selected list."""
        self.selected.addItem(
            self.noSelected.takeItem(self.noSelected.row(item))
        )
    
    @pyqtSlot(QListWidgetItem, name='on_selected_itemDoubleClicked')
    def __addNoSelected(self, item: QListWidgetItem):
        """Add item to no selected list."""
        self.noSelected.addItem(
            self.selected.takeItem(self.selected.row(item))
        )
