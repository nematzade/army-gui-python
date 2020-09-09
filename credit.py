# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'credit.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(675, 578)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 671, 261))
        self.groupBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.groupBox.setObjectName("groupBox")
        self.lcdNumber = QtWidgets.QLCDNumber(self.groupBox)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 30, 151, 81))
        self.lcdNumber.setObjectName("lcdNumber")
        self.input_lable = QtWidgets.QLabel(self.groupBox)
        self.input_lable.setGeometry(QtCore.QRect(540, 40, 121, 20))
        self.input_lable.setTextFormat(QtCore.Qt.AutoText)
        self.input_lable.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.input_lable.setObjectName("input_lable")
        self.input = QtWidgets.QLineEdit(self.groupBox)
        self.input.setGeometry(QtCore.QRect(250, 70, 411, 20))
        self.input.setObjectName("input")
        self.credit_lable = QtWidgets.QLabel(self.groupBox)
        self.credit_lable.setGeometry(QtCore.QRect(470, 110, 191, 20))
        self.credit_lable.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.credit_lable.setObjectName("credit_lable")
        self.creditor = QtWidgets.QLineEdit(self.groupBox)
        self.creditor.setGeometry(QtCore.QRect(250, 140, 411, 20))
        self.creditor.setObjectName("creditor")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 180, 671, 341))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 520, 671, 41))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 669, 39))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.btnDelete = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btnDelete.setGeometry(QtCore.QRect(400, 10, 75, 23))
        self.btnDelete.setObjectName("btnDelete")
        self.btnUpdate = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btnUpdate.setGeometry(QtCore.QRect(490, 10, 75, 23))
        self.btnUpdate.setObjectName("btnUpdate")
        self.add = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.add.setGeometry(QtCore.QRect(580, 10, 75, 23))
        self.add.setObjectName("add")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "رکن چهارم مرکز آموزش دژآجا (شعبه خواروبار)"))
        self.groupBox.setTitle(_translate("MainWindow", "میزان ورودی و بستانکاری از آمادگاه"))
        self.input_lable.setText(_translate("MainWindow", "ورودی"))
        self.credit_lable.setText(_translate("MainWindow", "مقدار طلبکاری از آمادگاه"))
        self.btnDelete.setText(_translate("MainWindow", "حذف"))
        self.btnUpdate.setText(_translate("MainWindow", "بروزرسانی"))
        self.add.setText(_translate("MainWindow", "ثبت"))

