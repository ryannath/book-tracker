import pickle
from typing import Dict, Optional
from datastruct.book import Book
from PyQt6.QtWidgets import QFileDialog


def openProfile() -> Optional[Dict[str, Book]]:
        name = QFileDialog.getOpenFileName(caption="Open File", filter="Profile Files (*.bt)")[0]
        data: Dict[str, Book] = None
        if name:
            with open(name, "rb") as f:
                data = pickle.load(f)
                print(data)
        return data

def saveProfile(data) -> None:
        name = QFileDialog.getSaveFileName(caption="Save As", filter="Profile Files (*.bt)")[0]
        with open(name, "wb") as f:
            pickle.dump(data, f)