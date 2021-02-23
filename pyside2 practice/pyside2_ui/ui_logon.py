# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'Logon.ui'
##
# Created by: Qt User Interface Compiler version 5.15.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import Logon_rc


class Ui_Logon(object):
    def setupUi(self, Logon):
        if not Logon.objectName():
            Logon.setObjectName(u"Logon")
        Logon.resize(269, 110)
        icon = QIcon()
        icon.addFile(u":/images/ok.png", QSize(), QIcon.Normal, QIcon.Off)
        Logon.setWindowIcon(icon)
        self.widget = QWidget(Logon)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 251, 91))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelId = QLabel(self.widget)
        self.labelId.setObjectName(u"labelId")

        self.gridLayout.addWidget(self.labelId, 0, 0, 1, 1)

        self.lineEditId = QLineEdit(self.widget)
        self.lineEditId.setObjectName(u"lineEditId")

        self.gridLayout.addWidget(self.lineEditId, 0, 1, 1, 1)

        self.labelPW = QLabel(self.widget)
        self.labelPW.setObjectName(u"labelPW")

        self.gridLayout.addWidget(self.labelPW, 1, 0, 1, 1)

        self.lineEditPW = QLineEdit(self.widget)
        self.lineEditPW.setObjectName(u"lineEditPW")
        self.lineEditPW.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.lineEditPW, 1, 1, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.buttonOk = QPushButton(self.widget)
        self.buttonOk.setObjectName(u"buttonOk")
        self.buttonOk.setIcon(icon)

        self.horizontalLayout.addWidget(self.buttonOk)

        self.verticalLayout.addLayout(self.horizontalLayout)

# if QT_CONFIG(shortcut)
        self.labelId.setBuddy(self.lineEditId)
        self.labelPW.setBuddy(self.lineEditPW)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.lineEditId, self.lineEditPW)
        QWidget.setTabOrder(self.lineEditPW, self.buttonOk)

        self.retranslateUi(Logon)

        QMetaObject.connectSlotsByName(Logon)
    # setupUi

    def retranslateUi(self, Logon):
        Logon.setWindowTitle(
            QCoreApplication.translate("Logon", u"Log on", None))
        self.labelId.setText(
            QCoreApplication.translate("Logon", u"&Id:", None))
        self.labelPW.setText(QCoreApplication.translate(
            "Logon", u"&Password:", None))
        self.buttonOk.setText(QCoreApplication.translate("Logon", u"Ok", None))
    # retranslateUi
