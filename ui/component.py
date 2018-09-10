# -*- coding: utf-8 -*-
"""
This is the basic component for qtObject
"""
from PyQt5.QtWidgets import QLabel, QSizePolicy, QFrame
from PyQt5.QtCore import Qt
import subprocess, cv2


class basicLabel(QLabel):
    def __init__(self, label_name=None):
        self.label_name = label_name
        self.setObjectName(self.label_name)
        self.config(self)
        self.setSizePolicy(self.sizePolicy)

        # Picture auto adaptation.
        self.setScaledContents(True)
        # Label Frame
        self.setFrameShape(QFrame.Box)
        self.setAlignment(Qt.AlignCenter)

        self.setGeometry(300,300)

    def config(self):
        self.sizePolicy = QSizePolicy(QSizePolicy.Expanding,
                                      QSizePolicy.Expanding)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)
        self.sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())

class basicTool():
    def availableCamera(self):
        cmd = 'ls /dev/video*'
        cam_lst = subprocess.getoutput(cmd).splitlines()
        for cam in cam_lst:
            capture = cv2.VideoCapture(cam)
            if not capture.isOpened():
                cam_lst.remove(cam)
        return cam_lst



if __name__ == '__main__':
    t = basicTool()
    lst = t.availableCamera()
    print(len(lst))
    pass