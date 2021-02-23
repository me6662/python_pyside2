import sys
from PySide2.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QGridLayout,
                               QPushButton, QHBoxLayout, QVBoxLayout)

from PySide2.QtGui import QIcon
from PySide2.QtCore import Qt

import GridDialog_rc
# 먼저 pyside2-rcc Logon.qrc -o Logon_rc.py 명령으로 이미지를 py 파일로 만들어줘야함.


if __name__ == '__main__':

    app = QApplication(sys.argv)
    logon = QWidget()

    labelID = QLabel('&Id :')  # & 은 단축키 임 ^^
    # label 을 오른쪽에 정렬 + 높이 중앙
    labelID.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
    labelPW = QLabel('&Password :')

    lineEditId = QLineEdit()  # 텍스트박스
    lineEditPW = QLineEdit()
    lineEditPW.setEchoMode(QLineEdit.Password)  # 패스워드 형식

    labelID.setBuddy(lineEditId)  # buddy 로 묶으면 라벨이 텍스트 박스 아이디와 연동되고, & 이 없어짐;;
    labelPW.setBuddy(lineEditPW)

    buttonOk = QPushButton("&OK")
    buttonOk.setIcon(QIcon(":/images/ok.png"))

    layout1 = QGridLayout()  # 그리드 레이아웃 (행렬처럼)
    layout1.addWidget(labelID, 0, 0)
    layout1.addWidget(lineEditId, 0, 1)
    layout1.addWidget(labelPW, 1, 0)
    layout1.addWidget(lineEditPW, 1, 1)

    layout2 = QHBoxLayout()  # 가로로 요소 쌓는 박스  ( 1by n 행렬)
    layout2.addStretch()
    layout2.addWidget(buttonOk)

    mainLayout = QVBoxLayout()  # 세로로 요소 쌓는 박스 (n by 1 행렬)
    mainLayout.addLayout(layout1)
    mainLayout.addLayout(layout2)

    logon.setLayout(mainLayout)
    logon.setWindowTitle('Log On by YDG')
    logon.setWindowIcon(QIcon(':/images/ok.png'))

    buttonOk.clicked.connect(app.quit)

    logon.show()
    app.exec_()
