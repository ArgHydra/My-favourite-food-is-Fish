import sys
import io
from random import randint
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt

f = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>ILoveCartoonDogs</class>
 <widget class="QMainWindow" name="ILoveCartoonDogs">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1280</width>
    <height>900</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>1280</width>
    <height>900</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>1280</width>
    <height>900</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background:qlineargradient(spread:pad, x1:0.211, y1:0.221364, x2:0.773, y2:0.772727, stop:0 rgba(0, 255, 255, 255), stop:0.943182 rgba(0, 0, 0, 255))</string>
  </property>
  <widget class="QWidget" name="centralwidget"/>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>1280</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>

'''


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.button = None
        self.setMouseTracking(True)
        self.pen = QPainter()
        f2 = io.StringIO(f)
        uic.loadUi(f2, self)
        self.initUI()

    def initUI(self):
        self.button = QPushButton()
        self.button.setGeometry(580, 320, 121, 121)
        self.button.setStyleSheet('border-radius: 50%; background: rgb(255, 255, 127);')
        self.button.setText('Призови его братьев')
        self.button.clicked.connect(self.draw)

    def draw(self):
        R = randint(10, 200)
        self.pen.setBrush(QColor(255, 255, 127))
        self.pen.drawEllipse(randint(1, 1279), randint(1, 899), R, R)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
