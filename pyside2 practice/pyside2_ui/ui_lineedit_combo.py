# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'LineEdit_ComboBox_ui.ui'
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
        Form.resize(387, 394)
        self.gB_LineEdit = QGroupBox(Form)
        self.gB_LineEdit.setObjectName(u"gB_LineEdit")
        self.gB_LineEdit.setGeometry(QRect(20, 20, 341, 91))
        self.label = QLabel(self.gB_LineEdit)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 71, 21))
        self.label.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.lineEdit = QLineEdit(self.gB_LineEdit)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(100, 20, 221, 20))
        self.lineEdit.setReadOnly(True)
        self.label_2 = QLabel(self.gB_LineEdit)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 50, 71, 21))
        self.label_2.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.lineEdit_2 = QLineEdit(self.gB_LineEdit)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(100, 50, 221, 20))
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setReadOnly(False)
        self.gB_ComboBox = QGroupBox(Form)
        self.gB_ComboBox.setObjectName(u"gB_ComboBox")
        self.gB_ComboBox.setGeometry(QRect(20, 120, 341, 71))
        self.comboBox = QComboBox(self.gB_ComboBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(20, 30, 301, 22))
        self.comboBox.setEditable(True)
        self.comboBox.setModelColumn(0)
        self.gB_Validator = QGroupBox(Form)
        self.gB_Validator.setObjectName(u"gB_Validator")
        self.gB_Validator.setGeometry(QRect(20, 200, 341, 151))
        self.lineEdit_int = QLineEdit(self.gB_Validator)
        self.lineEdit_int.setObjectName(u"lineEdit_int")
        self.lineEdit_int.setGeometry(QRect(130, 20, 191, 20))
        self.lineEdit_int.setEchoMode(QLineEdit.Normal)
        self.lineEdit_int.setReadOnly(False)
        self.label_3 = QLabel(self.gB_Validator)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 20, 111, 21))
        self.label_3.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_4 = QLabel(self.gB_Validator)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 50, 111, 21))
        self.label_4.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.lineEdit_double = QLineEdit(self.gB_Validator)
        self.lineEdit_double.setObjectName(u"lineEdit_double")
        self.lineEdit_double.setGeometry(QRect(130, 50, 191, 20))
        self.lineEdit_double.setEchoMode(QLineEdit.Normal)
        self.lineEdit_double.setReadOnly(False)
        self.lineEdit_over0 = QLineEdit(self.gB_Validator)
        self.lineEdit_over0.setObjectName(u"lineEdit_over0")
        self.lineEdit_over0.setGeometry(QRect(130, 80, 191, 20))
        self.lineEdit_over0.setEchoMode(QLineEdit.Normal)
        self.lineEdit_over0.setReadOnly(False)
        self.label_5 = QLabel(self.gB_Validator)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 80, 111, 21))
        self.label_5.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_6 = QLabel(self.gB_Validator)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 110, 111, 21))
        self.label_6.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.lineEdit_combo = QLineEdit(self.gB_Validator)
        self.lineEdit_combo.setObjectName(u"lineEdit_combo")
        self.lineEdit_combo.setGeometry(QRect(130, 110, 191, 20))
        self.lineEdit_combo.setEchoMode(QLineEdit.Normal)
        self.lineEdit_combo.setReadOnly(False)
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 360, 311, 16))

        self.retranslateUi(Form)
        self.comboBox.currentIndexChanged.connect(Form.onSelected)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.gB_LineEdit.setTitle(
            QCoreApplication.translate("Form", u"Line Edit", None))
        self.label.setText(QCoreApplication.translate(
            "Form", u"Read Only :", None))
        self.lineEdit.setText(
            QCoreApplication.translate("Form", u"Read Only", None))
        self.label_2.setText(QCoreApplication.translate(
            "Form", u"Password :", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(
            QCoreApplication.translate("Form", u"Set your password", None))
        self.gB_ComboBox.setTitle(
            QCoreApplication.translate("Form", u"Combo Box", None))
        self.comboBox.setItemText(
            0, QCoreApplication.translate("Form", u"Apple", None))
        self.comboBox.setItemText(
            1, QCoreApplication.translate("Form", u"StrawBerry", None))
        self.comboBox.setItemText(
            2, QCoreApplication.translate("Form", u"Water Melon", None))

        self.gB_Validator.setTitle(QCoreApplication.translate(
            "Form", u"Validator (Input Limitation)", None))
        self.lineEdit_int.setText("")
        self.lineEdit_int.setPlaceholderText("")
        self.label_3.setText(QCoreApplication.translate(
            "Form", u"100 ~ 999 int", None))
        self.label_4.setText(QCoreApplication.translate(
            "Form", u"-0.1 ~ 100 double", None))
        self.lineEdit_double.setText("")
        self.lineEdit_double.setPlaceholderText("")
        self.lineEdit_over0.setText("")
        self.lineEdit_over0.setPlaceholderText("")
        self.label_5.setText(QCoreApplication.translate(
            "Form", u"over 0 double", None))
        self.label_6.setText(
            QCoreApplication.translate("Form", u"combo", None))
        self.lineEdit_combo.setText("")
        self.lineEdit_combo.setPlaceholderText("")
        self.label_7.setText(QCoreApplication.translate(
            "Form", u"* Validator is only used at code", None))
    # retranslateUi
