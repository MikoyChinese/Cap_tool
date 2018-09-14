# -*- coding: utf-8 -*-
"""
    This is the camera Module.
--------------------------------------------------------------------------------
"""

import cv2, os, sys, time
import numpy as np
from loggingModule import MyLogging
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QThread, QMutex, QMutexLocker, pyqtSignal


class Camera():

    save_img = pyqtSignal(object, str)

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
        self.isSave = False

    def getFrame(self):
        try:
            # Get frame and convert it to PixMap
            ret, img = self.capture.read()
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            self.currentFrame = img

            #if self.isSave:
            #    self.save_img.emit(self.currentFrame, self.label_name)

            if self.label_name:
                cv2.putText(img, self.label_name,(18,56), 0, 1,
                            (129,216,207), 3)
            height, width, bytesPer = img.shape
            # bytesPerLine = bytesPer*3
            img = QImage(img, width, height,
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


class Save_img_Timer(QThread):

    send_msg = pyqtSignal(str)

    def __init__(self, parent=None, cap_Objects=None, time=float):
        super(Save_img_Timer, self).__init__()
        self.parent = parent
        self.cap_Objects = cap_Objects
        self.time = time/32
        self.save_dirs = []
        self.img_names = []

        for cap_Object in self.cap_Objects:
            self.save_dirs.append(self.parent.save_path + self.parent.cvid + '/'
                                  + cap_Object.label_name + '/' + \
                                  self.parent.direction + '/')

            self.img_names.append(self.parent.cvid + '_' + self.parent.char + '_' + \
                                  self.parent.date + '_' + cap_Object.label_name +\
                                  '_' + self.parent.direction)

        for save_dir in self.save_dirs:
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)


        self.index = 1
        self.isStop = False

    def __del__(self):
        self.wait()

    def run(self):
        num = len(self.cap_Objects)
        while not self.isStop:
            self.imgs = []
            self.file_names = []
            for i in range(num):
                ret, img = self.cap_Objects[i].capture.read()
                file_name = self.img_names[i] + '_' + str(self.index) + '.jpg'
                print(file_name)
                self.imgs.append(img)
                self.file_names.append(file_name)

            for i in range(num):
                cv2.imwrite(self.save_dirs[i] + self.file_names[i], self.imgs[i])

            msg = '[Cvid]:  %s  [Direction]:  %s  |  ---------->  %d\n' % (self.parent.cvid, self.parent.direction, self.index)
            self.send_msg.emit(msg)

            self.index += 1
            time.sleep(self.time)
            if self.index > 32:
                self.isStop = True
                break







