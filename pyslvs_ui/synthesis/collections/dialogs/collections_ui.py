# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'collections.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from pyslvs_ui.qt import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(651, 532)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons:collections.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.main_splitter = QtWidgets.QSplitter(Dialog)
        self.main_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.main_splitter.setObjectName("main_splitter")
        self.preview_box = QtWidgets.QGroupBox(self.main_splitter)
        self.preview_box.setObjectName("preview_box")
        self.preview_layout = QtWidgets.QVBoxLayout(self.preview_box)
        self.preview_layout.setObjectName("preview_layout")
        self.sub_splitter = QtWidgets.QSplitter(self.main_splitter)
        self.sub_splitter.setOrientation(QtCore.Qt.Vertical)
        self.sub_splitter.setObjectName("sub_splitter")
        self.layoutWidget = QtWidgets.QWidget(self.sub_splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.common_label = QtWidgets.QLabel(self.layoutWidget)
        self.common_label.setObjectName("common_label")
        self.verticalLayout_2.addWidget(self.common_label)
        self.common_list = QtWidgets.QListWidget(self.layoutWidget)
        self.common_list.setObjectName("common_list")
        self.verticalLayout_2.addWidget(self.common_list)
        self.common_load = QtWidgets.QPushButton(self.layoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons:data.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.common_load.setIcon(icon1)
        self.common_load.setObjectName("common_load")
        self.verticalLayout_2.addWidget(self.common_load)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.sub_splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.Collections_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Collections_label.setObjectName("Collections_label")
        self.verticalLayout_3.addWidget(self.Collections_label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.collections_list = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.collections_list.setObjectName("collections_list")
        self.horizontalLayout_2.addWidget(self.collections_list)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.project_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons:mechanism.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.project_btn.setIcon(icon2)
        self.project_btn.setObjectName("project_btn")
        self.verticalLayout.addWidget(self.project_btn)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.rename_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons:rename.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rename_btn.setIcon(icon3)
        self.rename_btn.setAutoDefault(False)
        self.rename_btn.setObjectName("rename_btn")
        self.verticalLayout.addWidget(self.rename_btn)
        self.copy_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons:copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.copy_btn.setIcon(icon4)
        self.copy_btn.setObjectName("copy_btn")
        self.verticalLayout.addWidget(self.copy_btn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.delete_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons:delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_btn.setIcon(icon5)
        self.delete_btn.setAutoDefault(False)
        self.delete_btn.setObjectName("delete_btn")
        self.verticalLayout.addWidget(self.delete_btn)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addWidget(self.main_splitter)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.btn_box = QtWidgets.QDialogButtonBox(Dialog)
        self.btn_box.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Open)
        self.btn_box.setObjectName("btn_box")
        self.horizontalLayout_3.addWidget(self.btn_box)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)
        self.btn_box.rejected.connect(Dialog.reject)
        self.btn_box.accepted.connect(Dialog.accept)
        self.common_load.clicked.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Profile collections"))
        self.preview_box.setTitle(_translate("Dialog", "Preview"))
        self.common_label.setText(_translate("Dialog", "Common:"))
        self.common_load.setText(_translate("Dialog", "Load common structure"))
        self.Collections_label.setText(_translate("Dialog", "Project Collections:"))
        self.project_btn.setText(_translate("Dialog", "Mechanism"))
        self.rename_btn.setText(_translate("Dialog", "Rename"))
        self.copy_btn.setText(_translate("Dialog", "Copy"))
        self.delete_btn.setText(_translate("Dialog", "Delete"))
