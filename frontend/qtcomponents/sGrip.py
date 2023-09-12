from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtWidgets import QSizeGrip


class SGrip(QSizeGrip):

    def __init__(self, parent):
        super().__init__(parent)
        self.mouseMovePos = None
        self.button = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.button = "left"
            self.mouseMovePos = event.globalPos() - QPoint(self.parent().pos().x() + self.parent().width(), self.parent().pos().y() + self.parent().height())
            self.origo = QPoint(self.parent().pos().x(), self.parent().pos().y())
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.button == "left" and self.parent().parent() and self.parent().parent().pixmap():
            diff = event.globalPos() - self.mouseMovePos

            image_origo = (self.parent().parent().size() - self.parent().parent().pixmap().size()) / 2
            image_cons = image_origo + self.parent().parent().pixmap().size()
            newPos = QPoint(min(max(diff.x(), image_origo.width()), image_cons.width()), min(max(diff.y(), image_origo.height()), image_cons.height()))
            print(f"origo {QPoint(self.parent().pos().x(), self.parent().pos().y())}, size {self.parent().size()}")
            self.parent().setGeometry(QRect(self.origo, newPos).normalized())
    
    def mouseReleaseEvent(self, event):
        self.button = None
        super(SGrip, self).mouseReleaseEvent(event)
