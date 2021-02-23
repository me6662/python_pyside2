from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                               QLabel, QFrame, QSizePolicy, QPushButton,
                               QFileDialog, QMessageBox)
from PySide2.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator, QPixmap, QImage
import sys

from pyside2_ui.ui_lineedit_combo import Ui_Form


class Form (QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Validator (line Edit 의 input 제한, setupUi 로 객체들을 만든다음에 코드로 수정)
        # Qt Designer 에는 수정 기능 없음
        self.ui.lineEdit_int.setValidator(QIntValidator(self))    # 정수
        self.ui.lineEdit_int.setValidator(
            QIntValidator(100, 999, self))    # 100..999사이의 정수

        self.ui.lineEdit_double.setValidator(
            QDoubleValidator(self))   # 실수, 1.2, -1.3, 1E-2 등 가능
        self.ui.lineEdit_double.setValidator(
            QDoubleValidator(-0.1, 100, 2, self))  # -0.1, 100 사이의 실수, 2개의 소수자리수만 허용.

        validator = QDoubleValidator(self)  # 0 이상 실수
        validator.setBottom(0.)
        self.ui.lineEdit_over0.setValidator(validator)

        # 복잡한 패턴 제약
        regExp = QRegExpValidator("[A-Za-z][1-9][0-9]{0,2}")
        # 첫 번째 문자는 대소문자의 알파벳이고, 두 번째는 1-9사이의 숫자가,
        # 이후 0-9사이의 숫자가 0개부터 2개까지 올 수 있도록 lineEdit의 입력을 제한한다는 의미이다.
        self.ui.lineEdit_combo.setValidator(QRegExpValidator(regExp, self))
        """
        regExp = QRegExp(“[A-Za-z]*")      # 알파벳만 임의의 개수만큼 가능
        regExp = QRegExp("[0-9]*")          # 숫자만 임의의 개수만큼 가능
        regExp = QRegExp("[A-Za-z0-9]*")  # 알파벳과 숫자만 임의의 개수만큼 가능
        """

    def onSelected(self, str):
        print('Combo Box changed', str)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = Form()

    form.show()
    app.exec_()
