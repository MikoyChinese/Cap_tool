# -*- coding: utf-8 -*-
"""
This is the basic component for qtObject
"""
from PyQt5.QtWidgets import QLabel, QComboBox, QSizePolicy, QFrame, QWidget, QMessageBox
from PyQt5.QtCore import Qt, QSize
import subprocess, cv2


class basicLabel(QLabel):

    def __init__(self, label_name=None, parent=None):
        super(basicLabel, self).__init__(parent)
        self.label_name = label_name
        self.config()
        self.setMinimumSize(QSize(417, 307))
        # Picture auto adaptation.
        self.setScaledContents(True)
        # Label Frame
        self.setFrameShape(QFrame.Box)
        self.setAlignment(Qt.AlignCenter)
        self.setObjectName(self.label_name)

    def config(self):
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)


class basicComboBox(QComboBox):

    def __init__(self, object_name=None, QWidget_parent=None):
        super(basicComboBox, self).__init__(QWidget_parent)
        self.object_name = object_name
        self.config()
        self.setObjectName(self.object_name)

    def config(self):
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)


class basicQuitMsgBox(QWidget):

    def __init__(self):
        super(basicQuitMsgBox, self).__init__()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Msg:', '确认退出吗？',
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class basicTool():

    def availableCamera(self):
        cmd = 'ls /dev/video*'
        cam_lst = subprocess.getoutput(cmd).splitlines()
        for cam in cam_lst:
            capture = cv2.VideoCapture(cam)
            if not capture.isOpened():
                cam_lst.remove(cam)
        return cam_lst

    def availableLabel(self, lst=list, count=int):
        if count == 2:
            lst.pop(1)
        if count == 4:
            lst.pop(1)
            lst.pop(4)
        if count == 5:
            lst.pop(4)
        return lst


if __name__ == '__main__':
    t = basicTool()
    lst = t.availableCamera()
    print(len(lst))
    pass