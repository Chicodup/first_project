from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

app = QApplication([])
win = QWidget()
win.resize(400,400)
win.setWindowTitle("Генератор переможця")

Winner = QLabel("Номер переможця")
result = QLabel("?")
gen_btn = QPushButton("Згенерувати")
line = QVBoxLayout()
line.addWidget(Winner, alignment=Qt.AlignCenter)
line.addWidget(result, alignment=Qt.AlignCenter)
line.addWidget(gen_btn, alignment=Qt.AlignCenter)
win.setLayout(line)
win.show()
app.exec_()
