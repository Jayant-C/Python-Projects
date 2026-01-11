from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton
import sys

app = QApplication(sys.argv)
window = QWidget()
window.resize(400, 300)

input_box = QLineEdit(window)
input_box.move(100, 100)

button = QPushButton("Show Text", window)
button.move(100, 140)

def show_text():
    print(input_box.text())

button.clicked.connect(show_text)

window.show()
sys.exit(app.exec_())
