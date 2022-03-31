import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
import PyQt6.QtWidgets as widget
from components.book_entry import BookEntry

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self._createUI()
    
    def _createUI(self):
        central = widget.QWidget()
        layout = widget.QHBoxLayout()
        central.setLayout(layout)
        self.button = widget.QPushButton()
        self.button.setText("HIIII")
        self.button2 = widget.QPushButton()
        self.button2.setText("YEET")
        self.button3 = widget.QPushButton("HOLAA!!")
        layout.addWidget(self.button)
        layout.addWidget(self.button2)
        layout.addWidget(BookEntry())
        self.setCentralWidget(central)




app = QApplication(sys.argv)
window = Main()
window.show()
app.exec()