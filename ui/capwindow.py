# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from ui.component import basicLabel
import sys


class Cap_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
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
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(11, 11, 11, 9)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.cap_next_Button = QtWidgets.QPushButton(self.centralWidget)
        self.cap_next_Button.setObjectName("cap_next_Button")
        self.gridLayout_3.addWidget(self.cap_next_Button, 3, 1, 1, 1)
        self.label_date = QtWidgets.QLabel(self.centralWidget)
        self.label_date.setMinimumSize(QtCore.QSize(113, 32))
        self.label_date.setAlignment(QtCore.Qt.AlignCenter)
        self.label_date.setObjectName("label_date")
        self.gridLayout_3.addWidget(self.label_date, 0, 2, 1, 1)
        self.label_direction = QtWidgets.QLabel(self.centralWidget)
        self.label_direction.setMinimumSize(QtCore.QSize(113, 32))
        self.label_direction.setAlignment(QtCore.Qt.AlignCenter)
        self.label_direction.setObjectName("label_direction")
        self.gridLayout_3.addWidget(self.label_direction, 1, 2, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(198, 32))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setText('1')
        self.gridLayout_3.addWidget(self.lineEdit_4, 1, 3, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(199, 32))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setText('0')
        self.gridLayout_3.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(199, 32))
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_3.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(198, 32))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setText('201809')
        self.gridLayout_3.addWidget(self.lineEdit_3, 0, 3, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(318, 32))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_3.addWidget(self.lineEdit_5, 2, 1, 1, 2)
        self.label_char = QtWidgets.QLabel(self.centralWidget)
        self.label_char.setMinimumSize(QtCore.QSize(96, 32))
        self.label_char.setAlignment(QtCore.Qt.AlignCenter)
        self.label_char.setObjectName("label_char")
        self.gridLayout_3.addWidget(self.label_char, 1, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralWidget)
        self.label_11.setMinimumSize(QtCore.QSize(96, 32))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 2, 0, 1, 1)
        self.cap_ok_Button = QtWidgets.QPushButton(self.centralWidget)
        self.cap_ok_Button.setObjectName("cap_ok_Button")
        self.gridLayout_3.addWidget(self.cap_ok_Button, 3, 2, 1, 2)
        self.toolButton = QtWidgets.QToolButton(self.centralWidget)
        self.toolButton.setIconSize(QtCore.QSize(63, 21))
        self.toolButton.setArrowType(QtCore.Qt.DownArrow)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout_3.addWidget(self.toolButton, 2, 3, 1, 1)
        self.label_cvid = QtWidgets.QLabel(self.centralWidget)
        self.label_cvid.setMinimumSize(QtCore.QSize(96, 32))
        self.label_cvid.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cvid.setObjectName("label_cvid")
        self.gridLayout_3.addWidget(self.label_cvid, 0, 0, 1, 1)
        self.cap_quit_Button = QtWidgets.QPushButton(self.centralWidget)
        self.cap_quit_Button.setMinimumSize(QtCore.QSize(96, 32))
        self.cap_quit_Button.setObjectName("cap_quit_Button")
        self.gridLayout_3.addWidget(self.cap_quit_Button, 3, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser.setMinimumSize(QtCore.QSize(630, 148))
        self.textBrowser.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textBrowser.setLineWidth(1)
        self.textBrowser.setMidLineWidth(0)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_3.addWidget(self.textBrowser, 0, 4, 4, 1)
        self.gridLayout_3.setColumnStretch(0, 96)
        self.gridLayout_3.setColumnStretch(1, 199)
        self.gridLayout_3.setColumnStretch(2, 96)
        self.gridLayout_3.setColumnStretch(3, 199)
        self.gridLayout_3.setColumnStretch(4, 630)
        self.gridLayout.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_2.setHorizontalSpacing(4)
        self.gridLayout_2.setVerticalSpacing(3)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.label_1 = basicLabel(label_name='label_1',
                                  parent=self.centralWidget, width=414,
                                  height=259)
        self.label_2 = basicLabel(label_name='label_2',
                                  parent=self.centralWidget, width=414,
                                  height=259)
        self.label_3 = basicLabel(label_name='label_3',
                                  parent=self.centralWidget, width=414,
                                  height=259)

        self.label_4 = basicLabel(label_name='label_4',
                                  parent=self.centralWidget, width=414,
                                  height=260)
        self.label_5 = basicLabel(label_name='label_5',
                                  parent=self.centralWidget, width=414,
                                  height=260)
        self.label_6 = basicLabel(label_name='label_6',
                                  parent=self.centralWidget, width=414,
                                  height=260)

        self.gridLayout_2.addWidget(self.label_1, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.label_2, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.label_3, 1, 2, 1, 1)
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.label_5, 2, 1, 1, 1)
        self.gridLayout_2.addWidget(self.label_6, 2, 2, 1, 1)


        self.label_10 = QtWidgets.QLabel(self.centralWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1280, 31))
        self.menuBar.setObjectName("menuBar")
        self.menuCap_Tool = QtWidgets.QMenu(self.menuBar)
        self.menuCap_Tool.setObjectName("menuCap_Tool")
        self.menuInfo = QtWidgets.QMenu(self.menuCap_Tool)
        self.menuInfo.setObjectName("menuInfo")
        MainWindow.setMenuBar(self.menuBar)
        self.action_Author = QtWidgets.QAction(MainWindow)
        self.action_Author.setObjectName("action_Author")
        self.actionEmail = QtWidgets.QAction(MainWindow)
        self.actionEmail.setObjectName("actionEmail")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setCheckable(False)
        self.actionHelp.setObjectName("actionHelp")
        self.menuInfo.addAction(self.action_Author)
        self.menuInfo.addAction(self.actionEmail)
        self.menuCap_Tool.addAction(self.menuInfo.menuAction())
        self.menuCap_Tool.addAction(self.actionHelp)
        self.menuBar.addAction(self.menuCap_Tool.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit, self.lineEdit_3)
        MainWindow.setTabOrder(self.lineEdit_3, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.lineEdit_4)
        MainWindow.setTabOrder(self.lineEdit_4, self.lineEdit_5)
        MainWindow.setTabOrder(self.lineEdit_5, self.toolButton)
        MainWindow.setTabOrder(self.toolButton, self.cap_ok_Button)
        MainWindow.setTabOrder(self.cap_ok_Button, self.cap_quit_Button)
        MainWindow.setTabOrder(self.cap_quit_Button, self.cap_next_Button)
        MainWindow.setTabOrder(self.cap_next_Button, self.textBrowser)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cap_next_Button.setText(_translate("MainWindow", "Next[转变方向]"))
        self.label_date.setText(_translate("MainWindow", "Date[生产日期]"))
        self.label_direction.setText(_translate("MainWindow", "Direction[方向]"))
        self.label_char.setText(_translate("MainWindow", "Char[形态]"))
        self.label_11.setText(_translate("MainWindow", "存储目录"))
        self.cap_ok_Button.setText(_translate("MainWindow", "Capture[开始拍照]"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.label_cvid.setText(_translate("MainWindow", "Cvid[商品名]"))
        self.cap_quit_Button.setText(_translate("MainWindow", "设置速度"))

        self.label_1.setText(_translate("MainWindow", "cap1"))
        self.label_2.setText(_translate("MainWindow", "cap2"))
        self.label_3.setText(_translate("MainWindow", "cap3"))
        self.label_4.setText(_translate("MainWindow", "Cap4"))
        self.label_5.setText(_translate("MainWindow", "cap5"))
        self.label_6.setText(_translate("MainWindow", "cap6"))
        self.label_10.setText(_translate("MainWindow", "Cap_Tool : v1.0"))

        self.menuCap_Tool.setTitle(_translate("MainWindow", "Cap Tool"))
        self.menuInfo.setTitle(_translate("MainWindow", "Info"))
        self.action_Author.setText(_translate("MainWindow", "__Author__: Mikoy"))
        self.actionEmail.setText(_translate("MainWindow", "Email: mikoychinese@gmail.com"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Cap_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())