import sys
from PySide2.QtWidgets import (QApplication, QMessageBox, QWidget, QLabel, QLineEdit, QGridLayout,
                               QPushButton, QHBoxLayout, QVBoxLayout)

from PySide2.QtGui import QIcon
from PySide2.QtCore import Qt, Signal

import Logon_rc

# class (super) : 상속임


class Logon(QWidget):
    ok = Signal()
    # 생성자 (self 는 걍 써줌 기본으로)

    def __init__(self, ids, pws, parent=None):
        # 보통 Qwidget 을 만들때, parent 를 넣어주는데, 없으면 default = None 임
        QWidget.__init__(self, parent)

        self.listIds = ids  # 클래스 생성자에다가 변수 걍 선언해도됨
        self.listPWs = pws

        self.labelId = QLabel('&Id :')
        self.labelId.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        self.labelPW = QLabel('&Password :')

        self.lineEditId = QLineEdit()
        self.lineEditPW = QLineEdit()
        # 문자열 나오는 형식을 설정함 (4종류 있음)
        self.lineEditPW.setEchoMode(QLineEdit.Password)

        self.labelId.setBuddy(self.lineEditId)
        self.labelPW.setBuddy(self.lineEditPW)

        self.buttonOk = QPushButton('&Ok')
        self.buttonOk.setIcon(QIcon(':/images/ok.png'))

        layout1 = QGridLayout()
        layout1.addWidget(self.labelId, 0, 0)
        layout1.addWidget(self.lineEditId, 0, 1)
        layout1.addWidget(self.labelPW, 1, 0)
        layout1.addWidget(self.lineEditPW, 1, 1)

        layout2 = QHBoxLayout()
        layout2.addStretch()
        layout2.addWidget(self.buttonOk)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(layout1)
        mainLayout.addLayout(layout2)

        self.setLayout(mainLayout)  # 되는 이유는 Qwidget 클래스를 상속했기 때문임
        self.setWindowTitle('Log on')
        self.setWindowIcon(QIcon(":/images/ok.png"))

        self.buttonOk.clicked.connect(self.onOk)  # 밑에 함수 연결

    def onOk(self):
        if (self.lineEditId.text() not in self.listIds):
            QMessageBox.critical(self, 'Logon Error', 'You are not my member.')
            self.lineEditId.setFocus()
        else:
            idx = self.listIds.index(self.lineEditId.text())

            if(self.lineEditPW.text() != self.listPWs[idx]):
                QMessageBox.critical(self, 'Logon Error', 'Wrong Number')
                self.lineEditPW.setFocus()
            else:
                self.ok.emit()  # ok 시그널 보냄


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ids = ['James', 'John', 'Jane']
    pws = ['123', '456', '789']

    logon = Logon(ids, pws)

    logon.ok.connect(app.exit)  # logon 에서 보내는 ok 시그널에 콜백함수 (여기선 exit) 연결

    logon.show()
    app.exec_()
