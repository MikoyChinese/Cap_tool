
"""
This file uses PyQt5 to design a Application to Capture photoes.

"""

import cv2, sys, os, time
from PyQt5 import QtWidgets
from ui.mainwindow import Ui_MainWindow
from ui.component import basicTool
from ui.capwindow import Cap_MainWindow
from cameraModule import Camera, Save_img_Timer
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QInputDialog


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

        # Create the
        self.ui.origin_label_names = ["None", "cap45a1", "cap60a1", "cap90a1",
                                   "cap45a2", "cap60a2", "cap90a2"]

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

    Fixed_save_path = os.path.expanduser('~') + '/.data/' + time.strftime(
        '%Y%m%d')

    def __init__(self, mainWindow=None, *accept_data):
        self.mainWindow = mainWindow
        self.get_data(accept_data)
        self.ui = Cap_MainWindow()
        self.ui.setupUi(mainWindow)
        self.centralWidget = self.ui.centralWidget
        self.time = 13.00
        self.set_time()

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
                                       label_name=self.label_name[cap_index],
                                       width=self.cap_width, height=self.cap_height))

        self.ui.cap_ok_Button.pressed.connect(self._data)
        self.ui.cap_quit_Button.clicked.connect(self.set_time)
        self.ui.cap_next_Button.clicked.connect(self.next)
        self.ui.toolButton.clicked.connect(self.select_folder)
        self.ui.cap_ok_Button.released.connect(self.start)
        self.ui.lineEdit.editingFinished.connect(self.set_default)


    def show(self):
        for cap in self.cap_label_name:
            cap.refresh()

    def select_folder(self):
        path = os.path.abspath(os.path.dirname(__file__))
        path = QFileDialog.getExistingDirectory(self.centralWidget, path)
        self.ui.lineEdit_5.setText(path)

    def set_default(self):
        self.ui.lineEdit_2.setText('0')
        self.ui.lineEdit_4.setText('1')

    def next(self):
        direction = int(self.ui.lineEdit_4.text())
        next = direction + 1
        self.ui.lineEdit_4.setText(str(next))

    def _data(self):
        self.cvid = self.ui.lineEdit.text()
        self.date = self.ui.lineEdit_3.text()
        self.char = self.ui.lineEdit_2.text()
        self.direction = self.ui.lineEdit_4.text()
        self.save_path = Fixed_save_path
        if self.save_path[-1] == '/':
            pass
        else:
            self.save_path += '/'

    def start(self):
        self.ui.cap_ok_Button.setEnabled(False)
        self.save_img_timer = Save_img_Timer(parent=self, cap_Objects=self.cap_label_name, time=self.time)
        self.save_img_timer.send_msg.connect(self.update_textBrowser)
        self.save_img_timer.start()



    def save_img(self, img, label_name):

        save_dir = self.save_path + self.cvid + '/' + label_name + '/' + \
                   self.direction + '/'
        img_name = self.cvid + '_' + self.char + '_' + self.date + '_' + \
                   label_name
        cv2.imwrite()



    def set_time(self):
        reply, ok = QInputDialog.getDouble(self.centralWidget, '拍照周期', '请输入拍照周期(单位 s)： ', 13, 0, 999,3)
        if ok:
            self.time = reply


    def get_data(self, data):
        if len(data):
            self.cap_width = data[0]
            self.cap_height = data[1]
            self.label_name_index = data[2]
            self.label_name = data[3]

    def update_textBrowser(self, msg):
        self.ui.textBrowser.append(msg)



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
    dir_path = os.path.join(os.path.dirname(__file__), 'log')
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    Fixed_save_path = os.path.expanduser('~') + '/.data/' + time.strftime(
        '%Y%m%d')
    if not os.path.exists(Fixed_save_path):
        os.makedirs(Fixed_save_path)


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

