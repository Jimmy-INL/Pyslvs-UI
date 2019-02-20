# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'core/synthesis/collections/structure_widget.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from core.QtModules import *


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(507, 639)
        icon = QIcon()
        icon.addPixmap(QPixmap(":/icons/structure.png"), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_by_files_button = QPushButton(Form)
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(":/icons/loadfile.png"), QIcon.Normal, QIcon.Off)
        self.add_by_files_button.setIcon(icon1)
        self.add_by_files_button.setObjectName("add_by_files_button")
        self.horizontalLayout.addWidget(self.add_by_files_button)
        self.add_by_edges_button = QPushButton(Form)
        self.add_by_edges_button.setIcon(icon)
        self.add_by_edges_button.setObjectName("add_by_edges_button")
        self.horizontalLayout.addWidget(self.add_by_edges_button)
        self.line = QFrame(Form)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.save_atlas = QPushButton(Form)
        icon2 = QIcon()
        icon2.addPixmap(QPixmap(":/icons/picture.png"), QIcon.Normal, QIcon.Off)
        self.save_atlas.setIcon(icon2)
        self.save_atlas.setObjectName("save_atlas")
        self.horizontalLayout.addWidget(self.save_atlas)
        self.save_edges = QPushButton(Form)
        icon3 = QIcon()
        icon3.addPixmap(QPixmap(":/icons/save_file.png"), QIcon.Normal, QIcon.Off)
        self.save_edges.setIcon(icon3)
        self.save_edges.setObjectName("save_edges")
        self.horizontalLayout.addWidget(self.save_edges)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.clear_button = QPushButton(Form)
        icon4 = QIcon()
        icon4.addPixmap(QPixmap(":/icons/clean.png"), QIcon.Normal, QIcon.Off)
        self.clear_button.setIcon(icon4)
        self.clear_button.setObjectName("clear_button")
        self.horizontalLayout.addWidget(self.clear_button)
        self.delete_button = QPushButton(Form)
        self.delete_button.setEnabled(False)
        icon5 = QIcon()
        icon5.addPixmap(QPixmap(":/icons/delete.png"), QIcon.Normal, QIcon.Off)
        self.delete_button.setIcon(icon5)
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout.addWidget(self.delete_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.splitter = QSplitter(Form)
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.collection_list = QListWidget(self.splitter)
        self.collection_list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.collection_list.setIconSize(QSize(100, 100))
        self.collection_list.setMovement(QListView.Static)
        self.collection_list.setResizeMode(QListView.Adjust)
        self.collection_list.setViewMode(QListView.IconMode)
        self.collection_list.setUniformItemSizes(True)
        self.collection_list.setObjectName("collection_list")
        self.verticalLayoutWidget = QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.graph_engine_text = QLabel(self.verticalLayoutWidget)
        self.graph_engine_text.setObjectName("graph_engine_text")
        self.horizontalLayout_7.addWidget(self.graph_engine_text)
        self.graph_engine = QComboBox(self.verticalLayoutWidget)
        self.graph_engine.setObjectName("graph_engine")
        self.horizontalLayout_7.addWidget(self.graph_engine)
        self.reload_atlas = QPushButton(self.verticalLayoutWidget)
        self.reload_atlas.setText("")
        icon6 = QIcon()
        icon6.addPixmap(QPixmap(":/icons/data_update.png"), QIcon.Normal, QIcon.Off)
        self.reload_atlas.setIcon(icon6)
        self.reload_atlas.setObjectName("reload_atlas")
        self.horizontalLayout_7.addWidget(self.reload_atlas)
        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.graph_link_as_node = QCheckBox(self.verticalLayoutWidget)
        self.graph_link_as_node.setObjectName("graph_link_as_node")
        self.horizontalLayout_7.addWidget(self.graph_link_as_node)
        self.graph_show_label = QCheckBox(self.verticalLayoutWidget)
        self.graph_show_label.setChecked(True)
        self.graph_show_label.setObjectName("graph_show_label")
        self.horizontalLayout_7.addWidget(self.graph_show_label)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.selection_window = QListWidget(self.verticalLayoutWidget)
        self.selection_window.setMinimumSize(QSize(210, 230))
        self.selection_window.setMaximumSize(QSize(210, 230))
        self.selection_window.setSelectionMode(QAbstractItemView.NoSelection)
        self.selection_window.setIconSize(QSize(200, 200))
        self.selection_window.setMovement(QListView.Static)
        self.selection_window.setViewMode(QListView.IconMode)
        self.selection_window.setObjectName("selection_window")
        self.horizontalLayout_2.addWidget(self.selection_window)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.edges_text = QLineEdit(self.verticalLayoutWidget)
        self.edges_text.setReadOnly(True)
        self.edges_text.setObjectName("edges_text")
        self.horizontalLayout_3.addWidget(self.edges_text)
        self.expr_copy = QPushButton(self.verticalLayoutWidget)
        icon7 = QIcon()
        icon7.addPixmap(QPixmap(":/icons/copy.png"), QIcon.Normal, QIcon.Off)
        self.expr_copy.setIcon(icon7)
        self.expr_copy.setObjectName("expr_copy")
        self.horizontalLayout_3.addWidget(self.expr_copy)
        self.capture_graph = QPushButton(self.verticalLayoutWidget)
        self.capture_graph.setIcon(icon2)
        self.capture_graph.setObjectName("capture_graph")
        self.horizontalLayout_3.addWidget(self.capture_graph)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.nl_text = QLabel(self.verticalLayoutWidget)
        self.nl_text.setObjectName("nl_text")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.nl_text)
        self.nl_label = QLabel(self.verticalLayoutWidget)
        self.nl_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.nl_label.setObjectName("nl_label")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.nl_label)
        self.nj_text = QLabel(self.verticalLayoutWidget)
        self.nj_text.setObjectName("nj_text")
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.nj_text)
        self.nj_label = QLabel(self.verticalLayoutWidget)
        self.nj_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.nj_label.setObjectName("nj_label")
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.nj_label)
        self.dof_text = QLabel(self.verticalLayoutWidget)
        self.dof_text.setObjectName("dof_text")
        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.dof_text)
        self.dof_label = QLabel(self.verticalLayoutWidget)
        self.dof_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dof_label.setObjectName("dof_label")
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.dof_label)
        self.is_degenerate_text = QLabel(self.verticalLayoutWidget)
        self.is_degenerate_text.setObjectName("is_degenerate_text")
        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.is_degenerate_text)
        self.is_degenerate_label = QLabel(self.verticalLayoutWidget)
        self.is_degenerate_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.is_degenerate_label.setObjectName("is_degenerate_label")
        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.is_degenerate_label)
        self.verticalLayout_5.addLayout(self.formLayout)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.link_assortments_text = QLabel(self.verticalLayoutWidget)
        self.link_assortments_text.setObjectName("link_assortments_text")
        self.verticalLayout_4.addWidget(self.link_assortments_text)
        self.link_assortments_label = QLabel(self.verticalLayoutWidget)
        self.link_assortments_label.setObjectName("link_assortments_label")
        self.verticalLayout_4.addWidget(self.link_assortments_label)
        self.contracted_link_assortments_text = QLabel(self.verticalLayoutWidget)
        self.contracted_link_assortments_text.setObjectName("contracted_link_assortments_text")
        self.verticalLayout_4.addWidget(self.contracted_link_assortments_text)
        self.contracted_link_assortments_label = QLabel(self.verticalLayoutWidget)
        self.contracted_link_assortments_label.setObjectName("contracted_link_assortments_label")
        self.verticalLayout_4.addWidget(self.contracted_link_assortments_label)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.configure_button = QPushButton(self.verticalLayoutWidget)
        self.configure_button.setEnabled(False)
        icon8 = QIcon()
        icon8.addPixmap(QPixmap(":/icons/configure.png"), QIcon.Normal, QIcon.Off)
        self.configure_button.setIcon(icon8)
        self.configure_button.setObjectName("configure_button")
        self.horizontalLayout_5.addWidget(self.configure_button)
        self.grounded_merge = QPushButton(self.verticalLayoutWidget)
        self.grounded_merge.setEnabled(False)
        icon9 = QIcon()
        icon9.addPixmap(QPixmap(":/icons/merge.png"), QIcon.Normal, QIcon.Off)
        self.grounded_merge.setIcon(icon9)
        self.grounded_merge.setObjectName("grounded_merge")
        self.horizontalLayout_5.addWidget(self.grounded_merge)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.grounded_list = QListWidget(self.verticalLayoutWidget)
        self.grounded_list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.grounded_list.setIconSize(QSize(150, 150))
        self.grounded_list.setMovement(QListView.Static)
        self.grounded_list.setResizeMode(QListView.Adjust)
        self.grounded_list.setViewMode(QListView.IconMode)
        self.grounded_list.setUniformItemSizes(True)
        self.grounded_list.setObjectName("grounded_list")
        self.horizontalLayout_4.addWidget(self.grounded_list)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addWidget(self.splitter)

        self.retranslateUi(Form)
        self.graph_engine.setCurrentIndex(-1)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.add_by_files_button.setStatusTip(_translate("Form", "Add the chain by edge expression from text files."))
        self.add_by_edges_button.setStatusTip(_translate("Form", "Add the chain by edge expression."))
        self.save_atlas.setStatusTip(_translate("Form", "Save the atlas to image file."))
        self.save_atlas.setText(_translate("Form", "Save as image"))
        self.save_edges.setStatusTip(_translate("Form", "Save the edges of atlas to text file."))
        self.save_edges.setText(_translate("Form", "Save as list"))
        self.clear_button.setStatusTip(_translate("Form", "Delete all of structures."))
        self.delete_button.setStatusTip(_translate("Form", "Delete this structure."))
        self.graph_engine_text.setText(_translate("Form", "Engine: "))
        self.graph_engine.setStatusTip(_translate("Form", "Layout engine from NetworkX."))
        self.reload_atlas.setToolTip(_translate("Form", "Re-layout"))
        self.graph_link_as_node.setText(_translate("Form", "Link as node"))
        self.graph_show_label.setText(_translate("Form", "Show labels"))
        self.expr_copy.setStatusTip(_translate("Form", "Copy expression."))
        self.nl_text.setText(_translate("Form", "Number of links:"))
        self.nl_label.setText(_translate("Form", "0"))
        self.nj_text.setText(_translate("Form", "Number of joints:"))
        self.nj_label.setText(_translate("Form", "0"))
        self.dof_text.setText(_translate("Form", "Degrees of freedom:"))
        self.dof_label.setText(_translate("Form", "0"))
        self.is_degenerate_text.setText(_translate("Form", "Is degenerate:"))
        self.is_degenerate_label.setText(_translate("Form", "N/A"))
        self.link_assortments_text.setText(_translate("Form", "Link assortments:"))
        self.link_assortments_label.setText(_translate("Form", "N/A"))
        self.contracted_link_assortments_text.setText(_translate("Form", "Contracted link assortments:"))
        self.contracted_link_assortments_label.setText(_translate("Form", "N/A"))
        self.configure_button.setStatusTip(_translate("Form", "Use trangular formula to do dimentional synthesis."))
        self.configure_button.setText(_translate("Form", "Configure"))
        self.grounded_merge.setStatusTip(_translate("Form", "Merge the specified chain to canvas with current layout."))
        self.grounded_merge.setText(_translate("Form", "Merge"))


import icons_rc
