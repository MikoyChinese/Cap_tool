# -*- coding: utf-8 -*-
"""
This file uses PyQt5 to design a Application to Capture photoes.

"""
import numpy as np
import cv2, time, sys
from PyQt5.QtGui import QImage, QPixmap
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, QMutex, QMutexLocker, pyqtSignal, QTimer
from loggingModule import MyLogging
from ui.mainwindow import Ui_MainWindow
from ui.component import basicTool


class Cap():
    def __init__(self, capture=cv2.VideoCapture(), label=None):
        # Get the capture object from the MainWindow init.
        self.capture = capture
        self.capture.set(3, 800)
        self.capture.set(4, 600)
        self.label = label
        self.currentFrame = np.array([])
        self.logger = MyLogging(logger_name='user').logger

    def getFrame(self):
        try:
            # Get frame and convert it to PixMap
            ret, self.currentFrame = self.capture.read()
            self.currentFrame = cv2.cvtColor(self.currentFrame, cv2.COLOR_BGR2RGB)
            height, width, bytesPer = self.currentFrame.shape
            # bytesPerLine = bytesPer*3
            img = QImage(self.currentFrame, width, height,
                  QImage.Format_RGB888)
            img = QPixmap.fromImage(img)
            # Set label show img. And update it.
            self.label.setPixmap(img)
        except:
            self.logger.error('Some error happened in <cap_tool.py | '
                              'getFrame>.')
            sys.exit(0)

    def refresh(self):
        # 1. Create a new Thread Class and Init it.
        self.cap_timer = Cap_Timer()
        # 2. Connect the thing let signal to do it.
        self.cap_timer.update.connect(self.getFrame)
        # 3. Start Thread.
        try:
            self.cap_timer.start()
        except BaseException:
            self.cap_timer.stoped


class Cap_Timer(QThread):
    update = pyqtSignal()
    def __init__(self):
        super(Cap_Timer, self).__init__()
        self.stoped = False
        self.mutex = QMutex()

    def run(self):
        with QMutexLocker(self.mutex):
            self.stoped = False

        while not self.stoped:
            self.update.emit()
            time.sleep(0.3)

    def stop(self):
        with QMutexLocker(self.mutex):
            self.stoped = True

    def isStoped(self):
        with QMutexLocker(self.mutex):
            return self.stoped



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)

    """
    cap = cv2.VideoCapture(0)
    cap2 = cv2.VideoCapture(1)
    cap_label_1 = Cap(capture=cap, label=ui.label_1)
    cap_label_1.refresh()
    
    cap_label_2 = Cap(capture=cap, label=ui.label_2)
    cap_label_2.refresh()
    cap_label_3 = Cap(capture=cap, label=ui.label_3)
    cap_label_3.refresh()
    cap_label_4 = Cap(capture=cap2, label=ui.label_4)
    cap_label_4.refresh()
    cap_label_5 = Cap(capture=cap2, label=ui.label_5)
    cap_label_5.refresh()
    cap_label_6 = Cap(capture=cap2, label=ui.label_6)
    cap_label_6.refresh()
    """
    label_lst = [ui.label_1, ui.label_2, ui.label_3, ui.label_4,
                 ui.label_5, ui.label_6]
    cap_label_name = []
    cap_name = []
    cam_lst = basicTool().availableCamera()

    for cam in cam_lst:
        cap_name.append(cv2.VideoCapture(cam))

    for i in range(len(cam_lst)):
        cap_label_name.append(Cap(capture=cap_name[i], label=label_lst[i]))

    for cap_label in cap_label_name:
        cap_label.refresh()


    mainWindow.update()
    mainWindow.show()
    sys.exit(app.exec_())
