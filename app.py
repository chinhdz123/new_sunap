# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(788, 563)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-4, -8, 791, 541))
        self.label.setStyleSheet("border-image: url(:/newPrefix/1614776.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 531, 341))
        self.label_2.setStyleSheet("border-image: url(:/newPrefix/9.jpg);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.bt_camera = QtWidgets.QPushButton(self.centralwidget)
        self.bt_camera.setGeometry(QtCore.QRect(220, 380, 111, 21))
        self.bt_camera.setStyleSheet("QPushButton#bt_camera{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#bt_camera:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2,65,118,100);\n"
"background-position:calc(100%-10px)center;\n"
"}\n"
"QPushButton#bt_camera:hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}\n"
"")
        self.bt_camera.setObjectName("bt_camera")
        self.bt_start = QtWidgets.QPushButton(self.centralwidget)
        self.bt_start.setGeometry(QtCore.QRect(50, 440, 131, 31))
        self.bt_start.setStyleSheet("QPushButton#bt_start{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#bt_start:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2,65,118,100);\n"
"background-position:calc(100%-10px)center;\n"
"}\n"
"QPushButton#bt_start:hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}\n"
"")
        self.bt_start.setObjectName("bt_start")
        self.bt_stop = QtWidgets.QPushButton(self.centralwidget)
        self.bt_stop.setGeometry(QtCore.QRect(380, 440, 141, 31))
        self.bt_stop.setStyleSheet("QPushButton#bt_stop{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#bt_stop:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2,65,118,100);\n"
"background-position:calc(100%-10px)center;\n"
"}\n"
"QPushButton#bt_stop:hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}\n"
"")
        self.bt_stop.setObjectName("bt_stop")
        self.label_date = QtWidgets.QLabel(self.centralwidget)
        self.label_date.setGeometry(QtCore.QRect(580, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_date.setFont(font)
        self.label_date.setStyleSheet("color: rgb(255, 255, 0);")
        self.label_date.setObjectName("label_date")
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        self.label_time.setGeometry(QtCore.QRect(580, 70, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_time.setFont(font)
        self.label_time.setStyleSheet("color: rgb(255, 255, 0);")
        self.label_time.setObjectName("label_time")
        self.label_date1 = QtWidgets.QLabel(self.centralwidget)
        self.label_date1.setGeometry(QtCore.QRect(650, 30, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_date1.setFont(font)
        self.label_date1.setStyleSheet("color: rgb(255, 255, 0);")
        self.label_date1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_date1.setObjectName("label_date1")
        self.label_time_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_time_1.setGeometry(QtCore.QRect(650, 70, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_time_1.setFont(font)
        self.label_time_1.setStyleSheet("color: rgb(255, 255, 0);")
        self.label_time_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time_1.setObjectName("label_time_1")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(580, 150, 191, 221))
        self.groupBox.setStyleSheet("color: rgb(255, 255, 0);\n"
"background-color:rgba(0,0,0,75);")
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(90, 50, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(90, 150, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 150, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.bt_grid = QtWidgets.QPushButton(self.centralwidget)
        self.bt_grid.setGeometry(QtCore.QRect(210, 440, 131, 31))
        self.bt_grid.setStyleSheet("QPushButton#bt_grid{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#bt_grid:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2,65,118,100);\n"
"background-position:calc(100%-10px)center;\n"
"}\n"
"QPushButton#bt_grid:hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}\n"
"")
        self.bt_grid.setObjectName("bt_grid")
        self.bt_mic = QtWidgets.QPushButton(self.centralwidget)
        self.bt_mic.setGeometry(QtCore.QRect(620, 390, 121, 31))
        self.bt_mic.setStyleSheet("QPushButton#bt_mic{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#bt_mic:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2,65,118,100);\n"
"background-position:calc(100%-10px)center;\n"
"}\n"
"QPushButton#bt_mic:hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}\n"
"")
        self.bt_mic.setObjectName("bt_mic")
        self.bt_data = QtWidgets.QPushButton(self.centralwidget)
        self.bt_data.setGeometry(QtCore.QRect(620, 450, 121, 31))
        self.bt_data.setStyleSheet("QPushButton#bt_data{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#bt_data:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2,65,118,100);\n"
"background-position:calc(100%-10px)center;\n"
"}\n"
"QPushButton#bt_data:hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}\n"
"")
        self.bt_data.setObjectName("bt_data")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 788, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_camera.setText(_translate("MainWindow", "Capture"))
        self.bt_start.setText(_translate("MainWindow", "Start"))
        self.bt_stop.setText(_translate("MainWindow", "Stop"))
        self.label_date.setText(_translate("MainWindow", "Date:"))
        self.label_time.setText(_translate("MainWindow", "Time:"))
        self.label_date1.setText(_translate("MainWindow", "-"))
        self.label_time_1.setText(_translate("MainWindow", "-"))
        self.groupBox.setTitle(_translate("MainWindow", "Infor"))
        self.label_3.setText(_translate("MainWindow", "Name:"))
        self.label_4.setText(_translate("MainWindow", "-"))
        self.label_5.setText(_translate("MainWindow", "-"))
        self.label_6.setText(_translate("MainWindow", "Number:"))
        self.bt_grid.setText(_translate("MainWindow", "Grid"))
        self.bt_mic.setText(_translate("MainWindow", "Mic"))
        self.bt_data.setText(_translate("MainWindow", "Data"))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
