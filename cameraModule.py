# -*- coding: utf-8 -*-
"""
    This is the camera Module.
--------------------------------------------------------------------------------
"""

import cv2, sys, time
import numpy as np
from loggingModule import MyLogging
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QThread, QMutex, QMutexLocker, pyqtSignal


class Camera():
    def __init__(self, capture=cv2.VideoCapture(), width=800, height=600,
                 label=None, label_name=None):
        # Get the capture object from the MainWindow init.
        self.capture = capture
        self.capture.set(3, int(width))
        self.capture.set(4, int(height))
        self.label = label
        self.label_name = label_name
        self.currentFrame = np.array([])
        self.logger = MyLogging(logger_name='user').logger

    def getFrame(self):
        try:
            # Get frame and convert it to PixMap
            ret, self.currentFrame = self.capture.read()
            self.currentFrame = cv2.cvtColor(self.currentFrame, cv2.COLOR_BGR2RGB)
            if self.label_name:
                cv2.putText(self.currentFrame, self.label_name,(18,56), 0, 1,
                            (129,216,207), 3)
            height, width, bytesPer = self.currentFrame.shape
            # bytesPerLine = bytesPer*3
            img = QImage(self.currentFrame, width, height,
                  QImage.Format_RGB888)
            img = QPixmap.fromImage(img)
            # Set label show img. And update it.
            self.label.setPixmap(img)
        except:
            self.logger.error('Some error happened in <cameraModule.py | '
                              'getFrame>.')
            sys.exit(0)

    def refresh(self):
        # 1. Create a new Thread Class and Init it.
        self.cap_timer = Camera_Timer()
        # 2. Connect the thing let signal to do it.
        self.cap_timer.update.connect(self.getFrame)
        # 3. Start Thread.
        try:
            self.cap_timer.start()
        except BaseException:
            self.cap_timer.stop()
            self.cap_timer.quit()

    def quit(self):
        self.cap_timer.stop()
        self.cap_timer.quit()


class Camera_Timer(QThread):
    update = pyqtSignal()
    def __init__(self):
        super(Camera_Timer, self).__init__()
        self.stoped = False
        self.mutex = QMutex()

    def run(self):
        while not self.stoped:
            self.update.emit()
            time.sleep(0.1)

    def stop(self):
        with QMutexLocker(self.mutex):
            self.stoped = True


    def isStoped(self):
        with QMutexLocker(self.mutex):
            return self.stoped

