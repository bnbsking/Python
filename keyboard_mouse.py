import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
class Window(QWidget):
    def __init__(self):
        super().__init__()       
        self.initUI()
        self.show()
    def initUI(self):
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Input Test')
        
        pixmap = QPixmap('9pix.png')
        pixmap = pixmap.scaled(400, 400, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.background = QLabel(self)
        self.background.setPixmap(pixmap)
        
        pixmap2 = QPixmap('now.png')
        pixmap2 = pixmap2.scaled(110, 110, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.block = QLabel(self)
        self.block.setPixmap(pixmap2)
        self.block.move(30, 25)

    def keyPressEvent(self, event): # cannot modify name
        if event.key()==16777234 and self.block.x()>30: # left
            self.block.move(self.block.x()-115, self.block.y())
        elif event.key()==16777235 and self.block.y()>25: # up
            self.block.move(self.block.x(), self.block.y()-100)
        elif event.key()==16777236 and self.block.x()<260: # right
            self.block.move(self.block.x()+115, self.block.y())
        elif event.key()==16777237 and self.block.y()<225: # down
            self.block.move(self.block.x(), self.block.y()+100)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            print('You click left !')
        elif event.button() == Qt.RightButton:
            print('You click right !')
        elif event.button() == Qt.MidButton:
            print('You click middle !')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
# 16777235 up
# 16777237 down
# 16777234 left
# 16777236 right
