import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 600, 353, 40)
        self.setWindowTitle('Вычисление выражений')

        self.input_1 = QLineEdit(self)
        self.input_1.move(5, 5)
        self.input_1.resize(150, 30)
        self.input_1.setText('Enter the eval')

        self.input_2 = QLineEdit(self)
        self.input_2.move(205, 5)
        self.input_1.resize(150, 30)

        self.button_switch = QPushButton(self)
        self.button_switch.move(160, 5)
        self.button_switch.resize(40, 30)
        self.button_switch.setText("->")
        self.button_switch.clicked.connect(self.calculate)

        self.show()

    def calculate(self):
        self.input_2.setText(f'{eval(self.input_1.text())}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())