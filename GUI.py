from sys import argv, exit
from typing import List
from functools import partial

from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout


class GUI:
    def __init__(self):
        self.__app: QApplication = QApplication(argv)
        self.__frame: QWidget = QWidget()
        self.__panel: QVBoxLayout = QVBoxLayout()
        self.__buttons: List[QPushButton] = []
        self.__label: QLabel = QLabel()
        self.__numPressButt: int = 0
        self.__press: bool = False

    def exec(self):
        exit(self.__app.exec_())

    def generation(self) -> None:
        self.__app.setStyleSheet('''
            QLabel#label {
                font: bold 20px
            }

            QPushButton#stdButt, QPushButton#wrongAns {
                border-style: outset
                border-width: 2px
                border-radius: 10px
                border-color: #2F2F2F
                font: bold 10px
                padding: 6px
            }

            QPushButton#stdButt {
                background-color: #666
            }

            QPushButton#wrongAns {
                background-color: #FF0000
            }
        ''')
        self.__label.setObjectName('label')
        self.__label.setAlignment(Qt.AlignHCenter)
        v_box = QVBoxLayout()
        v_box.addWidget(self.__label)
        for numButt in range(4):
            self.__buttons.append(QPushButton())
            self.__buttons[numButt].setObjectName('stdButt')  # временно
            self.__buttons[numButt].clicked.connect(partial(self.__action_performed, numButt))
            v_box.addWidget(self.__buttons[numButt])
        h_box = QHBoxLayout()
        h_box.addLayout(v_box)
        self.__frame.setLayout(h_box)
        self.__frame.showFullScreen()

    def set_quest_frame(self, quest: str, texts_ans: List[str]) -> None:
        self.__label.setText(quest)
        for numButt in range(4):
            self.__buttons[numButt].setStyleSheet('background-color: #00CED1')
            self.__buttons[numButt].setText(texts_ans[numButt])

    def get_response(self) -> int:
        while not self.__press:
            pass
        self.__press = False
        return self.__numPressButt

    def wrong_ans(self) -> None:
        self.__buttons[self.__numPressButt].setStyleSheet('background-color: #ff0000')

    def end_of_quiz(self) -> None:
        self.__label.setText("Все раунды пройдены")
        for numButt in range(4):
            self.__buttons[numButt].setDisabled(True)

    def create_error_window(self, error_files: List[str], fatal_error: bool) -> None:
        screen_size: QRect = QApplication.desktop().screenGeometry()
        half_of_screen_width: int = screen_size.width() / 2
        half_of_screen_height: int = screen_size.height() / 2
        self.__frame.resize(half_of_screen_width / 3, half_of_screen_height / 4)
        text: str = ''
        if fatal_error:
            text += '<html><p>Не удалось создать файлы:</p>'
        else:
            text += '<html><p>В этих файлах не достаёт данных:</p>'
        for emptyFile in error_files:
            text += '<p>' + emptyFile + '</p>'
        text += '</html>'
        self.__label.setText(text)
        self.__label.setStyleSheet('color: #ff0000')
        v_box = QVBoxLayout()
        v_box.addWidget(self.__label)
        self.__frame.setLayout(v_box)
        self.__frame.show()
        exit(self.__app.exec_())

    def __action_performed(self, num_butt: int) -> None:
        self.__numPressButt = num_butt
        self.__press = True
