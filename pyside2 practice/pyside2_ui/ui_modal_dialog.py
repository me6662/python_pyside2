# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'Modal_Dialog.ui'
##
# Created by: Qt User Interface Compiler version 5.15.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import GridDialog_rc


class Ui_GridDialog(object):
    def setupUi(self, GridDialog):
        if not GridDialog.objectName():
            GridDialog.setObjectName(u"GridDialog")
        GridDialog.resize(254, 164)
        self.verticalLayout = QVBoxLayout(GridDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(GridDialog)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setLayoutDirection(Qt.LeftToRight)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(True)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.xLabel = QLabel(self.groupBox)
        self.xLabel.setObjectName(u"xLabel")

        self.gridLayout.addWidget(self.xLabel, 0, 0, 1, 1)

        self.xLineEdit = QLineEdit(self.groupBox)
        self.xLineEdit.setObjectName(u"xLineEdit")

        self.gridLayout.addWidget(self.xLineEdit, 0, 1, 1, 1)

        self.yLabel = QLabel(self.groupBox)
        self.yLabel.setObjectName(u"yLabel")

        self.gridLayout.addWidget(self.yLabel, 1, 0, 1, 1)

        self.yLineEdit = QLineEdit(self.groupBox)
        self.yLineEdit.setObjectName(u"yLineEdit")

        self.gridLayout.addWidget(self.yLineEdit, 1, 1, 1, 1)

        self.verticalLayout.addWidget(self.groupBox)

        self.checkBox = QCheckBox(GridDialog)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout.addWidget(self.checkBox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.okButton = QPushButton(GridDialog)
        self.okButton.setObjectName(u"okButton")
        icon = QIcon()
        icon.addFile(u":/images/ok.png", QSize(), QIcon.Normal, QIcon.Off)
        self.okButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.okButton)

        self.cancelButton = QPushButton(GridDialog)
        self.cancelButton.setObjectName(u"cancelButton")
        icon1 = QIcon()
        icon1.addFile(u":/images/cancel.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.cancelButton.setIcon(icon1)

        self.horizontalLayout.addWidget(self.cancelButton)

        self.verticalLayout.addLayout(self.horizontalLayout)

# if QT_CONFIG(shortcut)
        self.xLabel.setBuddy(self.xLineEdit)
        self.yLabel.setBuddy(self.yLineEdit)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(GridDialog)
        self.okButton.clicked.connect(GridDialog.accept)
        self.cancelButton.clicked.connect(GridDialog.reject)
        self.groupBox.toggled.connect(self.checkBox.setEnabled)

        QMetaObject.connectSlotsByName(GridDialog)
    # setupUi

    def retranslateUi(self, GridDialog):
        GridDialog.setWindowTitle(
            QCoreApplication.translate("GridDialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate(
            "GridDialog", u"Use Grid", None))
        self.xLabel.setText(QCoreApplication.translate(
            "GridDialog", u"&X:", None))
        self.yLabel.setText(QCoreApplication.translate(
            "GridDialog", u"&Y:", None))
        self.checkBox.setText(QCoreApplication.translate(
            "GridDialog", u"Use Snap", None))
        self.okButton.setText(
            QCoreApplication.translate("GridDialog", u"&Ok", None))
        self.cancelButton.setText(
            QCoreApplication.translate("GridDialog", u"&Cancel", None))
    # retranslateUi
