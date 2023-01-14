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

        self.input_1 = QLineEdit('edit1', self)
        self.input_1.move(70, 5)
        self.input_1.setVisible(self.checkbox_1.isChecked())

        self.show()

    def change_visible(self, state):
        if self.checkbox_1.isChecked():
            self.input_1.setVisible(True)
        else:
            self.input_1.setVisible(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())