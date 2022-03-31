from typing import Any

from PyQt6.QtCore import QObject


STYLE_PATH: str = "styles/main-window.css"

def loadStyle(obj: QObject, path: str = STYLE_PATH) -> None:
        """Applies all styling from given file"""
        with open(path, 'r') as f:
            obj.setStyleSheet(f.read())
