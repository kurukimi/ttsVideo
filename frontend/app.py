from dataclasses import dataclass
from typing import Callable
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QImage, QPixmap, QColor, QPalette, QPainter
from PyQt5.QtCore import QSize, Qt, QPoint, QRect
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QRubberBand, QLabel, QFileDialog, QHBoxLayout, QVBoxLayout, QWidget, QPushButton
import urllib.request
from qtcomponents.imageLabel import ImageLabel
from qtcomponents.resizableRubberBand import ResizableRubberBand

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
        self.setMinimumSize(100, 100)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


@dataclass
class Action:
    name: str
    action: Callable


class ToolPanel(QWidget):

    def __init__(self, actions: list[Action]):
        super(ToolPanel, self).__init__()
        
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.layout)
        for action in actions:
            self._setButtons(action)
    
    def _setButtons(self, action: Action):
        button = QPushButton(action.name)
        button.clicked.connect(action.action)
        self.layout.addWidget(button)

# Subclass QMainWindow to customize your application's main window
class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.width = 1200
        self.height = 800
        self._setProperties()
        self._setLayouts()
        self.show()

    def _setActions(self):
        self.actions = [
            Action("Add rubberband", self.image_label.addRubberBand(ResizableRubberBand)),
            Action("Get dimensions", self.image_label.getRubberbandSelection)
        ]

    def _setProperties(self):
        self.setWindowTitle("My App")
        self.setMinimumSize(300, 200)
        self.resize(self.width, self.height)
        self.setAcceptDrops(True)
        self.image_label = ImageLabel(self)
        self._setActions()
        self.toolPanel = ToolPanel(self.actions)

    def _setLayouts(self):
        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.image_label, stretch=4)
        self.h_layout.addWidget(self.toolPanel, stretch=1)
        self.v_layout = QVBoxLayout()
        self.v_layout.addLayout(self.h_layout, stretch=3)
        self.v_layout.addWidget(Color("red"), stretch=1)
        self.setLayout(self.v_layout)

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            url = event.mimeData().urls()[0]
            if url.isLocalFile():
                image = url.toLocalFile()
            else:
                data = urllib.request.urlopen(url.url()).read()
                image = QImage()
                image.loadFromData(data)
            
            self.image_label.set_image(image)
            event.accept()
        
        else:
            event.ignore()


app = QApplication(sys.argv)

window = MainWindow()
app.exec()