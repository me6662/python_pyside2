import sys

from PySide2.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QGridLayout,
                               QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox)
from PySide2.QtGui import QIcon
from PySide2.QtCore import Qt, Signal, Slot

from pyside2_ui.ui_button_demo import Ui_Form


class Form (QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

    # Slot
    def btnOk_click(self):
        print('okButtonClicked')

    def cb_case_sense_toggled(self, toggle):
        print('okCaseSensitivity', toggle)
        print(self.ui.cb_case_sense.isChecked())

    def rb_onMale_toggled(self, toggle):
        print('onMale', toggle)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = Form()

    form.show()
    app.exec_()
