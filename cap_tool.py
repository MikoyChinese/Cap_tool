
"""
This file uses PyQt5 to design a Application to Capture photoes.

"""

import cv2, sys
from PyQt5 import QtWidgets
from ui.mainwindow import Ui_MainWindow
from ui.component import basicTool
from cameraModule import Camera


class Init_config():
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        mainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(mainWindow)

        # List all label we have in the UI.
        label_lst = [ui.label_1, ui.label_2, ui.label_3, ui.label_4,
                     ui.label_5, ui.label_6]
        # To save the cap_label init name.
        cap_label_name = []
        # To save all available Camera name or path.
        cap_name = []
        cam_lst = basicTool().availableCamera()
        for cam in cam_lst:
            cap_name.append(cv2.VideoCapture(cam))

        # Append the cap_label object.
        for i in range(len(cam_lst)):
            cap_label_name.append(
                Camera(capture=cap_name[i], label=label_lst[i]))
        # Start all available Camera Thread to show in the UI.
        for cap_label in cap_label_name:
            cap_label.refresh()

        mainWindow.update()
        mainWindow.show()

        sys.exit(app.exec_())


class Init_Cap():
    pass



if __name__ == '__main__':

    Init_config()


    """
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)

    # List all label we have in the UI.
    label_lst = [ui.label_1, ui.label_2, ui.label_3, ui.label_4,
                 ui.label_5, ui.label_6]
    # To save the cap_label init name.
    cap_label_name = []
    # To save all available Camera name or path.
    cap_name = []
    cam_lst = basicTool().availableCamera()
    for cam in cam_lst:
        cap_name.append(cv2.VideoCapture(cam))

    # Append the cap_label object.
    for i in range(len(cam_lst)):
        cap_label_name.append(
            Camera(capture=cap_name[i], label=label_lst[i]))
    # Start all available Camera Thread to show in the UI.
    for cap_label in cap_label_name:
        cap_label.refresh()

    mainWindow.update()
    mainWindow.show()

    sys.exit(app.exec_())
    """
