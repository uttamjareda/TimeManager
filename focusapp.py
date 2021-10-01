# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'focusapp.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence, QPalette, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPalette
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import time

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(452, 361)

        self.hour=0
        self.starttime=0
        self.endtime=0
        self.date=datetime.date(datetime.now())
        self.timeworked=0
        self.totaltime=0
        self.stopflag=0
        self.count=0
        
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 10, 341, 24))
        self.label.setObjectName("label")
        self.start = QtWidgets.QPushButton(Form)
        self.start.setGeometry(QtCore.QRect(10, 90, 71, 31))
        self.start.setObjectName("start")
        self.stop = QtWidgets.QPushButton(Form)
        self.stop.setGeometry(QtCore.QRect(230, 90, 91, 31))
        self.stop.setObjectName("stop")
        self.reset = QtWidgets.QPushButton(Form)
        self.reset.setGeometry(QtCore.QRect(330, 90, 101, 31))
        self.reset.setObjectName("reset")
        self.total = QtWidgets.QPushButton(Form)
        self.total.setGeometry(QtCore.QRect(330, 50, 101, 31))
        self.total.setObjectName("total")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(10, 180, 441, 171))
        self.textEdit.setObjectName("textEdit")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(100, 90, 113, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(100, 130, 241, 41))
        self.textEdit_2.setObjectName("textEdit_2")

        self.start.clicked.connect(self.startf)
        self.reset.clicked.connect(self.resetf)
        self.stop.clicked.connect(self.stopf)
        self.total.clicked.connect(self.totaltimef)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def startf(self):

        self.work=int(self.lineEdit.text())
        
        self.starttime=datetime.time(datetime.now())
        self.date=datetime.date(datetime.now())
        tim=0
        minutes=0
        hours=0
        self.stopflag=0
        while(self.stopflag==0):
            
            tim+=1
            if(tim==60):
                minutes+=1
            if(minutes==60):
                hours+=1
            minutes=minutes%60
            tim=tim%60
            a= str(hours)+":"+str(minutes)+":"+str(tim)
            self.textEdit_2.setText(a)
            self.count+=1
            self.totaltime+=1
            QtWidgets.QApplication.processEvents()
            time.sleep(1)
            
            
        return

    def stopf(self):
        self.stopflag=1
        print(self.count)
        
        minutes=int(self.count/60)
        print(minutes)
        hours=int(minutes/60)
        minutes=minutes%60
        self.endtime=datetime.time(datetime.now())
        sttime=str(self.starttime)
        endtim=str(self.endtime)
        st=sttime[0:5]
        et=endtim[0:5]
        
        
        self.textEdit.append(str(self.date)+"   "+str(self.work)+"   "+ st+"    "+et+"   "+str(hours)+":"+str(minutes))
        self.count=0
        
        return

    def resetf(self):
        self.textEdit.clear()
        self.textEdit_2.clear()
        self.stopflag=0
        self.totaltime=0
        return

    def totaltimef(self):
        
        minutes=self.totaltime/60
        minutes=int(minutes)
        hours=int(minutes/60)
        a=str(hours)+":"+str(minutes)
        self.textEdit_2.setText(a)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; color:#ce5c00;\">I will become the best versin of myself</span></p></body></html>"))
        self.start.setText(_translate("Form", "Start"))
        self.stop.setText(_translate("Form", "Stop"))
        self.reset.setText(_translate("Form", "Reset"))
        self.total.setText(_translate("Form", "CountTotal"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    palette = QtGui.QPalette()
    palette.setColor(QPalette.Window, QColor(0,0,0))
    #palette.setColor(QPalette.Background,QColor(0,0,0))
    palette.setColor(QPalette.WindowText, QColor(0,255,255))
    
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, QColor(255,128,0))
    palette.setColor(QPalette.Button, QColor(0,0,0))
    palette.setColor(QPalette.ButtonText,QColor(0,255,255) )
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
