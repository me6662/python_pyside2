import sys

from PySide2.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QGridLayout,
                               QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox)
from PySide2.QtGui import QIcon
from PySide2.QtCore import Qt, Signal

from pyside2_ui.ui_logon import Ui_Logon


class Logon (QWidget):
    ok = Signal()

    def __init__(self, ids, pws, parent=None):
        QWidget.__init__(self, parent)

        self.listIds = ids
        self.listPWs = pws

        # ui 객체 생성
        self.ui = Ui_Logon()
        self.ui.setupUi(self)

        self.ui.buttonOk.clicked.connect(self.onOk)

    def onOk(self):
        if (self.ui.lineEditId.text() not in self.listIds):
            QMessageBox.critical(self, "Logon error", "Unregistered user")
            self.ui.lineEditId.setFocus()
        else:
            idx = self.listIds.index(self.ui.lineEditId.text())
            if self.ui.lineEditPW.text() != self.listPWs[idx]:
                QMessageBox.critical(self, "Logon error",
                                     "Incroreect password")
                self.ui.lineEditPW.setFocus()
            else:
                QMessageBox.information(self, "Welcome!",
                                        "Welcome! My friend.")
                self.ok.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ids = ['James', 'John', 'Jane']
    pws = ['123', '456', '789']

    logon = Logon(ids, pws)
    logon.ok.connect(app.exit)

    logon.show()
    app.exec_()
