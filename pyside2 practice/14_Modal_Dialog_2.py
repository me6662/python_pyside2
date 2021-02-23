from PySide2.QtWidgets import (QApplication, QDial, QMainWindow, QTextEdit, QAction,
                               QMenu, QMenuBar, QDialog, QLabel, QLineEdit,
                               QGroupBox, QCheckBox, QPushButton, QGridLayout,
                               QHBoxLayout, QVBoxLayout)
from PySide2.QtGui import QIcon, QDoubleValidator

from pyside2_ui.ui_modal_dialog import Ui_GridDialog

import sys


class GridDialog (QDialog):
    def __init__(self, x, y, useGrid, useSnap, parent=None):
        QDialog.__init__(self, parent)
        self.ui = Ui_GridDialog()
        self.ui.setupUi(self)

        self.ui.xLineEdit.setText(str(x))
        self.ui.yLineEdit.setText(str(y))

        validator = QDoubleValidator(self)
        validator.setBottom(0.)
        self.ui.xLineEdit.setValidator(validator)
        self.ui.yLineEdit.setValidator(validator)

        self.ui.groupBox.setChecked(useGrid)
        self.ui.checkBox.setChecked(useSnap)
        self.ui.checkBox.setEnabled(useGrid)

    def gridInfo(self):
        x = float(self.ui.xLineEdit.text())
        y = float(self.ui.yLineEdit.text())
        useGrid = self.ui.groupBox.isChecked()
        useSnap = self.ui.checkBox.isChecked()

        return (x, y, useGrid, useSnap)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        # menu bar 에 추가할 항목
        action = QAction('set grid', self)
        action.triggered.connect(self.setGrid)  # 누를때 슬롯

        # 메뉴바
        myMenu = self.menuBar().addMenu("&action")
        myMenu.addAction(action)

        self.x = 10
        self.y = 10
        self.useGrid = True
        self.useSnap = False

    def setGrid(self):
        gridDialog = GridDialog(
            self.x, self.y, self.useGrid, self.useSnap, self)
        if gridDialog.exec():
            self.x, self.y, self.useGrid, self.useSnap = gridDialog.gridInfo()

            log = "Ok : useGrid ="+str(self.useGrid) + \
                  ", useSnap = " + str(self.useSnap) + \
                  ", x= " + str(self.x) + ", y = " + str(self.y)
            self.textEdit.append(log)
        else:
            self.textEdit.append("Cancel")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.resize(400, 300)
    mainWindow.show()

    mainWindow.setWindowTitle("Test GridDialog")

    mainWindow.show()
    app.exec_()
