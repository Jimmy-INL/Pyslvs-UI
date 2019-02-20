# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'core/synthesis/structure_synthesis/structure_widget.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from core.QtModules import *


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(397, 639)
        icon = QIcon()
        icon.addPixmap(QPixmap(":/icons/number.png"), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout_8 = QVBoxLayout(Form)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.edges_label = QLabel(Form)
        self.edges_label.setObjectName("edges_label")
        self.horizontalLayout_4.addWidget(self.edges_label)
        self.edges_text = QLineEdit(Form)
        self.edges_text.setReadOnly(True)
        self.edges_text.setObjectName("edges_text")
        self.horizontalLayout_4.addWidget(self.edges_text)
        self.expr_copy = QPushButton(Form)
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(":/icons/copy.png"), QIcon.Normal, QIcon.Off)
        self.expr_copy.setIcon(icon1)
        self.expr_copy.setObjectName("expr_copy")
        self.horizontalLayout_4.addWidget(self.expr_copy)
        self.expr_add_collection = QPushButton(Form)
        self.expr_add_collection.setText("")
        icon2 = QIcon()
        icon2.addPixmap(QPixmap(":/icons/collections.png"), QIcon.Normal, QIcon.Off)
        self.expr_add_collection.setIcon(icon2)
        self.expr_add_collection.setObjectName("expr_add_collection")
        self.horizontalLayout_4.addWidget(self.expr_add_collection)
        self.from_mechanism_button = QPushButton(Form)
        icon3 = QIcon()
        icon3.addPixmap(QPixmap(":/icons/merge_from.png"), QIcon.Normal, QIcon.Off)
        self.from_mechanism_button.setIcon(icon3)
        self.from_mechanism_button.setAutoDefault(True)
        self.from_mechanism_button.setDefault(True)
        self.from_mechanism_button.setObjectName("from_mechanism_button")
        self.horizontalLayout_4.addWidget(self.from_mechanism_button)
        self.verticalLayout_8.addLayout(self.horizontalLayout_4)
        self.line = QFrame(Form)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_8.addWidget(self.line)
        self.splitter = QSplitter(Form)
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.verticalLayoutWidget = QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.NJ_text = QLabel(self.verticalLayoutWidget)
        self.NJ_text.setObjectName("NJ_text")
        self.gridLayout.addWidget(self.NJ_text, 0, 1, 1, 1)
        self.NL_text = QLabel(self.verticalLayoutWidget)
        self.NL_text.setObjectName("NL_text")
        self.gridLayout.addWidget(self.NL_text, 0, 0, 1, 1)
        self.NL_input = QSpinBox(self.verticalLayoutWidget)
        self.NL_input.setMinimum(4)
        self.NL_input.setObjectName("NL_input")
        self.gridLayout.addWidget(self.NL_input, 2, 0, 1, 1)
        self.NJ_input = QSpinBox(self.verticalLayoutWidget)
        self.NJ_input.setMinimum(4)
        self.NJ_input.setObjectName("NJ_input")
        self.gridLayout.addWidget(self.NJ_input, 2, 1, 1, 1)
        self.DOF_text = QLabel(self.verticalLayoutWidget)
        self.DOF_text.setObjectName("DOF_text")
        self.gridLayout.addWidget(self.DOF_text, 0, 2, 1, 1)
        self.DOF = QSpinBox(self.verticalLayoutWidget)
        self.DOF.setEnabled(False)
        self.DOF.setMinimum(-99)
        self.DOF.setProperty("value", 1)
        self.DOF.setObjectName("DOF")
        self.gridLayout.addWidget(self.DOF, 2, 2, 1, 1)
        self.keep_dof = QCheckBox(self.verticalLayoutWidget)
        self.keep_dof.setChecked(True)
        self.keep_dof.setObjectName("keep_dof")
        self.gridLayout.addWidget(self.keep_dof, 0, 3, 1, 1)
        self.graph_degenerate = QComboBox(self.verticalLayoutWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graph_degenerate.sizePolicy().hasHeightForWidth())
        self.graph_degenerate.setSizePolicy(sizePolicy)
        self.graph_degenerate.setObjectName("graph_degenerate")
        self.graph_degenerate.addItem("")
        self.graph_degenerate.addItem("")
        self.graph_degenerate.addItem("")
        self.gridLayout.addWidget(self.graph_degenerate, 2, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.number_synthesis_button = QPushButton(self.verticalLayoutWidget)
        self.number_synthesis_button.setAutoDefault(True)
        self.number_synthesis_button.setObjectName("number_synthesis_button")
        self.verticalLayout_2.addWidget(self.number_synthesis_button)
        self.splitter_2 = QSplitter(self.verticalLayoutWidget)
        self.splitter_2.setOrientation(Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.verticalLayoutWidget_3 = QWidget(self.splitter_2)
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.link_assortments_label = QLabel(self.verticalLayoutWidget_3)
        self.link_assortments_label.setObjectName("link_assortments_label")
        self.verticalLayout_4.addWidget(self.link_assortments_label)
        self.l_a_list = QListWidget(self.verticalLayoutWidget_3)
        self.l_a_list.setObjectName("l_a_list")
        self.verticalLayout_4.addWidget(self.l_a_list)
        self.verticalLayoutWidget_4 = QWidget(self.splitter_2)
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.contracted_link_assortments_label = QLabel(self.verticalLayoutWidget_4)
        self.contracted_link_assortments_label.setObjectName("contracted_link_assortments_label")
        self.verticalLayout_7.addWidget(self.contracted_link_assortments_label)
        self.c_l_a_list = QListWidget(self.verticalLayoutWidget_4)
        self.c_l_a_list.setObjectName("c_l_a_list")
        self.verticalLayout_7.addWidget(self.c_l_a_list)
        self.verticalLayout_2.addWidget(self.splitter_2)
        self.verticalLayoutWidget_2 = QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.graph_engine_text = QLabel(self.verticalLayoutWidget_2)
        self.graph_engine_text.setObjectName("graph_engine_text")
        self.horizontalLayout.addWidget(self.graph_engine_text)
        self.graph_engine = QComboBox(self.verticalLayoutWidget_2)
        self.graph_engine.setObjectName("graph_engine")
        self.horizontalLayout.addWidget(self.graph_engine)
        self.reload_atlas = QPushButton(self.verticalLayoutWidget_2)
        self.reload_atlas.setText("")
        icon4 = QIcon()
        icon4.addPixmap(QPixmap(":/icons/data_update.png"), QIcon.Normal, QIcon.Off)
        self.reload_atlas.setIcon(icon4)
        self.reload_atlas.setObjectName("reload_atlas")
        self.horizontalLayout.addWidget(self.reload_atlas)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.graph_link_as_node = QCheckBox(self.verticalLayoutWidget_2)
        self.graph_link_as_node.setObjectName("graph_link_as_node")
        self.horizontalLayout.addWidget(self.graph_link_as_node)
        self.graph_show_label = QCheckBox(self.verticalLayoutWidget_2)
        self.graph_show_label.setChecked(True)
        self.graph_show_label.setObjectName("graph_show_label")
        self.horizontalLayout.addWidget(self.graph_show_label)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.structure_list_clear_button = QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.structure_list_clear_button.sizePolicy().hasHeightForWidth())
        self.structure_list_clear_button.setSizePolicy(sizePolicy)
        icon5 = QIcon()
        icon5.addPixmap(QPixmap(":/icons/clean.png"), QIcon.Normal, QIcon.Off)
        self.structure_list_clear_button.setIcon(icon5)
        self.structure_list_clear_button.setObjectName("structure_list_clear_button")
        self.horizontalLayout_5.addWidget(self.structure_list_clear_button)
        self.structure_synthesis_all_button = QPushButton(self.verticalLayoutWidget_2)
        self.structure_synthesis_all_button.setMaximumSize(QSize(100, 16777215))
        self.structure_synthesis_all_button.setAutoDefault(True)
        self.structure_synthesis_all_button.setObjectName("structure_synthesis_all_button")
        self.horizontalLayout_5.addWidget(self.structure_synthesis_all_button)
        self.structure_synthesis_links_button = QPushButton(self.verticalLayoutWidget_2)
        self.structure_synthesis_links_button.setObjectName("structure_synthesis_links_button")
        self.horizontalLayout_5.addWidget(self.structure_synthesis_links_button)
        self.structure_synthesis_button = QPushButton(self.verticalLayoutWidget_2)
        self.structure_synthesis_button.setAutoDefault(True)
        self.structure_synthesis_button.setObjectName("structure_synthesis_button")
        self.horizontalLayout_5.addWidget(self.structure_synthesis_button)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7.addLayout(self.verticalLayout_6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.structure_list = QListWidget(self.verticalLayoutWidget_2)
        self.structure_list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.structure_list.setIconSize(QSize(200, 200))
        self.structure_list.setMovement(QListView.Static)
        self.structure_list.setResizeMode(QListView.Adjust)
        self.structure_list.setViewMode(QListView.IconMode)
        self.structure_list.setUniformItemSizes(True)
        self.structure_list.setObjectName("structure_list")
        self.verticalLayout_3.addWidget(self.structure_list)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.time_title_label = QLabel(self.verticalLayoutWidget_2)
        self.time_title_label.setObjectName("time_title_label")
        self.horizontalLayout_6.addWidget(self.time_title_label)
        self.time_label = QLabel(self.verticalLayoutWidget_2)
        self.time_label.setObjectName("time_label")
        self.horizontalLayout_6.addWidget(self.time_label)
        self.paint_time_title_label = QLabel(self.verticalLayoutWidget_2)
        self.paint_time_title_label.setObjectName("paint_time_title_label")
        self.horizontalLayout_6.addWidget(self.paint_time_title_label)
        self.paint_time_label = QLabel(self.verticalLayoutWidget_2)
        self.paint_time_label.setObjectName("paint_time_label")
        self.horizontalLayout_6.addWidget(self.paint_time_label)
        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.save_atlas = QPushButton(self.verticalLayoutWidget_2)
        icon6 = QIcon()
        icon6.addPixmap(QPixmap(":/icons/picture.png"), QIcon.Normal, QIcon.Off)
        self.save_atlas.setIcon(icon6)
        self.save_atlas.setObjectName("save_atlas")
        self.horizontalLayout_6.addWidget(self.save_atlas)
        self.save_edges = QPushButton(self.verticalLayoutWidget_2)
        icon7 = QIcon()
        icon7.addPixmap(QPixmap(":/icons/save_file.png"), QIcon.Normal, QIcon.Off)
        self.save_edges.setIcon(icon7)
        self.save_edges.setObjectName("save_edges")
        self.horizontalLayout_6.addWidget(self.save_edges)
        self.edges2atlas_button = QPushButton(self.verticalLayoutWidget_2)
        icon8 = QIcon()
        icon8.addPixmap(QPixmap(":/icons/edges_to_atlas.png"), QIcon.Normal, QIcon.Off)
        self.edges2atlas_button.setIcon(icon8)
        self.edges2atlas_button.setIconSize(QSize(40, 16))
        self.edges2atlas_button.setObjectName("edges2atlas_button")
        self.horizontalLayout_6.addWidget(self.edges2atlas_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout_8.addWidget(self.splitter)

        self.retranslateUi(Form)
        self.graph_degenerate.setCurrentIndex(1)
        self.graph_engine.setCurrentIndex(-1)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.edges_label.setText(_translate("Form", "Edge set:"))
        self.expr_copy.setStatusTip(_translate("Form", "Copy expression."))
        self.expr_add_collection.setStatusTip(_translate("Form", "Add to collection."))
        self.from_mechanism_button.setStatusTip(_translate("Form", "Analyze current mechanism from canvas."))
        self.NJ_text.setToolTip(_translate("Form", "Number of joints"))
        self.NJ_text.setText(_translate("Form", "NJ (?)"))
        self.NL_text.setToolTip(_translate("Form", "Number of links"))
        self.NL_text.setText(_translate("Form", "NL (?)"))
        self.DOF_text.setToolTip(_translate("Form", "Degree of freedom"))
        self.DOF_text.setText(_translate("Form", "DOF (?)"))
        self.keep_dof.setStatusTip(_translate("Form", "Keep the degrees of freedom when adjusting numbers."))
        self.keep_dof.setText(_translate("Form", "Keep the DOF"))
        self.graph_degenerate.setItemText(0, _translate("Form", "Only degenerate"))
        self.graph_degenerate.setItemText(1, _translate("Form", "No degenerate"))
        self.graph_degenerate.setItemText(2, _translate("Form", "All"))
        self.number_synthesis_button.setStatusTip(_translate("Form", "Find the possible number of different joints."))
        self.number_synthesis_button.setText(_translate("Form", "Number Synthesis"))
        self.link_assortments_label.setText(_translate("Form", "Link assortments:"))
        self.contracted_link_assortments_label.setText(_translate("Form", "Contracted link assortments:"))
        self.graph_engine_text.setText(_translate("Form", "Engine: "))
        self.graph_engine.setStatusTip(_translate("Form", "Layout engine from NetworkX."))
        self.reload_atlas.setToolTip(_translate("Form", "Re-layout"))
        self.graph_link_as_node.setStatusTip(_translate("Form", "Show the edges as nodes."))
        self.graph_link_as_node.setText(_translate("Form", "Link as node"))
        self.graph_show_label.setText(_translate("Form", "Show labels"))
        self.structure_synthesis_all_button.setStatusTip(_translate("Form", "Find the structure of mechanism from all numbers."))
        self.structure_synthesis_all_button.setText(_translate("Form", "Find All"))
        self.structure_synthesis_links_button.setText(_translate("Form", "Find by Links"))
        self.structure_synthesis_button.setStatusTip(_translate("Form", "Find the structure of mechanism from specified numbers."))
        self.structure_synthesis_button.setText(_translate("Form", "Find by Contracted Links"))
        self.time_title_label.setText(_translate("Form", "Find in:"))
        self.paint_time_title_label.setText(_translate("Form", "Painted in:"))
        self.save_atlas.setStatusTip(_translate("Form", "Save the atlas to image file."))
        self.save_atlas.setText(_translate("Form", "Save as image"))
        self.save_edges.setStatusTip(_translate("Form", "Save the edges of atlas to text file."))
        self.save_edges.setText(_translate("Form", "Save as list"))
        self.edges2atlas_button.setStatusTip(_translate("Form", "Load the edges data from text file, then save them to image files."))


import icons_rc
