
"""
This file uses PyQt5 to design a Application to Capture photoes.

"""

import cv2, sys, os
from PyQt5 import QtWidgets
from ui.mainwindow import Ui_MainWindow
from ui.component import basicTool
from ui.capwindow import Cap_MainWindow
from cameraModule import Camera
from PyQt5.QtWidgets import QMessageBox, QFileDialog


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
        self.label_lst = basicTool().availableLabel(lst=self.label_lst, count=len(cam_lst))


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


    def show(self):
        # Start all available Camera Thread to show in the UI.
        for cap_label in self.cap_label_name:
            cap_label.refresh()

    def quit(self):
        for cap_label in self.cap_label_name:
            cap_label.quit()
        cv2.destroyAllWindows()
        for cap in self.cap_objects:
            cap.release()



class Init_Cap():

    def __init__(self, mainWindow=None, *accept_data):
        self.mainWindow = mainWindow
        self.get_data(accept_data)
        self.ui = Cap_MainWindow()
        self.ui.setupUi(mainWindow)
        self.centralWidget = self.ui.centralWidget

        # List all Cap label we have in the UI.
        self.label_lst = [self.ui.label_1, self.ui.label_2, self.ui.label_3,
                          self.ui.label_4, self.ui.label_5, self.ui.label_6]

        # To save all available Camera name or path.
        self.cap_objects = []
        cam_lst = basicTool().availableCamera()
        self.label_lst = basicTool().availableLabel(lst=self.label_lst, count=len(cam_lst))

        for cam_name in cam_lst:
            cap = cv2.VideoCapture(cam_name)
            if cap.isOpened():
                self.cap_objects.append(cap)
            else:
                print('%s Camera can not open.' % cam_name)
        self.cap_label_name = []
        # Append the cap_label object.
        for i in range(len(self.cap_objects)):
            cap_index = int(self.label_name_index[i])
            self.cap_label_name.append(Camera(capture=self.cap_objects[cap_index],
                                       label=self.label_lst[i],
                                              label_name=self.label_name[cap_index]))


        self.ui.cap_quit_Button.clicked.connect(self.quit)
        self.ui.cap_next_Button.clicked.connect(self.next)
        self.ui.toolButton.clicked.connect(self.select_folder)
        self.ui.lineEdit.textChanged.connect(self.set_default)

    def show(self):
        for cap in self.cap_label_name:
            cap.refresh()

    def select_folder(self):
        path = os.path.abspath(os.path.dirname(__file__))
        path = QFileDialog.getExistingDirectory(self.centralWidget, path)
        self.ui.lineEdit_5.setText(path)

    def set_default(self):
        self.ui.lineEdit.setText('')
        self.ui.lineEdit_2.setText('0')
        self.ui.lineEdit_4.setText('1')

    def next(self):
        direction = int(self.ui.lineEdit_4.text())
        next = direction + 1
        self.ui.lineEdit_4.setText(str(next))

    def quit(self):
        reply = QMessageBox.question(self.centralWidget, 'Msg:', '确认退出吗？',
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.mainWindow.close()
        else:
            pass

    def get_data(self, data):
        if len(data):
            self.cap_width = data[0]
            self.cap_height = data[1]
            self.label_name_index = data[2]
            self.label_name = data[3]



class Handle():
    def __init__(self, mainWindow=QtWidgets.QMainWindow,
                 parent=Ui_MainWindow, widget=None, main=None):
        self.mainWindow = mainWindow
        self.parent = parent
        self.widget = widget
        self.main = main

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
        width, height, label_name_index, label_name = self.mainwindow_get_data()
        self.init_Cap = Init_Cap(self.mainWindow, width, height,
                                 label_name_index, label_name)
        self.init_Cap.show()




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
        # Get the user choose comboBox value except None.
        for each in comboBox_lst:
            if each not in label_names and each != 'None':
                label_names.append(each)
            else:
                pass
        # Get the every Cap Object where it should show.
        label_name_index = []
        for each in label_names:
            label_name_index.append(origin_label_names.index(each))

        for i in range(len(label_name_index)):
            index = 0
            for each in label_name_index:
                if label_name_index[i] > int(each):
                    index += 1
            label_name_index[i] = index
        # The label_name_index will order by origin index, finally return
        # such as [1, 2, 0].

        return width, height, label_name_index, label_names


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()

    main = Init_config(mainWindow)
    main.show()

    handle = Handle(mainWindow=mainWindow, parent=main.ui,
                         widget=main.centralWidget, main=main)
    # Yes button what to do and Cancel button waht to do.
    main.ui.buttonBox.accepted.connect(main.quit)
    main.ui.buttonBox.accepted.connect(handle.start)
    main.ui.buttonBox.rejected.connect(handle.quit)


    mainWindow.update()
    mainWindow.show()

    sys.exit(app.exec_())

