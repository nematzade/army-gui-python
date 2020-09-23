from fbs_runtime.application_context.PyQt5 import ApplicationContext
import sys
from ui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtSql, QtWidgets
import pandas as pd
import sqlite3
from credit import *
from unidecode import unidecode
from PyQt5.QtCore import QDir
from PyQt5 import *
import xlsxwriter
from csv import writer

# https://www.learnpyqt.com/courses/packaging-and-distribution/packaging-pyqt5-pyside2-applications-windows-pyinstaller/
# https://github.com/pyqt/examples
class Controller:
    def __init__(self):
        pass

    def Show_FirstWindow(self):
        self.FirstWindow = QtWidgets.QMainWindow()
        self.FirstWindow.setWindowIcon(QtGui.QIcon('aja.png'))
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.FirstWindow)
        
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('fieldlist.db')
        self.model = QtSql.QSqlTableModel()
        self.model.setTable('supply')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.select()

        self.model.setHeaderData(1, QtCore.Qt.Vertical,"نوع کالا")
        self.model.setHeaderData(2, QtCore.Qt.Vertical,"صرفه جویی")
        self.model.setHeaderData(3, QtCore.Qt.Vertical,"مقدار/تعداد")
        self.ui.tableWidget.setModel(self.model)
        self.ui.pushButton.clicked.connect(self.addToDb)
        self.ui.pushButton_2.clicked.connect(self.updaterow)
        self.ui.pushButton_3.clicked.connect(self.delrow)
        self.ui.pushButton_4.clicked.connect(self.coming_back)
        self.ui.pushButton_5.clicked.connect(self.Show_SecondWindow)
        self.ui.browse_btn.clicked.connect(self.browseSlot)
        self.i = self.model.rowCount()
        self.ui.lcdNumber.display(self.i)
        print(self.ui.tableWidget.currentIndex().row())
        self.FirstWindow.show()

    def Show_SecondWindow(self):
        self.SecondWindow = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.SecondWindow)
        # todo : create table for second window in database And delete creditor And create method for computing.
        self.ui.btnDelete.clicked.connect(self.print_message) 
        # todo : select from db.
        self.ui.lcdNumber.display(1555)
        self.SecondWindow.show()   

    def print_message(self):
        print("hello")

    # browse file 
    def browseSlot(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file, _ = QtWidgets.QFileDialog.getOpenFileName(
                        None,
                        "QFileDialog.getOpenFileName()",
                        "",
                        "Excel Files (*.xlsx);;Python Files (*.py)",
                        options=options)
        if file:
            self.daily_stats(file)
            # self.diet_compare(file)

    def diet_compare(self,file):
        pass

    # convert persian/Arabic digit to english digit.
    def convert_num(self,num):
        cnum = unidecode(str(num))
        return cnum

    def coming_back(self):
        self.model = QtSql.QSqlTableModel()
        self.model.setTable('supply')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        try:
            sqliteCon = sqlite3.connect('fieldlist.db')
            cursor = sqliteCon.cursor()
            print('connected to sqlite')
            sql_read_query = "SELECT * from supply"
            cursor.execute(sql_read_query)
            result = cursor.fetchall()
            for row in result:
                kg = int(row[3]) + int(row[2])
                sql_query = """UPDATE supply SET kg = ? , sj = 0 WHERE id=?"""
                cursor.execute(sql_query,(kg,row[0]))
            sqliteCon.commit()
            print("Record Updated successfully ")
            cursor.close()
            self.model.select()
            self.ui.tableWidget.setModel(self.model)
        except sqlite3.Error as error:
            print("Failed to update multiple records of sqlite table", error)
        finally:
            if (sqliteCon):
                sqliteCon.close()
                print("The SQLite connection is closed")


    def daily_stats(self,file):
        df = pd.read_excel(file)
        print('---------------------------------')
        sqliteCon = sqlite3.connect('fieldlist.db')
        cursor = sqliteCon.cursor()
        print('connected to sqlite')
        sql_read_query = "SELECT * from supply"
        cursor.execute(sql_read_query)
        result = cursor.fetchall()
        total_stats = self.ui.lineEdit.text()
        meal = self.ui.lineEdit_2.text()
        if total_stats == "" or meal == "":
            self.show_dialog("اطلاعاتی وارد نشده! دوباره تلاس کنید.")
        else:
            total_stats = int(total_stats)
            meal = int(meal)
        for i in df.index:
            for row in result:                
                try:
                    name_in_db   = row[1]
                    name_in_file = df['name'][i]
                    basis = df['basis'][i]
                    # convert persian/Arabic digit to english number.
                    basis = self.convert_num(basis)
                    if(name_in_db == name_in_file):
                        kgr = int(basis) * meal
                        kgk = int(basis) * total_stats
                        kg  = row[3]
                        frugality = 0
                        frugality = kgk - kgr
                        kg  = int(kg) - kgk
                        sql_query = """UPDATE supply SET kg = ? , sj = ? WHERE id=?"""
                        sj  = row[2]
                        sj  = float(sj) + float(frugality)
                        uid = int(row[0])
                        cursor.execute(sql_query,(kg,int(sj),uid))
                        print("Record Updated successfully ")
                except Exception:
                    self.show_dialog("فایل اکسل را مجددا بررسی کنید!")
                    return
        sqliteCon.commit()
        cursor.close()
        self.model = QtSql.QSqlTableModel()
        self.model.setTable('supply')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.select()
        self.ui.tableWidget.setModel(self.model)        
        print('---------------------------------')

    # clear lineEdit after update and insert.        
    def lineEdit_clear(self):
        self.ui.lineEdit.setText("")
        self.ui.lineEdit_2.setText("")    
        self.ui.lineEdit_3.setText("")

    def show_dialog(self,infoText,y_n = '',connect = ''):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setInformativeText(infoText)
        msg.setWindowTitle("خطا!")
        if y_n != '':
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        else:
            msg.setStandardButtons(QMessageBox.Ok)

        if connect != '':
            msg.buttonClicked.connect(connect)
        retval = msg.exec_()

    def addToDb(self):
        sj = self.ui.lineEdit_2.text()
        kg = self.ui.lineEdit_3.text()
        if sj == '':
            self.show_dialog("هیچکدام از فیلد ها نباید خالی باشد.")
            return
        elif kg == '':
            self.show_dialog("هیچکدام از فیلد ها نباید خالی باشد.")
            return
        elif self.ui.lineEdit.text() == '':
            self.show_dialog("هیچکدام از فیلد ها نباید خالی باشد.")
            return
        
        try:
            # convert persian/Arabic digit to english number.
            le_2 = self.convert_num(sj)
            le_3 = self.convert_num(kg)
            self.model.insertRows(self.i,1)
            # et_name    
            self.model.setData(self.model.index(self.i,1),self.ui.lineEdit.text())
            self.model.setData(self.model.index(self.i,2), int(le_2))
            self.model.setData(self.model.index(self.i,3), int(le_3))
            self.model.submitAll()
            self.i += 1
            self.ui.lcdNumber.display(self.i)
            self.lineEdit_clear()
        except ValueError:
            print('error')

    def delrow(self):
        if self.ui.tableWidget.currentIndex().row() > -1:
            self.model.removeRow(self.ui.tableWidget.currentIndex().row())
            self.i -= 1
            self.model.select()
            self.ui.lcdNumber.display(self.i)
        else:
            self.show_dialog("دوباره تلاش کنید.")
            self.show()

    def updaterow(self):
        # convert persian/Arabic digit to english number.
        le_2 = self.convert_num(self.ui.lineEdit_2.text())
        le_3 = self.convert_num(self.ui.lineEdit_3.text())

        if self.ui.tableWidget.currentIndex().row() > -1:
            record = self.model.record(self.ui.tableWidget.currentIndex().row())
            try:
                record.setValue("kg",int(le_3))
            except ValueError:
                self.show_dialog("مقدار نباید خالی باشد.")
                return
            try:
                record.setValue("sj",int(le_2))
            except ValueError:
                self.show_dialog("مقدار نباید خالی باشد.")
                return

            record.setValue("name", self.ui.lineEdit.text())
            self.model.setRecord(self.ui.tableWidget.currentIndex().row(), record)
        else:
            self.show_dialog("ابتدا یکی از فیلد ها را انتخاب کیند.")
            self.show()
        self.lineEdit_clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Controller = Controller()
    Controller.Show_FirstWindow()
    sys.exit(app.exec_())
