from PySide2.QtWidgets import (QApplication, QMainWindow, QTextEdit, QAction,
                               QMenu, QMenuBar, QDialog, QLabel, QLineEdit, QComboBox,
                               QGroupBox, QCheckBox, QPushButton, QGridLayout,
                               QHBoxLayout, QVBoxLayout)
from PySide2.QtGui import QIcon, QDoubleValidator

from PySide2.QtCore import Signal
import FindReplaceDialog_rc
import sys

from pyside2_ui.ui_modaless_dialog import Ui_FindReplaceDialog

# Modaless Dialog
# 모달리스(modeless) 다이얼로그는 다이얼로그가 떠있는 상태에서 다른 작업을 할 수 있는 다이얼로그이다.
# Ok, Cancel 버턴을 가지는 모달 다이얼로그와 달리 Close 버턴으로 다이얼로그를 닫도록 설계되며
# 다른 버턴이나 위젯에 대한 반응으로 즉시 작업을 수행하도록 설계한다.


class FindReplaceDialog(QDialog):
    # find(findText,matchWholeWord,matchCase,upward)
    find = Signal(str, bool, bool, bool)
    # replace(findText,replaceText,matchWoleWord,matchCase,upward)
    replace = Signal(str, str, bool, bool, bool)
    # replaceAll(findText,replaceText,matchWoleWord,matchCase,upward)
    replaceAll = Signal(str, str, bool, bool, bool)

    def __init__(self, parent=None):
        QDialog.__init__(self)

        self.ui = Ui_FindReplaceDialog()
        self.ui.setupUi(self)

    def enableButtons(self):
        findText = self.ui.findComboBox.currentText()
        if findText != '':
            self.ui.findButton.setEnabled(True)

        replaceText = self.ui.replaceComboBox.currentText()
        if findText != "" and replaceText != "":
            self.ui.replaceButton.setEnabled(True)
            self.ui.replaceAllButton.setEnabled(True)

    def onFind(self):
        findText = self.ui.findComboBox.currentText()
        matchWholeWord = self.ui.checkBox.isChecked()
        matchCase = self.ui.checkBox_2.isChecked()
        upward = self.ui.checkBox_3.isChecked()

        index = self.ui.findComboBox.findText(findText)
        if index != 1:
            self.ui.findComboBox.removeItem(index)
        self.ui.findComboBox.insertItem(0, findText)
        self.ui.findComboBox.setCurrentIndex(0)

        self.find.emit(findText, matchWholeWord, matchCase, upward)

    def onReplace(self):
        findText = self.ui.findComboBox.currentText()
        replaceText = self.ui.replaceComboBox.currentText()
        matchWholeWord = self.ui.checkBox.isChecked()
        matchCase = self.ui.checkBox_2.isChecked()
        upward = self.ui.checkBox_3.isChecked()

        index = self.ui.findComboBox.findText(findText)
        if index != 1:
            self.ui.findComboBox.removeItem(index)
        self.ui.findComboBox.insertItem(0, findText)
        self.ui.findComboBox.setCurrentIndex(0)

        index = self.ui.replaceComboBox.findText(replaceText)
        if index != 1:
            self.ui.replaceComboBox.removeItem(index)
        self.ui.replaceComboBox.insertItem(0, replaceText)
        self.ui.replaceComboBox.setCurrentIndex(0)

        self.replace.emit(findText, replaceText,
                          matchWholeWord, matchCase, upward)

    def onRepalceAll(self):
        findText = self.ui.findComboBox.currentText()
        replaceText = self.ui.replaceComboBox.currentText()
        matchWholeWord = self.ui.checkBox.isChecked()
        matchCase = self.ui.checkBox_2.isChecked()
        upward = self.ui.checkBox_3.isChecked()

        index = self.ui.findComboBox.findText(findText)
        if index != 1:
            self.ui.findComboBox.removeItem(index)
        self.ui.findComboBox.insertItem(0, findText)
        self.ui.findComboBox.setCurrentIndex(0)

        index = self.ui.replaceComboBox.findText(replaceText)
        if index != 1:
            self.ui.replaceComboBox.removeItem(index)
        self.ui.replaceComboBox.insertItem(0, replaceText)
        self.ui.replaceComboBox.setCurrentIndex(0)

        self.replaceAll.emit(findText, replaceText,
                             matchWholeWord, matchCase, upward)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        action = QAction("Test", self)
        action.triggered.connect(self.findReplace)

        myMenu = self.menuBar().addMenu("&Test")
        myMenu.addAction(action)

        self.findReplaceDialog = None

    def findReplace(self):
        if self.findReplaceDialog is None:
            self.findReplaceDialog = FindReplaceDialog()
            self.findReplaceDialog.find.connect(self.find)
            self.findReplaceDialog.replace.connect(self.replace)
            self.findReplaceDialog.replaceAll.connect(self.replaceAll)

        # Make Modaless!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.findReplaceDialog.show()
        self.findReplaceDialog.raise_()  # Note raise_() not raise()
        self.findReplaceDialog.activateWindow()

    def find(self, findText, matchWholeWord, matchCase, upward):
        log = "Find operation " + findText + \
              "\nMatchWoleWord : " + str(matchWholeWord) + \
              "\nMatchCase : " + str(matchCase) + \
              "\nUpward : " + str(upward)
        self.textEdit.append(log)

    def replace(self, findText, replaceText, matchWholeWord, matchCase, upward):
        log = "Replace operation " + findText + " " + replaceText + \
              "\nMatchWoleWord : " + str(matchWholeWord) + \
              "\nMatchCase : " + str(matchCase) + \
              "\nUpward : " + str(upward)
        self.textEdit.append(log)

    def replaceAll(self, findText, replaceText, matchWholeWord, matchCase, upward):
        log = "ReplaceAll operation " + findText + " " + replaceText + \
              "\nMatchWoleWord : " + str(matchWholeWord) + \
              "\nMatchCase : " + str(matchCase) + \
              "\nUpward : " + str(upward)
        self.textEdit.append(log)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()

    app.exec_()
