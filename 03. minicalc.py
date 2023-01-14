import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QLCDNumber


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 600, 370, 155)
        self.setWindowTitle('Вычисление выражений')

        self.label_num_1 = QLabel(self)
        self.label_num_1.move(10, 5)
        self.label_num_1.setText('1st Number (INT)')
        self.input_1 = QLineEdit(self)
        self.input_1.move(5, 30)
        self.input_1.resize(150, 30)

        self.label_num_2 = QLabel(self)
        self.label_num_2.move(10, 80)
        self.label_num_2.setText('2nd Number (INT)')
        self.input_2 = QLineEdit(self)
        self.input_2.move(5, 105)
        self.input_2.resize(150, 30)

        self.button_calc = QPushButton(self)
        self.button_calc.move(160, 65)
        self.button_calc.resize(60, 30)
        self.button_calc.setText("->")
        self.button_calc.clicked.connect(self.calculate)

        self.label_sum = QLabel(self)
        self.label_sum.move(250, 5)
        self.label_sum.setText('sum = ')
        self.label_diff = QLabel(self)
        self.label_diff.move(250, 45)
        self.label_diff.setText('diff = ')
        self.label_mult = QLabel(self)
        self.label_mult.move(250, 85)
        self.label_mult.setText('sum = ')
        self.label_eq = QLabel(self)
        self.label_eq.move(250, 125)
        self.label_eq.setText('sum = ')

        self.lcd_sum = QLCDNumber(self)
        self.lcd_sum.move(300, 5)
        self.lcd_diff = QLCDNumber(self)
        self.lcd_diff.move(300, 45)
        self.lcd_mult = QLCDNumber(self)
        self.lcd_mult.move(300, 85)
        self.lcd_eq = QLCDNumber(self)
        self.lcd_eq.move(300, 125)

        self.show()

    def calculate(self):
        self.lcd_sum.display(int(self.input_1.text()) + int(self.input_2.text()))
        self.lcd_diff.display(int(self.input_1.text()) - int(self.input_2.text()))
        self.lcd_mult.display(int(self.input_1.text()) * int(self.input_2.text()))
        if self.input_2.text() == '0':
            self.lcd_eq.display('Error')
        else:
            self.lcd_eq.display(round(int(self.input_1.text()) / int(self.input_2.text()), 3))




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())