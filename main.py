import sys
import io
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

f = open('UI.ui', 'r', encoding='UTF-16')


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        f2 = io.StringIO(f)
        uic.loadUi(f2, self)

    def initUI(self):
        pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
