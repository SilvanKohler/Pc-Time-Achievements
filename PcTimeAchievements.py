from PyQt5 import QtCore, QtGui, QtWidgets
import csv
import time
import os
import sys

FILE = open("Stunden.dll", "r")
Stunden = float(FILE.read())
FILE.close()

Progress1 = (Stunden*10)*100
if Progress1 > 10000:
    Progress1 = 10000
Progress2 = (Stunden)*100
if Progress2 > 10000:
    Progress2 = 10000
Progress3 = (Stunden/10)*100
if Progress3 > 10000:
    Progress3 = 10000
Progress4 = (Stunden/100)*100
if Progress4 > 10000:
    Progress4 = 10000
Progress5 = (Stunden/1000)*100
if Progress5 > 10000:
    Progress5 = 10000
Progress6 = (Stunden/10000)*100
if Progress6 > 10000:
    Progress6 = 10000
Progress7 = (Stunden*4.1666666666666666666666666666667)*100
if Progress7 > 10000:
    Progress7 = 10000
Progress8 = (Stunden/29.1662)*100
if Progress8 > 10000:
    Progress8 = 10000
Progress9 = (Stunden/116.6648)*100
if Progress9 > 10000:
    Progress9 = 10000
Progress10 = (Stunden/349.9944)*100
if Progress10 > 10000:
    Progress10 = 10000
Progress11 = (Stunden/699.9888)*100
if Progress11 > 10000:
    Progress11 = 10000
Progress12 = (Stunden/1399.9776)*100
if Progress12 > 10000:
    Progress12 = 10000
Progress13 = (Stunden/13999.776 )*100
if Progress13 > 10000:
    Progress13 = 10000
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
            MainWindow.setObjectName("MainWindow")
            MainWindow.resize(1280, 720)
            MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
            MainWindow.setMaximumSize(QtCore.QSize(1280, 720))
            MainWindow.setMouseTracking(True)
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.label = QtWidgets.QLabel(self.centralwidget)
            self.label.setGeometry(QtCore.QRect(0, 20, 311, 71))
            font = QtGui.QFont()
            font.setPointSize(25)
            self.label.setFont(font)
            self.label.setMouseTracking(False)
            self.label.setObjectName("label")
            self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
            self.lcdNumber.setGeometry(QtCore.QRect(280, 35, 331, 41))
            self.lcdNumber.setDigitCount(18)
            self.lcdNumber.setObjectName("lcdNumber")
            self.lcdNumber.display(Stunden)
            self.label_2 = QtWidgets.QLabel(self.centralwidget)
            self.label_2.setGeometry(QtCore.QRect(610, 20, 671, 71))
            font = QtGui.QFont()
            font.setPointSize(25)
            self.label_2.setFont(font)
            self.label_2.setMouseTracking(False)
            self.label_2.setObjectName("label_2")
            self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
            self.progressBar.setGeometry(QtCore.QRect(150, 160, 1091, 23))
            self.progressBar.setMaximum(10000)
            self.progressBar.setProperty("value", Progress1)
            self.progressBar.setObjectName("progressBar")
            self.progressBar_2 = QtWidgets.QProgressBar(self.centralwidget)
            self.progressBar_2.setGeometry(QtCore.QRect(150, 200, 1091, 23))
            self.progressBar_2.setMaximum(10000)
            self.progressBar_2.setProperty("value", Progress2)
            self.progressBar_2.setObjectName("progressBar_2")
            self.progressBar_3 = QtWidgets.QProgressBar(self.centralwidget)
            self.progressBar_3.setGeometry(QtCore.QRect(150, 240, 1091, 23))
            self.progressBar_3.setMaximum(10000)
            self.progressBar_3.setProperty("value", Progress3)
            self.progressBar_3.setTextVisible(True)
            self.progressBar_3.setObjectName("progressBar_3")
            self.label_3 = QtWidgets.QLabel(self.centralwidget)
            self.label_3.setGeometry(QtCore.QRect(10, 160, 61, 16))
            self.label_3.setObjectName("label_3")
            self.label_4 = QtWidgets.QLabel(self.centralwidget)
            self.label_4.setGeometry(QtCore.QRect(10, 200, 71, 20))
            self.label_4.setObjectName("label_4")
            self.label_5 = QtWidgets.QLabel(self.centralwidget)
            self.label_5.setGeometry(QtCore.QRect(10, 240, 71, 20))
            self.label_5.setObjectName("label_5")
            self.label_6 = QtWidgets.QLabel(self.centralwidget)
            self.label_6.setGeometry(QtCore.QRect(10, 280, 81, 20))
            self.label_6.setObjectName("label_6")
            self.label_7 = QtWidgets.QLabel(self.centralwidget)
            self.label_7.setGeometry(QtCore.QRect(10, 320, 81, 20))
            self.label_7.setObjectName("label_7")
            self.label_8 = QtWidgets.QLabel(self.centralwidget)
            self.label_8.setGeometry(QtCore.QRect(10, 360, 91, 20))
            self.label_8.setObjectName("label_8")
            self.label_9 = QtWidgets.QLabel(self.centralwidget)
            self.label_9.setGeometry(QtCore.QRect(10, 400, 71, 20))
            self.label_9.setObjectName("label_9")
            self.label_10 = QtWidgets.QLabel(self.centralwidget)
            self.label_10.setGeometry(QtCore.QRect(10, 440, 71, 20))
            self.label_10.setObjectName("label_10")
            self.label_11 = QtWidgets.QLabel(self.centralwidget)
            self.label_11.setGeometry(QtCore.QRect(10, 480, 71, 20))
            self.label_11.setObjectName("label_11")
            self.label_12 = QtWidgets.QLabel(self.centralwidget)
            self.label_12.setGeometry(QtCore.QRect(10, 520, 71, 20))
            self.label_12.setObjectName("label_12")
            self.label_13 = QtWidgets.QLabel(self.centralwidget)
            self.label_13.setGeometry(QtCore.QRect(10, 560, 71, 20))
            self.label_13.setObjectName("label_13")
            self.label_14 = QtWidgets.QLabel(self.centralwidget)
            self.label_14.setGeometry(QtCore.QRect(10, 600, 71, 20))
            self.label_14.setObjectName("label_14")
            self.label_15 = QtWidgets.QLabel(self.centralwidget)
            self.label_15.setGeometry(QtCore.QRect(10, 640, 71, 20))
            self.label_15.setObjectName("label_15")
            self.progressBar_4 = QtWidgets.QProgressBar(self.centralwidget)
            self.progressBar_4.setGeometry(QtCore.QRect(150, 280, 1091, 23))
            self.progressBar_4.setMaximum(10000)
            self.progressBar_4.setProperty("value", Progress4)
            self.progressBar_4.setTextVisible(True)
            self.progressBar_4.setObjectName("progressBar_4")
            self.progressBar_5 = QtWidgets.QProgressBar(self.centralwidget)
            self.progressBar_5.setGeometry(QtCore.QRect(150, 320, 1091, 23))
            self.progressBar_5.setMaximum(10000)
            self.progressBar_5.setProperty("value", Progress5)
            self.progressBar_5.setTextVisible(True)
            self.progressBar_5.setObjectName("progressBar_5")
            self.progressBar_6 = QtWidgets.QProgressBar(self.centralwidget)
            self.progressBar_6.setGeometry(QtCore.QRect(150, 360, 1091, 23))
            self.progressBar_6.setMaximum(10000)
            self.progressBar_6.setProperty("value", Progress6)
            self.progressBar_6.setTextVisible(True)
            self.progressBar_6.setObjectName("progressBar_6")
            self.progressBar_7 = QtWidgets.QProgressBar(self.centralwidget)
            self.progressBar_7.setGeometry(QtCore.QRect(150, 400, 1091, 23))
            self.progressBar_7.setMaximum(10000)
            self.progressBar_7.setProperty("value", Progress7)
            self.progressBar_7.setTextVisible(True)
            self.progressBar_7.setObjectName("progressBar_7")
            self.progressBar_8 = QtWidgets.QProgressBar(self.centralwidget)
            self.progressBar_8.setGeometry(QtCore.QRect(150, 440, 1091, 23))
            self.progressBar_8.setMaximum(10000)
            self.progressBar_8.setProperty("value", Progress8)
            self.progressBar_8.setTextVisible(True)
            self.progressBar_8.setObjectName("progressBar_8")
            self.progressBar_9 = QtWidgets.QProgressBar(self.centralwidget)
            self.progressBar_9.setGeometry(QtCore.QRect(150, 480, 1091, 23))
            self.progressBar_9.setMaximum(10000)
            self.progressBar_9.setProperty("value", Progress9)
            self.progressBar_9.setTextVisible(True)
            self.progressBar_9.setObjectName("progressBar_9")
            self.progressBar_10 = QtWidgets.QProgressBar(self.centralwidget)
            self.progressBar_10.setGeometry(QtCore.QRect(150, 520, 1091, 23))
            self.progressBar_10.setMaximum(10000)
            self.progressBar_10.setProperty("value", Progress10)
            self.progressBar_10.setTextVisible(True)
            self.progressBar_10.setObjectName("progressBar_10")
            self.progressBar_11 = QtWidgets.QProgressBar(self.centralwidget)
            self.progressBar_11.setGeometry(QtCore.QRect(150, 560, 1091, 23))
            self.progressBar_11.setMaximum(10000)
            self.progressBar_11.setProperty("value", Progress11)
            self.progressBar_11.setTextVisible(True)
            self.progressBar_11.setObjectName("progressBar_11")
            self.progressBar_12 = QtWidgets.QProgressBar(self.centralwidget)
            self.progressBar_12.setGeometry(QtCore.QRect(150, 600, 1091, 23))
            self.progressBar_12.setMaximum(10000)
            self.progressBar_12.setProperty("value", Progress12)
            self.progressBar_12.setTextVisible(True)
            self.progressBar_12.setObjectName("progressBar_12")
            self.progressBar_13 = QtWidgets.QProgressBar(self.centralwidget)
            self.progressBar_13.setGeometry(QtCore.QRect(150, 640, 1091, 23))
            self.progressBar_13.setMaximum(10000)
            self.progressBar_13.setProperty("value", Progress13)
            self.progressBar_13.setTextVisible(True)
            self.progressBar_13.setObjectName("progressBar_13")
            self.line = QtWidgets.QFrame(self.centralwidget)
            self.line.setGeometry(QtCore.QRect(10, 620, 1261, 20))
            self.line.setFrameShape(QtWidgets.QFrame.HLine)
            self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line.setObjectName("line")
            self.line_2 = QtWidgets.QFrame(self.centralwidget)
            self.line_2.setGeometry(QtCore.QRect(10, 580, 1261, 20))
            self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
            self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_2.setObjectName("line_2")
            self.line_3 = QtWidgets.QFrame(self.centralwidget)
            self.line_3.setGeometry(QtCore.QRect(10, 540, 1261, 20))
            self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
            self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_3.setObjectName("line_3")
            self.line_4 = QtWidgets.QFrame(self.centralwidget)
            self.line_4.setGeometry(QtCore.QRect(10, 500, 1261, 20))
            self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
            self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_4.setObjectName("line_4")
            self.line_5 = QtWidgets.QFrame(self.centralwidget)
            self.line_5.setGeometry(QtCore.QRect(10, 460, 1261, 20))
            self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
            self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_5.setObjectName("line_5")
            self.line_6 = QtWidgets.QFrame(self.centralwidget)
            self.line_6.setGeometry(QtCore.QRect(10, 420, 1261, 20))
            self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
            self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_6.setObjectName("line_6")
            self.line_7 = QtWidgets.QFrame(self.centralwidget)
            self.line_7.setGeometry(QtCore.QRect(10, 380, 1261, 20))
            self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
            self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_7.setObjectName("line_7")
            self.line_8 = QtWidgets.QFrame(self.centralwidget)
            self.line_8.setGeometry(QtCore.QRect(10, 340, 1261, 20))
            self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
            self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_8.setObjectName("line_8")
            self.line_9 = QtWidgets.QFrame(self.centralwidget)
            self.line_9.setGeometry(QtCore.QRect(10, 300, 1261, 20))
            self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
            self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_9.setObjectName("line_9")
            self.line_10 = QtWidgets.QFrame(self.centralwidget)
            self.line_10.setGeometry(QtCore.QRect(10, 260, 1261, 20))
            self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
            self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_10.setObjectName("line_10")
            self.line_11 = QtWidgets.QFrame(self.centralwidget)
            self.line_11.setGeometry(QtCore.QRect(10, 220, 1261, 20))
            self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
            self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_11.setObjectName("line_11")
            self.line_12 = QtWidgets.QFrame(self.centralwidget)
            self.line_12.setGeometry(QtCore.QRect(10, 180, 1261, 20))
            self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
            self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_12.setObjectName("line_12")
            MainWindow.setCentralWidget(self.centralwidget)
            self.statusbar = QtWidgets.QStatusBar(MainWindow)
            self.statusbar.setObjectName("statusbar")
            MainWindow.setStatusBar(self.statusbar)

            self.retranslateUi(MainWindow)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pc Time Achievements"))
        self.label.setText(_translate("MainWindow", "Deine Nutzungszeit"))
        if (Stunden < 10):
            coolerspruch = "Neuling!"
        elif (10 <= Stunden < 20):
            coolerspruch = "Anfänger/in!"
        elif (20 <= Stunden < 40):
            coolerspruch = "fortgeschrittene/r Anfänger/in!"
        elif (40 <= Stunden < 70):
            coolerspruch = "Kompetente/r!"
        elif (70 <= Stunden < 400):
            coolerspruch = "Gewandte/r!"
        elif (400 <= Stunden < 800):
            coolerspruch = "Experte/Expertin!"
        elif (800 <= Stunden < 2000):
            coolerspruch = "Level 100 Mafia Boss!"
        elif (2000 <= Stunden < 8000):
            coolerspruch = "Hobbylose/r Pc-Spasst/in!"
        elif (8000 <= Stunden < 20000):
            coolerspruch = "Stromrechnunghinterzieher/in!"
        elif (Stunden >= 20000):
            coolerspruch = "Suchti!"
        else:
            coolerspruch = ""
        self.label_2.setText(_translate("MainWindow", "Stunden, Du " + coolerspruch))
        self.label_3.setText(_translate("MainWindow", "10 Stunden"))
        self.label_4.setText(_translate("MainWindow", "100 Stunden"))
        self.label_5.setText(_translate("MainWindow", "1000 Stunden"))
        self.label_6.setText(_translate("MainWindow", "10000 Stunden"))
        self.label_7.setText(_translate("MainWindow", "100000 Stunden"))
        self.label_8.setText(_translate("MainWindow", "1000000 Stunden"))
        self.label_9.setText(_translate("MainWindow", "1 Tag"))
        self.label_10.setText(_translate("MainWindow", "1 Woche"))
        self.label_11.setText(_translate("MainWindow", "1 Monat"))
        self.label_12.setText(_translate("MainWindow", "3 Monate"))
        self.label_13.setText(_translate("MainWindow", "6 Monate"))
        self.label_14.setText(_translate("MainWindow", "1 Jahr"))
        self.label_15.setText(_translate("MainWindow", "10 Jahre"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())