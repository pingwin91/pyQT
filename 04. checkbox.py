import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 600, 353, 40)
        self.setWindowTitle('Вычисление выражений')

        self.checkbox_1 = QCheckBox('edit1', self)
        self.checkbox_1.move(5, 5)
        self.checkbox_1.stateChanged.connect(self.change_visible)
        self.checkbox_2 = QCheckBox('edit1', self)
        self.checkbox_2.move(5, 30)
        self.checkbox_2.stateChanged.connect(self.change_visible)
        self.checkbox_3 = QCheckBox('edit1', self)
        self.checkbox_3.move(5, 60)
        self.checkbox_3.stateChanged.connect(self.change_visible)
        self.checkbox_4 = QCheckBox('edit1', self)
        self.checkbox_4.move(5, 90)
        self.checkbox_4.stateChanged.connect(self.change_visible)

        self.input_1 = QLineEdit('edit1', self)
        self.input_1.move(70, 5)
        self.input_1.setVisible(self.checkbox_1.isChecked())
        self.input_2 = QLineEdit('edit1', self)
        self.input_2.move(70, 30)
        self.input_2.setVisible(self.checkbox_2.isChecked())
        self.input_3 = QLineEdit('edit1', self)
        self.input_3.move(70, 60)
        self.input_3.setVisible(self.checkbox_3.isChecked())
        self.input_4 = QLineEdit('edit1', self)
        self.input_4.move(70, 90)
        self.input_4.setVisible(self.checkbox_4.isChecked())

        self.show()

    def change_visible(self, state):
        self.input_1.setVisible(self.checkbox_1.isChecked())
        self.input_2.setVisible(self.checkbox_2.isChecked())
        self.input_3.setVisible(self.checkbox_3.isChecked())
        self.input_4.setVisible(self.checkbox_4.isChecked())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())