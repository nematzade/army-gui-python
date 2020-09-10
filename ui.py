# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\uipython\pyqtex\pyqtdb\crud.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(673, 578)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 671, 261))
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        # LCD number
        self.lcdNumber = QtWidgets.QLCDNumber(self.groupBox)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 30, 151, 81))
        self.lcdNumber.setObjectName("lcdNumber")

        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(540, 40, 121, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(250, 70, 411, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(470, 110, 191, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 140, 411, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(400, 180, 259, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(250, 210, 411, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.tableWidget = QtWidgets.QTableView(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 260, 671, 261))
        self.tableWidget.setObjectName("tableWidget")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 520, 671, 41))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 669, 39))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        # Buttons
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 10, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 10, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_4.setGeometry(QtCore.QRect(310, 10, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_5.setGeometry(QtCore.QRect(410, 10, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")

        self.browse_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.browse_btn.setGeometry(QtCore.QRect(510, 10, 75, 23))
        self.browse_btn.setObjectName("browse_btn")

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
        self.groupBox.setTitle(_translate("MainWindow", "آمار روزانه یخچال"))
        self.label.setText(_translate("MainWindow", "نام کالا"))
        self.label_2.setText(_translate("MainWindow", "صرفه جویی"))
        self.label_3.setText(_translate("MainWindow", "مقدار/تعداد"))

        self.pushButton.setText(_translate("MainWindow", "ثبت"))
        self.pushButton_2.setText(_translate("MainWindow", "بروزرسانی"))
        self.pushButton_3.setText(_translate("MainWindow", "حذف"))
        self.pushButton_4.setText(_translate("MainWindow", "عودت"))
        self.pushButton_5.setText(_translate("MainWindow", "آمادگاه"))
        self.browse_btn.setText(_translate("MainWindow", "فایل"))

