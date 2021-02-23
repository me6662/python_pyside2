from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                               QLabel, QFrame, QSizePolicy, QPushButton,
                               QFileDialog, QMessageBox)
from PySide2.QtGui import QPixmap, QImage
import sys

from pyside2_ui.ui_image_loader import Ui_ImageLoader


class ImageLoader (QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.ui = Ui_ImageLoader()
        self.ui.setupUi(self)

    # Slot

    def open(self):
        fileName, _ = QFileDialog.getOpenFileName(self,
                                                  "Open Image File", ".", "Images (*.png *.xpm *.jpg)")
        if fileName != "":
            self.load(fileName)

    def load(self, fileName):
        image = QImage(fileName)

        if image.isNull():
            QMessageBox.information(
                self, QApplication.applicationName(), "Cannot load"+fileName)
            self.setWindowTitle(u"Image Loader by YDG")
            self.setPixmap(QPixmap())

        self.ui.imageLabel.setPixmap(QPixmap.fromImage(image))
        self.setWindowTitle(fileName)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    image_loader = ImageLoader()

    image_loader.show()
    app.exec_()
