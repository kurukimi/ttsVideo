from PyQt5.QtCore import QSize, Qt, QPoint
from PyQt5.QtWidgets import QRubberBand, QHBoxLayout, QWidget
from qtcomponents.sGrip import SGrip

class ResizableRubberBand(QWidget):
    def __init__(self, parent=None):
        super(ResizableRubberBand, self).__init__(parent)

        self.draggable = True
        self.dragging_threshold = 5
        self.mousePressPos = None
        self.mouseMovePos = None
        self.borderRadius = 5

        self.setWindowFlags(Qt.SubWindow)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(
            SGrip(self), 0,
            Qt.AlignLeft | Qt.AlignTop)
        layout.addWidget(
            SGrip(self), 0,
            Qt.AlignRight | Qt.AlignBottom)
        self._band = QRubberBand(
            QRubberBand.Rectangle, self)
        self._band.show()
        self.setGeometry(150, 150, 150, 150)
        self.show()

    def resizeEvent(self, event):
        x = event.size().width()
        y = event.size().height()
        newPos = QSize(x, y)
        self._band.resize(newPos)

    def mousePressEvent(self, event):
        if self.draggable and event.button() == Qt.RightButton:
            self.mousePressPos = event.globalPos()                # global
            self.mouseMovePos = event.globalPos() - self.pos()    # local
        super(ResizableRubberBand, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.draggable and event.buttons() & Qt.RightButton:
            globalPos = event.globalPos()
            moved = globalPos - self.mousePressPos
            if moved.manhattanLength() > self.dragging_threshold:
                # Move when user drag window more than dragging_threshold
                diff = globalPos - self.mouseMovePos
                image_origo = (self.parent().size() - self.parent().pixmap().size()) / 2
                image_cons = image_origo + self.parent().pixmap().size() - self.size()
                newPos = QPoint(min(max(diff.x(), image_origo.width()), image_cons.width()), min(max(diff.y(), image_origo.height()), image_cons.height()))
                self.move(newPos)
                
                self.mouseMovePos = globalPos - self.pos()
        super(ResizableRubberBand, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.mousePressPos is not None:
            if event.button() == Qt.RightButton:
                moved = event.globalPos() - self.mousePressPos
                if moved.manhattanLength() > self.dragging_threshold:
                    # Do not call click event or so on
                    event.ignore()
                self.mousePressPos = None
        super(ResizableRubberBand, self).mouseReleaseEvent(event)

    # def paintEvent(self, event):
    #     # Get current window size
    #     window_size = self.size()
    #     qp = QPainter()
    #     qp.begin(self)
    #     qp.setRenderHint(QPainter.Antialiasing, True)
    #     qp.drawRoundedRect(0, 0, window_size.width(), window_size.height(),
    #                        self.borderRadius, self.borderRadius)
    #     qp.end()
