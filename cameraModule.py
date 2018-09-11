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


class Camera_Timer(QThread):
    update = pyqtSignal()
    def __init__(self):
        super(Camera_Timer, self).__init__()
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
