# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'ImageLoader.ui'
##
# Created by: Qt User Interface Compiler version 5.15.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ImageLoader(object):
    def setupUi(self, ImageLoader):
        if not ImageLoader.objectName():
            ImageLoader.setObjectName(u"ImageLoader")
        ImageLoader.resize(707, 541)
        self.verticalLayoutWidget = QWidget(ImageLoader)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 681, 471))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.imageLabel = QLabel(self.verticalLayoutWidget)
        self.imageLabel.setObjectName(u"imageLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.imageLabel.sizePolicy().hasHeightForWidth())
        self.imageLabel.setSizePolicy(sizePolicy)
        self.imageLabel.setFrameShape(QFrame.Panel)
        self.imageLabel.setFrameShadow(QFrame.Sunken)
        self.imageLabel.setScaledContents(True)

        self.verticalLayout.addWidget(self.imageLabel)

        self.openButton = QPushButton(self.verticalLayoutWidget)
        self.openButton.setObjectName(u"openButton")

        self.verticalLayout.addWidget(self.openButton)

        self.retranslateUi(ImageLoader)
        self.openButton.clicked.connect(ImageLoader.open)

        QMetaObject.connectSlotsByName(ImageLoader)
    # setupUi

    def retranslateUi(self, ImageLoader):
        ImageLoader.setWindowTitle(QCoreApplication.translate(
            "ImageLoader", u"Image Loader by YDG", None))
        self.imageLabel.setText("")
        self.openButton.setText(QCoreApplication.translate(
            "ImageLoader", u"Load Image", None))
    # retranslateUi
