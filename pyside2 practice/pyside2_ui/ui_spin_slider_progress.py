# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'Spin_Slider_Progress.ui'
##
# Created by: Qt User Interface Compiler version 5.15.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(334, 62)
        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 311, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.spinBox = QSpinBox(self.horizontalLayoutWidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimum(20)
        self.spinBox.setMaximum(30)
        self.spinBox.setSingleStep(2)
        self.spinBox.setValue(24)

        self.horizontalLayout.addWidget(self.spinBox)

        self.horizontalSlider = QSlider(self.horizontalLayoutWidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.horizontalSlider)

        self.progressBar = QProgressBar(self.horizontalLayoutWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)
        self.progressBar.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.progressBar)

        self.retranslateUi(Form)
        self.spinBox.valueChanged.connect(self.horizontalSlider.setValue)
        self.spinBox.valueChanged.connect(self.progressBar.setValue)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.spinBox.setSuffix(
            QCoreApplication.translate("Form", u" km", None))
        self.spinBox.setPrefix("")
        self.progressBar.setFormat(
            QCoreApplication.translate("Form", u"%v km", None))
    # retranslateUi
