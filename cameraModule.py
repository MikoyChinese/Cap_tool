# -*- coding: utf-8 -*-

"""
--------------------------------------------------------------------------------
This part is main for Camera, it include the class Camera, Timer, subThread
save_img_timer.
Camera: a basic class such like cv2.VideoCapture().
Timer: a Timer thread, to control your process when to start and do what.
Save_img_Timer: a subThread to handle save img.
--------------------------------------------------------------------------------
"""

import cv2, os, sys, time
import numpy as np
from loggingModule import MyLogging
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QThread, QMutex, QMutexLocker, pyqtSignal


class Camera():

    def __init__(self, capture=cv2.VideoCapture, width=800, height=600,
                 label=None, label_name=None):
        # Get the capture object from the MainWindow init.
        self.capture = capture
        self.capture.set(3, int(width))
        self.capture.set(4, int(height))
        self.width = width
        self.height = height
        self.label = label
        self.label_name = label_name
        self.currentFrame = np.array([])
        self.logger = MyLogging(logger_name='user').logger
        self.logger.info('Create [Capture]: %s [Label_name]: %s'
                         %(self.capture, self.label_name))

    def getFrame(self):
        try:
            # Get frame and convert it to PixMap
            ret, img = self.capture.read()
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            # Add the hisself Cap object's label name in pic top.
            if self.label_name:
                cv2.putText(img, self.label_name,(18,56), 0, 1,
                            (129,216,207), 3)
            # Get the height, width, byserPer from this img.
            height, width, bytesPer = img.shape
            # bytesPerLine = bytesPer*3
            # Convert the img to QPixmap type, because the QtLabel just
            # accept this type.
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
        self.logger.info("Camera_Timer: [%s] has created." % self.cap_timer)
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
            time.sleep(0.27)

    def stop(self):
        with QMutexLocker(self.mutex):
            self.stoped = True


    def isStoped(self):
        with QMutexLocker(self.mutex):
            return self.stoped


class Save_img_Timer(QThread):

    """
    Send_msg will emit the capture process to capWindow's textBroswer.
    Creat_dirs_msg will emit the new creating dirs to capWindow's textBroswer.

    :param
    parent: It is the who create or init The Save_img_Timer class.
    cap_Objects: a list of all avaliable Cameras on PC.
    time: The time of capturing 32 pics to spend.
    save_dirs: a list of to save dirs to save img by needing.
    img_names: a list of how to save img with your name.
    """
    send_msg = pyqtSignal(str)
    creat_dirs_msg = pyqtSignal(str)

    def __init__(self, parent=None, cap_Objects=None, time=float):
        super(Save_img_Timer, self).__init__()
        self.parent = parent
        self.cap_Objects = cap_Objects
        self.time = time/32
        self.save_dirs = []
        self.img_names = []
        self.logger = MyLogging(logger_name='user').logger

        for cap_Object in self.cap_Objects:
            self.save_dirs.append(self.parent.save_path + self.parent.cvid + '/'
                                  + cap_Object.label_name + '/' + \
                                  self.parent.direction + '/')

            self.img_names.append(self.parent.cvid + '_' + self.parent.char + '_' + \
                                  self.parent.date + '_' + cap_Object.label_name +\
                                  '_' + self.parent.direction)

        for save_dir in self.save_dirs:
            dir_msg = '/' + '/'.join(save_dir.split('/')[-4:-1])
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)
                self.logger.info('Create dir [%s]' % save_dir)
                msg = 'Create dir [%s]' % dir_msg
                self.creat_dirs_msg.connect(self.parent.update_textBrowser)
                self.creat_dirs_msg.emit(msg)


        self.index = 1
        self.isStop = False

    def run(self):
        msg = '[CVID]: %s [DIRECTION]: %s [ACTIVED]: Start.' % (self.parent.cvid, self.parent.direction)
        self.logger.info(msg)
        self.send_msg.emit(msg)
        num = len(self.cap_Objects)
        while not self.isStop:
            self.imgs = []
            self.file_names = []
            for i in range(num):
                ret, img = self.cap_Objects[i].capture.read()
                file_name = self.img_names[i] + '_' + str(self.index) + '.jpg'
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
                msg = '[CVID]: %s [DIRECTION]: %s [ACTIVED]: End.' % (self.parent.cvid, self.parent.direction)
                self.logger.info(msg)
                self.send_msg.emit(msg)
                self.parent.ui.cap_ok_Button.setEnabled(True)
                break







