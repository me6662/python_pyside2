from PySide2.QtWidgets import *
"""
<from vs import>
from 이란 것이 있는 이유는 여러개의 모듈에 동일한 함수의 이름이나 모듈의 이름이 있을 수 있기 때문이다.
여러 모듈을 import 한 상태에서는 어떤 모듈의 함수인지 애매할 수 있기 때문이다.
그리고 밑에다가 더 쓸 부분을 줄일 수도 있고

만약에 위에서 그냥

import PySide2.QtWidgets 이렇게 했으면

밑에 QApplication 의 경우,

app = PySide2.QtWidgets.QApplication(sys.argv) 이렇게 존나게 길게 써야된다.
"""

import sys

if __name__ == '__main__':  # C++ 에서 int main () {~~} 여기에 해당되는 부분이라고 보면된다.
    app = QApplication(sys.argv)  # 윈도우에서 켜지는 App 생성

    window = QWidget()  # 거기에 최상위 레이블인 프로그램 창을 킴 (Widget:  사람눈깔에 보이는 창을 의미 , 사용자 입력에 반응함)
    window.resize(289, 170)  # 프로그램 창의 사이즈
    window.setWindowTitle("FIrst Qt Program by YDG")  # 이름

    # 이 Qwidget 이 최상위 이고, 그밑에 객체들은 다 부모객체를 가짐. 부모객체가 사라지면 자식객체도 사라짐
    # QLabel 은 Qwidget 의 자식 (라벨), window 는 부모객체
    label = QLabel('Hello Qt, I''m YDG', window)
    label.move(110, 80)

    window.show()  # widget 윈도우창에 보여지게함

    app.exec_()  # app 객체가 메시지루프 (?) 를 가동 >> 반응형으로 만든다는 소리인듯...
