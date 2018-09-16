# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ui.component import basicLabel, basicComboBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # The main window size.
        MainWindow.resize(1280, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 800))
        MainWindow.setSizeIncrement(QtCore.QSize(10, 10))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setMinimumSize(QtCore.QSize(1024, 720))
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(9, 0, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_2.setHorizontalSpacing(4)
        self.gridLayout_2.setVerticalSpacing(3)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.label_1 = basicLabel(label_name='label_1',
                                  parent=self.centralWidget)
        self.label_2 = basicLabel(label_name='label_2',
                                  parent=self.centralWidget)
        self.label_3 = basicLabel(label_name='label_3',
                                  parent=self.centralWidget)
        self.label_4 = basicLabel(label_name='label_4',
                                  parent=self.centralWidget)
        self.label_5 = basicLabel(label_name='label_5',
                                  parent=self.centralWidget)
        self.label_6 = basicLabel(label_name='label_6',
                                  parent=self.centralWidget)

        # The mainWindow labels, it will show the pics.
        self.gridLayout_2.addWidget(self.label_1, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.label_2, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.label_3, 1, 2, 1, 1)
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.gridLayout_2.addWidget(self.label_5, 3, 1, 1, 1)
        self.gridLayout_2.addWidget(self.label_6, 3, 2, 1, 1)

        # Create the default label name, if you want to change it, please
        # change it in the main process <cap_tool.py>.
        self.origin_label_names = ["None", "cap45a1", "cap60a1", "cap90a1",
                                   "cap45a2", "cap60a2", "cap90a2"]

        self.comboBox_1 = basicComboBox(object_name='comboBox_1',
                                        QWidget_parent=self.centralWidget)
        self.comboBox_2 = basicComboBox(object_name='comboBox_2',
                                        QWidget_parent=self.centralWidget)
        self.comboBox_3 = basicComboBox(object_name='comboBox_3',
                                        QWidget_parent=self.centralWidget)
        self.comboBox_4 = basicComboBox(object_name='comboBox_4',
                                        QWidget_parent=self.centralWidget)
        self.comboBox_5 = basicComboBox(object_name='comboBox_5',
                                        QWidget_parent=self.centralWidget)
        self.comboBox_6 = basicComboBox(object_name='comboBox_6',
                                        QWidget_parent=self.centralWidget)

        self.comboBox_lst = [self.comboBox_1, self.comboBox_2,
                             self.comboBox_3, self.comboBox_4,
                             self.comboBox_5, self.comboBox_6]
        for comboBox in self.comboBox_lst:
            comboBox.addItems(self.origin_label_names)


        self.gridLayout_2.addWidget(self.comboBox_1, 0, 0, 1, 1,
                                    QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addWidget(self.comboBox_2, 0, 1, 1, 1,
                                    QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addWidget(self.comboBox_3, 0, 2, 1, 1,
                                    QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addWidget(self.comboBox_4, 2, 0, 1, 1,
                                    QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addWidget(self.comboBox_5, 2, 1, 1, 1,
                                    QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addWidget(self.comboBox_6, 2, 2, 1, 1,
                                    QtCore.Qt.AlignHCenter)

        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label_width = QtWidgets.QLabel(self.centralWidget)
        self.label_width.setMinimumSize(QtCore.QSize(96, 32))
        self.label_width.setAlignment(QtCore.Qt.AlignCenter)
        self.label_width.setObjectName("label_width")
        self.label_width.setText('Width[宽]:')
        self.lineEdit_width = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_width.setMinimumSize(QtCore.QSize(96, 32))
        self.lineEdit_width.setText('800')
        self.lineEdit_width.setObjectName("lineEdit_width")

        self.horizontalLayout.addWidget(self.label_width)
        self.horizontalLayout.addWidget(self.lineEdit_width)

        self.label_height = QtWidgets.QLabel(self.centralWidget)
        self.label_height.setMinimumSize(QtCore.QSize(96, 32))
        self.label_height.setAlignment(QtCore.Qt.AlignCenter)
        self.label_height.setObjectName("label_height")
        self.label_height.setText('Height[高]:')
        self.lineEdit_height = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_height.setMinimumSize(QtCore.QSize(96, 32))
        self.lineEdit_height.setText('600')
        self.lineEdit_height.setObjectName("lineEdit_height")

        self.horizontalLayout.addWidget(self.label_height)
        self.horizontalLayout.addWidget(self.lineEdit_height)

        # MainWindow button
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralWidget)
        # self.buttonBox.setMinimumSize(640, 32)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)

        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout.setRowStretch(0, 16)
        self.gridLayout.setRowStretch(1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1280, 31))
        self.menuBar.setObjectName("menuBar")
        self.menuCap_Tool = QtWidgets.QMenu(self.menuBar)
        self.menuCap_Tool.setObjectName("menuCap_Tool")
        self.menuInfo = QtWidgets.QMenu(self.menuCap_Tool)
        self.menuInfo.setObjectName("menuInfo")
        MainWindow.setMenuBar(self.menuBar)
        self.action_Author_Mikoy = QtWidgets.QAction(MainWindow)
        self.action_Author_Mikoy.setObjectName("action_Author_Mikoy")
        self.actionEmail_mikoychinese_gmail_com = QtWidgets.QAction(MainWindow)
        self.actionEmail_mikoychinese_gmail_com.setObjectName("actionEmail_mikoychinese_gmail_com")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setCheckable(False)
        self.actionHelp.setObjectName("actionHelp")
        self.menuInfo.addAction(self.action_Author_Mikoy)
        self.menuInfo.addAction(self.actionEmail_mikoychinese_gmail_com)
        self.menuCap_Tool.addAction(self.menuInfo.menuAction())
        self.menuCap_Tool.addAction(self.actionHelp)
        self.menuBar.addAction(self.menuCap_Tool.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Cap_configurate", "Cap_configurate"))

        self.menuCap_Tool.setTitle(_translate("MainWindow", "Cap Tool"))
        self.menuInfo.setTitle(_translate("MainWindow", "Info"))
        self.action_Author_Mikoy.setText(_translate("MainWindow", "__Author__: Mikoy"))
        self.actionEmail_mikoychinese_gmail_com.setText(_translate("MainWindow", "Email: mikoychinese@gmail.com"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
