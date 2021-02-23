from PySide2.QtCore import Signal

# Must inherit QObject for signals
"""

시그널-슬롯은 Qt에서 제공하는 고수준의 명령 처리 방식으로 이해할 수 있으며, 
대부분 Qt 클래스의 최상위 클래스인 QObject로 부터 상속받은 클래스에서 사용가능하다. 
한편, 저수준의 명령처리방식으로 위젯을 대상으로 하는 메세지(이벤트)가 있다.
"""


class Communicate(QObject):
    speak = Signal()

    def __init__(self):
        super(Communicate, self).__init__()
        self.speak.connect(self.say_hello)

    def speaking_method(self):
        self.speak.emit()

    def say_hello(self):
        print("Hello")


someone = Communicate()
someone.speaking_method.connect(some_slot)  # 시그널-슬롯 연결

# 대충 이런형식인데 logon2 에 가면 자세히 쓰는법 나와있음
