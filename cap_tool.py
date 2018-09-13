
"""
This file uses PyQt5 to design a Application to Capture photoes.

"""

import cv2, sys
from PyQt5 import QtWidgets
from ui.mainwindow import Ui_MainWindow
from ui.component import basicTool
from ui.capwindow import Cap_MainWindow
from cameraModule import Camera
from PyQt5.QtWidgets import QMessageBox


class Init_config():

    def __init__(self, mainWindow=None):
        self.mainWindow = mainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(mainWindow)
        self.centralWidget = self.ui.centralWidget

        # List all label we have in the UI.
        self.label_lst = [self.ui.label_1, self.ui.label_2, self.ui.label_3,
                          self.ui.label_4, self.ui.label_5, self.ui.label_6]
        # To save the cap_label init name.
        self.cap_label_name = []
        # To save all available Camera name or path.
        self.cap_objects = []
        cam_lst = basicTool().availableCamera()
        # self.label_lst = basicTool().availableLabel(lst=self.label_lst, count=len(cam_lst))


        for cam_name in cam_lst:
            cap = cv2.VideoCapture(cam_name)
            if cap.isOpened():
                self.cap_objects.append(cap)
            else:
                print('%s Camera can not open.' % cam_name)

        # Append the cap_label object.
        for i in range(len(self.cap_objects)):
            self.cap_label_name.append(
                Camera(capture=self.cap_objects[i], label=self.label_lst[i]))

        self.handle = Handle(mainWindow=self.mainWindow, parent=self.ui, widget=self.centralWidget)
        self.ui.buttonBox.rejected.connect(self.handle.quit)

    def show(self):
        # Start all available Camera Thread to show in the UI.
        for cap_label in self.cap_label_name:
            cap_label.refresh()

    def quit(self):
        for cap_label in self.cap_label_name:
            cap_label.quit()
        for cap in self.cap_objects:
            cap.release()
        cv2.destroyAllWindows()



class Init_Cap():

    def __init__(self, mainWindow=None):
        self.mainWindow = mainWindow
        self.ui = Cap_MainWindow()
        self.ui.setupUi(mainWindow)
        self.centralWidget = self.ui.centralWidget

        # List all Cap label we have in the UI.
        self.label_lst = [self.ui.label_1, self.ui.label_2, self.ui.label_3,
                          self.ui.label_4, self.ui.label_5, self.ui.label_6]

        # To save all available Camera name or path.
        self.cap_objects = []
        cam_lst = basicTool().availableCamera()
        # self.label_lst = basicTool().availableLabel(lst=self.label_lst, count=len(cam_lst))

        for cam_name in cam_lst:
            cap = cv2.VideoCapture(cam_name)
            if cap.isOpened():
                self.cap_objects.append(cap)
            else:
                print('%s Camera can not open.' % cam_name)


class Handle():
    def __init__(self, mainWindow=QtWidgets.QMainWindow, parent=Ui_MainWindow, widget=None):
        self.mainWindow = mainWindow
        self.parent = parent
        self.widget = widget

    def quit(self):
        reply = QMessageBox.question(self.widget, 'Msg:', '确认退出吗？',
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.mainWindow.close()
        else:
            pass

    def start(self):
        self.parent.centralWidget.close()
        Init_Cap(self.mainWindow)


    def mainwindow_get_data(self):
        width = self.parent.lineEdit_width.text()
        height = self.parent.lineEdit_height.text()

        label_names = []
        origin_label_names = self.parent.origin_label_names.copy()
        origin_label_names.pop(0)
        comboBox_lst = [self.parent.comboBox_1.currentText(),
                        self.parent.comboBox_2.currentText(),
                        self.parent.comboBox_3.currentText(),
                        self.parent.comboBox_4.currentText(),
                        self.parent.comboBox_5.currentText(),
                        self.parent.comboBox_6.currentText()]

        for each in comboBox_lst:
            if each not in label_names and each != 'None':
                label_names.append(each)
            else:
                pass

        label_name_index = []
        for each in label_names:
            label_name_index.append(origin_label_names.index(each))

        return width, height, label_name_index


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()

    ui = Init_config(mainWindow)
    ui.show()

    mainWindow.update()
    mainWindow.show()

    sys.exit(app.exec_())

