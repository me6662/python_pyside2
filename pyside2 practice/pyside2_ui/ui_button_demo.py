# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'Button_Demo.ui'
##
# Created by: Qt User Interface Compiler version 5.15.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import Logon_rc


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(305, 167)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 281, 151))
        self.main_layout = QVBoxLayout(self.verticalLayoutWidget)
        self.main_layout.setSpacing(6)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.main_layout.setContentsMargins(5, 10, 5, 10)
        self.btn_OK = QPushButton(self.verticalLayoutWidget)
        self.btn_OK.setObjectName(u"btn_OK")
        icon = QIcon()
        icon.addFile(u":/images/ok.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_OK.setIcon(icon)

        self.main_layout.addWidget(self.btn_OK)

        self.cb_case_sense = QCheckBox(self.verticalLayoutWidget)
        self.cb_case_sense.setObjectName(u"cb_case_sense")

        self.main_layout.addWidget(self.cb_case_sense)

        self.gb_sex = QGroupBox(self.verticalLayoutWidget)
        self.gb_sex.setObjectName(u"gb_sex")
        self.verticalLayoutWidget_2 = QWidget(self.gb_sex)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(9, 19, 251, 51))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.rb_male = QRadioButton(self.verticalLayoutWidget_2)
        self.rb_male.setObjectName(u"rb_male")
        self.rb_male.setChecked(True)

        self.verticalLayout.addWidget(self.rb_male)

        self.rb_female = QRadioButton(self.verticalLayoutWidget_2)
        self.rb_female.setObjectName(u"rb_female")

        self.verticalLayout.addWidget(self.rb_female)

        self.main_layout.addWidget(self.gb_sex)

        self.retranslateUi(Form)
        self.btn_OK.clicked.connect(Form.btnOk_click)
        self.cb_case_sense.toggled.connect(Form.cb_case_sense_toggled)
        self.rb_male.toggled.connect(Form.rb_onMale_toggled)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate(
            "Form", u"Button Demo by YDG", None))
        self.btn_OK.setText(QCoreApplication.translate("Form", u"OK", None))
        self.cb_case_sense.setText(QCoreApplication.translate(
            "Form", u"Case sensitivity", None))
        self.gb_sex.setTitle(QCoreApplication.translate("Form", u"Sex", None))
        self.rb_male.setText(QCoreApplication.translate("Form", u"Male", None))
        self.rb_female.setText(
            QCoreApplication.translate("Form", u"Female", None))
    # retranslateUi
