# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'Modaless_Dialog.ui'
##
# Created by: Qt User Interface Compiler version 5.15.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import FindReplaceDialog_rc


class Ui_FindReplaceDialog(object):
    def setupUi(self, FindReplaceDialog):
        if not FindReplaceDialog.objectName():
            FindReplaceDialog.setObjectName(u"FindReplaceDialog")
        FindReplaceDialog.resize(406, 170)
        icon = QIcon()
        icon.addFile(u":/images/find.png", QSize(), QIcon.Normal, QIcon.Off)
        FindReplaceDialog.setWindowIcon(icon)
        self.horizontalLayout = QHBoxLayout(FindReplaceDialog)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.findComboBox = QComboBox(FindReplaceDialog)
        self.findComboBox.setObjectName(u"findComboBox")
        self.findComboBox.setEnabled(True)
        self.findComboBox.setEditable(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.findComboBox)

        self.label = QLabel(FindReplaceDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.replaceComboBox = QComboBox(FindReplaceDialog)
        self.replaceComboBox.setObjectName(u"replaceComboBox")
        self.replaceComboBox.setEditable(True)

        self.formLayout.setWidget(
            1, QFormLayout.FieldRole, self.replaceComboBox)

        self.label_2 = QLabel(FindReplaceDialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.verticalLayout.addLayout(self.formLayout)

        self.groupBox = QGroupBox(FindReplaceDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_2.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout_2.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.groupBox)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout_2.addWidget(self.checkBox_3)

        self.verticalLayout.addWidget(self.groupBox)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.findButton = QPushButton(FindReplaceDialog)
        self.findButton.setObjectName(u"findButton")

        self.verticalLayout_3.addWidget(self.findButton)

        self.replaceButton = QPushButton(FindReplaceDialog)
        self.replaceButton.setObjectName(u"replaceButton")
        self.replaceButton.setEnabled(False)

        self.verticalLayout_3.addWidget(self.replaceButton)

        self.replaceAllButton = QPushButton(FindReplaceDialog)
        self.replaceAllButton.setObjectName(u"replaceAllButton")
        self.replaceAllButton.setEnabled(False)

        self.verticalLayout_3.addWidget(self.replaceAllButton)

        self.closeButton = QPushButton(FindReplaceDialog)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setEnabled(False)

        self.verticalLayout_3.addWidget(self.closeButton)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)
# if QT_CONFIG(shortcut)
        self.label.setBuddy(self.replaceComboBox)
        self.label_2.setBuddy(self.findComboBox)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(FindReplaceDialog)
        self.closeButton.clicked.connect(FindReplaceDialog.close)
        self.findComboBox.currentTextChanged.connect(
            FindReplaceDialog.enableButtons)
        self.replaceComboBox.currentTextChanged.connect(
            FindReplaceDialog.enableButtons)
        self.findButton.clicked.connect(FindReplaceDialog.onFind)
        self.replaceButton.clicked.connect(FindReplaceDialog.onReplace)
        self.replaceAllButton.clicked.connect(FindReplaceDialog.onRepalceAll)

        self.findButton.setDefault(True)

        QMetaObject.connectSlotsByName(FindReplaceDialog)
    # setupUi

    def retranslateUi(self, FindReplaceDialog):
        FindReplaceDialog.setWindowTitle(QCoreApplication.translate(
            "FindReplaceDialog", u"Find/Replace", None))
        self.label.setText(QCoreApplication.translate(
            "FindReplaceDialog", u"Replace with : ", None))
        self.label_2.setText(QCoreApplication.translate(
            "FindReplaceDialog", u"Find what : ", None))
        self.groupBox.setTitle(QCoreApplication.translate(
            "FindReplaceDialog", u"Options", None))
        self.checkBox.setText(QCoreApplication.translate(
            "FindReplaceDialog", u"Match whole word", None))
        self.checkBox_2.setText(QCoreApplication.translate(
            "FindReplaceDialog", u"Match case", None))
        self.checkBox_3.setText(QCoreApplication.translate(
            "FindReplaceDialog", u"Upward", None))
        self.findButton.setText(QCoreApplication.translate(
            "FindReplaceDialog", u"Find", None))
        self.replaceButton.setText(QCoreApplication.translate(
            "FindReplaceDialog", u"Replace", None))
        self.replaceAllButton.setText(QCoreApplication.translate(
            "FindReplaceDialog", u"Replace All", None))
        self.closeButton.setText(QCoreApplication.translate(
            "FindReplaceDialog", u"Close", None))
    # retranslateUi
