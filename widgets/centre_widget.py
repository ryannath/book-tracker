from typing import Optional
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt

class CentreWidget(QWidget):

    newBookButton: QPushButton
    """Button to add a new button to the profile"""

    def __init__(self, parent: Optional[QWidget]=None) -> None:
        super().__init__(parent)
        self._createUI()

    def _createUI(self) -> None:
        self.newBookButton = QPushButton("Add New Book")
        layout = QVBoxLayout()
        layout.addWidget(self.newBookButton)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(layout)
    