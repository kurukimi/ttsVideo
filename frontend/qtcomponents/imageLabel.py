
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QFileDialog
from qtcomponents.resizableRubberBand import ResizableRubberBand

class ImageLabel(QLabel):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.image = None
        #self.setPixmap(QPixmap().fromImage(self.image))
        self.setAlignment(Qt.AlignCenter)
        self.rubberbands = []
        self.setText('\n\n Drop Image Here \n\n')
        self.setStyleSheet('''
            QLabel{
                border: 1px dashed #aaa
            }
        ''')

    def addRubberBand(self, rubberBand: ResizableRubberBand):
        def execute():
            self.rubberbands.append(rubberBand(self))
        return execute
    
    def getRubberbandSelection(self):
        for rubberband in self.rubberbands:
            print(f"band {rubberband.geometry().getCoords()}")
            print(f"pix {self.getImageCoords()}()")

    def getImageCoords(self):
        imageOrigo = (self.size() - self.pixmap().size()) / 2
        downRight = imageOrigo + self.pixmap().size()
        return imageOrigo, downRight

    def mousePressEvent(self, event):
        if self.image == None:
            self.openImage()

    def set_image(self, image):
        self.image = QImage(image)
        if (self.image.height() > self.height() or self.image.width() > self.width()):
            self.setPixmap(QPixmap(self.image).scaled(self.width(), self.height(), Qt.KeepAspectRatio))
        else:
            #self.setMinimumSize(self.image.width(), self.image.height())
            self.setPixmap(QPixmap(self.image))

    def openImage(self):
        """Load a new image into the """
        image_file, _ = QFileDialog.getOpenFileName(self, "Open Image", 
                "", "Image files (*.jpg *.gif *.png *.jpeg)")
        if image_file:
            self.set_image(image_file)
            #image_size = self.image_label.sizeHint()
            #self.resize(self.pixmap().size())
    
    def resizeEvent(self, event):
        if self.image and (self.image.height() > self.height() or self.image.width() > self.width()):
            self.clear()
            self.setPixmap(QPixmap(self.image).scaled(self.width(), self.height(), Qt.KeepAspectRatio))
        return super().resizeEvent(event)
