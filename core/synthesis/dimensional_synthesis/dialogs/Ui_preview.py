# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'core/synthesis/dimensional_synthesis/dialogs/preview.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from core.QtModules import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(811, 659)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.information_tab = QTabWidget(Dialog)
        self.information_tab.setObjectName("information_tab")
        self.geometry = QWidget()
        self.geometry.setObjectName("geometry")
        self.verticalLayout = QVBoxLayout(self.geometry)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_splitter = QSplitter(self.geometry)
        self.main_splitter.setOrientation(Qt.Horizontal)
        self.main_splitter.setObjectName("main_splitter")
        self.leftWidget = QWidget(self.main_splitter)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftWidget.sizePolicy().hasHeightForWidth())
        self.leftWidget.setSizePolicy(sizePolicy)
        self.leftWidget.setObjectName("leftWidget")
        self.left_layout = QHBoxLayout(self.leftWidget)
        self.left_layout.setContentsMargins(0, 0, 0, 0)
        self.left_layout.setObjectName("left_layout")
        self.line = QFrame(self.leftWidget)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.left_layout.addWidget(self.line)
        self.splitter = QSplitter(self.main_splitter)
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.basic_groupbox = QGroupBox(self.splitter)
        self.basic_groupbox.setObjectName("basic_groupbox")
        self.verticalLayout_4 = QVBoxLayout(self.basic_groupbox)
        self.verticalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.scrollArea = QScrollArea(self.basic_groupbox)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 717, 85))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.basic_label = QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.basic_label.sizePolicy().hasHeightForWidth())
        self.basic_label.setSizePolicy(sizePolicy)
        self.basic_label.setObjectName("basic_label")
        self.verticalLayout_6.addWidget(self.basic_label)
        spacerItem = QSpacerItem(20, 47, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.scrollArea)
        self.algorithm_groupbox = QGroupBox(self.splitter)
        self.algorithm_groupbox.setObjectName("algorithm_groupbox")
        self.verticalLayout_7 = QVBoxLayout(self.algorithm_groupbox)
        self.verticalLayout_7.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.scrollArea_2 = QScrollArea(self.algorithm_groupbox)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 717, 197))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.algorithm_label = QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.algorithm_label.sizePolicy().hasHeightForWidth())
        self.algorithm_label.setSizePolicy(sizePolicy)
        self.algorithm_label.setObjectName("algorithm_label")
        self.verticalLayout_5.addWidget(self.algorithm_label)
        spacerItem1 = QSpacerItem(20, 201, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_7.addWidget(self.scrollArea_2)
        self.hardware_groupbox = QGroupBox(self.splitter)
        self.hardware_groupbox.setObjectName("hardware_groupbox")
        self.verticalLayout_3 = QVBoxLayout(self.hardware_groupbox)
        self.verticalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea_3 = QScrollArea(self.hardware_groupbox)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 717, 196))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.hardware_label = QLabel(self.scrollAreaWidgetContents_3)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hardware_label.sizePolicy().hasHeightForWidth())
        self.hardware_label.setSizePolicy(sizePolicy)
        self.hardware_label.setObjectName("hardware_label")
        self.verticalLayout_8.addWidget(self.hardware_label)
        spacerItem2 = QSpacerItem(20, 201, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem2)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_3.addWidget(self.scrollArea_3)
        self.verticalLayout.addWidget(self.main_splitter)
        self.information_tab.addTab(self.geometry, "")
        self.verticalLayout_2.addWidget(self.information_tab)

        self.retranslateUi(Dialog)
        self.information_tab.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.basic_groupbox.setTitle(_translate("Dialog", "Basic information"))
        self.basic_label.setText(_translate("Dialog", "TextLabel"))
        self.algorithm_groupbox.setTitle(_translate("Dialog", "Algorithm information"))
        self.algorithm_label.setText(_translate("Dialog", "TextLabel"))
        self.hardware_groupbox.setTitle(_translate("Dialog", "Hardware information"))
        self.hardware_label.setText(_translate("Dialog", "TextLabel"))
        self.information_tab.setTabText(self.information_tab.indexOf(self.geometry), _translate("Dialog", "Geometry"))


