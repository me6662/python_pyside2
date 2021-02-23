from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                               QLabel, QFrame, QSizePolicy, QPushButton,
                               QFileDialog, QMessageBox)
from PySide2.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator, QPixmap, QImage
import sys

from pyside2_ui.ui_spin_slider_progress import Ui_Form


class Form (QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = Form()

    form.show()
    app.exec_()
