# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'core/synthesis/collections/dialogs/collections.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from core.QtModules import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(651, 532)
        icon = QIcon()
        icon.addPixmap(QPixmap(":/icons/collections.png"), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)
        self.verticalLayout_4 = QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.main_splitter = QSplitter(Dialog)
        self.main_splitter.setOrientation(Qt.Horizontal)
        self.main_splitter.setObjectName("main_splitter")
        self.preview_box = QGroupBox(self.main_splitter)
        self.preview_box.setObjectName("preview_box")
        self.preview_layout = QVBoxLayout(self.preview_box)
        self.preview_layout.setObjectName("preview_layout")
        self.show_solutions = QCheckBox(self.preview_box)
        self.show_solutions.setChecked(True)
        self.show_solutions.setObjectName("show_solutions")
        self.preview_layout.addWidget(self.show_solutions)
        self.sub_splitter = QSplitter(self.main_splitter)
        self.sub_splitter.setOrientation(Qt.Vertical)
        self.sub_splitter.setObjectName("sub_splitter")
        self.layoutWidget = QWidget(self.sub_splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.common_label = QLabel(self.layoutWidget)
        self.common_label.setObjectName("common_label")
        self.verticalLayout_2.addWidget(self.common_label)
        self.common_list = QListWidget(self.layoutWidget)
        self.common_list.setObjectName("common_list")
        self.verticalLayout_2.addWidget(self.common_list)
        self.common_load = QPushButton(self.layoutWidget)
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(":/icons/data.png"), QIcon.Normal, QIcon.Off)
        self.common_load.setIcon(icon1)
        self.common_load.setObjectName("common_load")
        self.verticalLayout_2.addWidget(self.common_load)
        self.verticalLayoutWidget = QWidget(self.sub_splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.line = QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.Collections_label = QLabel(self.verticalLayoutWidget)
        self.Collections_label.setObjectName("Collections_label")
        self.verticalLayout_3.addWidget(self.Collections_label)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.collections_list = QListWidget(self.verticalLayoutWidget)
        self.collections_list.setObjectName("collections_list")
        self.horizontalLayout_2.addWidget(self.collections_list)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.workbook_button = QPushButton(self.verticalLayoutWidget)
        icon2 = QIcon()
        icon2.addPixmap(QPixmap(":/icons/mechanism.png"), QIcon.Normal, QIcon.Off)
        self.workbook_button.setIcon(icon2)
        self.workbook_button.setObjectName("workbook_button")
        self.verticalLayout.addWidget(self.workbook_button)
        self.line_2 = QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.rename_button = QPushButton(self.verticalLayoutWidget)
        icon3 = QIcon()
        icon3.addPixmap(QPixmap(":/icons/rename.png"), QIcon.Normal, QIcon.Off)
        self.rename_button.setIcon(icon3)
        self.rename_button.setAutoDefault(False)
        self.rename_button.setObjectName("rename_button")
        self.verticalLayout.addWidget(self.rename_button)
        self.copy_button = QPushButton(self.verticalLayoutWidget)
        icon4 = QIcon()
        icon4.addPixmap(QPixmap(":/icons/copy.png"), QIcon.Normal, QIcon.Off)
        self.copy_button.setIcon(icon4)
        self.copy_button.setObjectName("copy_button")
        self.verticalLayout.addWidget(self.copy_button)
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.delete_button = QPushButton(self.verticalLayoutWidget)
        icon5 = QIcon()
        icon5.addPixmap(QPixmap(":/icons/delete.png"), QIcon.Normal, QIcon.Off)
        self.delete_button.setIcon(icon5)
        self.delete_button.setAutoDefault(False)
        self.delete_button.setObjectName("delete_button")
        self.verticalLayout.addWidget(self.delete_button)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addWidget(self.main_splitter)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.button_box = QDialogButtonBox(Dialog)
        self.button_box.setStandardButtons(QDialogButtonBox.Close|QDialogButtonBox.Open)
        self.button_box.setObjectName("button_box")
        self.horizontalLayout_3.addWidget(self.button_box)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)
        self.button_box.rejected.connect(Dialog.reject)
        self.button_box.accepted.connect(Dialog.accept)
        self.common_load.clicked.connect(Dialog.accept)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Profile collections"))
        self.preview_box.setTitle(_translate("Dialog", "Preview"))
        self.show_solutions.setText(_translate("Dialog", "Show solutions"))
        self.common_label.setText(_translate("Dialog", "Common:"))
        self.common_load.setText(_translate("Dialog", "Load common structure"))
        self.Collections_label.setText(_translate("Dialog", "Workbook Collections:"))
        self.workbook_button.setText(_translate("Dialog", "Mechanism"))
        self.rename_button.setText(_translate("Dialog", "Rename"))
        self.copy_button.setText(_translate("Dialog", "Copy"))
        self.delete_button.setText(_translate("Dialog", "Delete"))


import icons_rc
import preview_rc
