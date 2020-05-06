# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from functions import *
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Root(object):
    def setupUi(self, Root):
        Root.setObjectName("Root")
        Root.resize(640, 193)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Root.sizePolicy().hasHeightForWidth())
        Root.setSizePolicy(sizePolicy)
        Root.setMaximumSize(QtCore.QSize(640, 193))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        Root.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        Root.setWindowIcon(icon)
        Root.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.0451977 rgba(170, 85, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(Root)
        self.centralwidget.setObjectName("centralwidget")
        self.Entry = QtWidgets.QLineEdit(self.centralwidget)
        self.Entry.setGeometry(QtCore.QRect(40, 50, 561, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Entry.sizePolicy().hasHeightForWidth())
        self.Entry.setSizePolicy(sizePolicy)
        self.Entry.setStyleSheet("border-radius: 8px;\n"
"background: rgb(255, 255, 255);\n"
"")
        self.Entry.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Entry.setText("")
        self.Entry.setCursorPosition(0)
        self.Entry.setObjectName("Entry")
        self.Browse_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Browse_btn.setGeometry(QtCore.QRect(410, 100, 91, 31))
        self.Browse_btn.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 8px;\n"
"border-color: rgb(0, 0, 127);\n"
"font: 75 10pt \"MS Serif\";\n"
"color: white;\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(3, 153, 216, 255), stop:0.875 rgba(8, 14, 203, 255));\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"color:rgb(0, 0, 127);\n"
"}")
        self.Browse_btn.setObjectName("Browse_btn")
        self.Organize_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Organize_btn.setGeometry(QtCore.QRect(510, 100, 91, 31))
        self.Organize_btn.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 8px;\n"
"border-color: rgb(0, 0, 127);\n"
"font: 75 10pt \"MS Serif\";\n"
"color: white;\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(3, 153, 216, 255), stop:0.875 rgba(8, 14, 203, 255));\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"color:rgb(0, 0, 127);\n"
"}")
        self.Organize_btn.setObjectName("Organize_btn")
        self.Reset_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Reset_btn.setGeometry(QtCore.QRect(40, 100, 91, 31))
        self.Reset_btn.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 8px;\n"
"border-color: rgb(0, 0, 127);\n"
"font: 75 10pt \"MS Serif\";\n"
"color: white;\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(3, 153, 216, 255), stop:0.875 rgba(8, 14, 203, 255));\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"color:rgb(0, 0, 127);\n"
"}")
        self.Reset_btn.setObjectName("Reset_btn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 170, 71, 16))
        self.label.setStyleSheet("background: transparent;\n"
"color: rgb(0, 0, 127);\n"
"font: 75 10pt \"MS Sherif\";")
        self.label.setObjectName("label")
        Root.setCentralWidget(self.centralwidget)

        self.retranslateUi(Root)
        self.Reset_btn.clicked.connect(self.Entry.clear)
        QtCore.QMetaObject.connectSlotsByName(Root)

        self.Organize_btn.clicked.connect(self.organize)
        self.Browse_btn.clicked.connect(self.browse)

    def retranslateUi(self, Root):
        _translate = QtCore.QCoreApplication.translate
        Root.setWindowTitle(_translate("Root", "File Management System"))
        self.Entry.setPlaceholderText(_translate("Root", "     Enter Folder Path"))
        self.Browse_btn.setText(_translate("Root", "Browse"))
        self.Organize_btn.setText(_translate("Root", "Organize"))
        self.Reset_btn.setText(_translate("Root", "Reset"))
        self.label.setText(_translate("Root", "v 5.0"))


    def browse(self):
        path=QtWidgets.QFileDialog.getExistingDirectory()
        self.Entry.setText(path)
    

    def organize(self):
        
        path=self.Entry.text()
        Organize(path)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Root = QtWidgets.QMainWindow()
    ui = Ui_Root()
    ui.setupUi(Root)
    Root.show()
    sys.exit(app.exec_())

