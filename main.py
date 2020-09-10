import sys
from ui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableView,QInputDialog,QFileDialog
from PyQt5 import QtSql,QtCore,QtGui
import pandas as pd
import sqlite3
from credit import *
from pathlib import Path

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

    def browseSlot(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file, _ = QtWidgets.QFileDialog.getOpenFileName(
                        None,
                        "QFileDialog.getOpenFileName()",
                        "",
                        "All Files (*);;Python Files (*.py)",
                        options=options)
        if file:
            self.daily_stats(file)


    def print_message(self):
        print('deleted!')
        

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
        for i in df.index:
            for row in result:                
                name_in_db   = row[1]
                name_in_file = df['name'][i] 
                basis = df['basis'][i]
                if(name_in_db == name_in_file):
                    # total_stats = 1500 => meal = 1300
                    kgr = int(basis) * 10
                    kgk = int(basis) * 20
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
        sqliteCon.commit()
        cursor.close()
        self.model = QtSql.QSqlTableModel()
        self.model.setTable('supply')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.select()
        self.ui.tableWidget.setModel(self.model)        
        print('---------------------------------')
        
    def addToDb(self):
        # todo: Validation
        self.model.insertRows(self.i,1)
        # et_name    
        self.model.setData(self.model.index(self.i,1),self.ui.lineEdit.text())
        try:
            self.model.setData(self.model.index(self.i,2), self.ui.lineEdit_2.text())
        except ValueError:
            QMessageBox.question(self,'اخطار', "مقدار صرفه جویی حتما باید به عدد وارد شود", QMessageBox.Ok)

        try:
            self.model.setData(self.model.index(self.i,3), int(self.ui.lineEdit_3.text()))
        except ValueError:
            QMessageBox.question(self,'اخطار', "مقدار/تعداد حتما باید به عدد وارد شود", QMessageBox.Ok)

        self.model.submitAll()
        self.i += 1
        self.ui.lcdNumber.display(self.i)

    def delrow(self):
        if self.ui.tableWidget.currentIndex().row() > -1:
            self.model.removeRow(self.ui.tableWidget.currentIndex().row())
            self.i -= 1
            self.model.select()
            self.ui.lcdNumber.display(self.i)
        else:
            QMessageBox.question(self,'پیام', "لطفا قبل از فشردن دکمه یکی از فیلد ها را انتخاب کنید", QMessageBox.Ok)
            self.show()

    def updaterow(self):
        if self.ui.tableWidget.currentIndex().row() > -1:
            record = self.model.record(self.ui.tableWidget.currentIndex().row())
            try:
                record.setValue("kg",int(self.ui.lineEdit_3.text()))
            except ValueError:
                QMessageBox.question(self,'اخطار', "مقدار/تعداد حتما باید به عدد وارد شود", QMessageBox.Ok)
            try:
                record.setValue("sj",self.ui.lineEdit_2.text())
            except ValueError:
                QMessageBox.question(self,'اخطار', "صرفه جویی حتما باید به عدد وارد شود", QMessageBox.Ok)

            record.setValue("name", self.ui.lineEdit.text())
            self.model.setRecord(self.ui.tableWidget.currentIndex().row(), record)
        else:
            QMessageBox.question(self,'پیام', "لطفا قبل از فشردن دکمه یکی از فیلد ها را انتخاب کنید", QMessageBox.Ok)
            self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Controller = Controller()
    Controller.Show_FirstWindow()
    sys.exit(app.exec_())
