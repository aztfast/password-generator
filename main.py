import string
import random
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLineEdit,
                             QSlider, QHBoxLayout, QVBoxLayout, QLCDNumber, QLabel,
                             QWidget, QRadioButton, QButtonGroup)


class Generator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password generator")
        self.setGeometry(200, 200, 400, 150)
        central_widget = QWidget()
        self.lay = QVBoxLayout(central_widget)
        QHlay = QHBoxLayout()
        QV_for_group = QVBoxLayout()
        self.group = QButtonGroup(self)
        self.btnletter = QRadioButton(self)
        self.btnletter.setText("only letters")
        self.btnletter.setChecked(True)
        self.btnsnumber = QRadioButton(self)
        self.btnsnumber.setText("only numbers")
        self.btnssymbol = QRadioButton(self)
        self.btnssymbol.setText("symbols")
        self.group.addButton(self.btnletter)
        self.group.addButton(self.btnsnumber)
        self.group.addButton(self.btnssymbol)
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(6, 32)
        self.slider.setValue(8)
        self.passwd_line = QLineEdit(self)
        self.generate_btn = QPushButton("Generate", self)
        self.lcd = QLCDNumber(self)
        self.lcd.display("8")
        QHlay.addWidget(self.slider)

        QHlay.addWidget(self.lcd)
        QV_for_group.addWidget(self.btnletter)
        QV_for_group.addWidget(self.btnsnumber)
        QV_for_group.addWidget(self.btnssymbol)
        QHlay.addLayout(QV_for_group)
        self.setCentralWidget(central_widget)
        self.lay.addLayout(QHlay)
        self.slider.valueChanged.connect(self.set_val)
        self.lay.addWidget(self.generate_btn)
        self.lay.addWidget(self.passwd_line)
        self.setLayout(self.lay)
        self.generate_btn.clicked.connect(self.generate)

    def set_val(self):
        self.lcd.display(self.slider.value())

    def generate(self):
        password = ""
        curr_symbol_type = self.group.checkedButton().text()
        if curr_symbol_type == "symbols":
            symbols = string.ascii_letters + string.digits
            for i in range(self.slider.value()):
                password += random.choice(symbols)
        elif curr_symbol_type == "only numbers":
            for i in range(self.slider.value()):
                password += random.choice(string.digits)
        elif curr_symbol_type == "only letters":
            for i in range(self.slider.value()):
                password += random.choice(string.ascii_letters)
        self.passwd_line.setText(password)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Generator()
    window.show()
    sys.exit(app.exec())
