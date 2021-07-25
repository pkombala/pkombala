from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
import mysql.connector as mc
ui, _ = loadUiType('school.ui')

class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.tabBar().setVisible(False)  # Hide TabBar
        self.menubar.setVisible(False)  # Hide MenuBar
        self.b01.clicked.connect(self.login)  # login Butten
        self.menu11.triggered.connect(self.show_add_new_student_tab)
        self.pb11.clicked.connect(self.save_student_details)
        self.menu12.triggered.connect(self.edit_or_delete_student_tab)
        self.cb21.currentIndexChanged.connect(self.fill_details_when_combo_box_selected)
        self.pb21.clicked.connect(self.edit_student_details)
        self.pb22.clicked.connect(self.delete_student_detals)


    #########    login function   ######

    def login(self):
        un = self.tb01.text()
        pw = self.tb02.text()
        if (un == "admin" and pw == "admin"):
            self.menubar.setVisible(True)
            self.tabWidget.setCurrentIndex(1)
        else:
            QMessageBox.information(self, "School Management system","Invalid Username or Password")
            self.l01.setText("Invalid Username or Password")
            self.l01.setStyleSheet("background-color: yellow; border:1px solid black;")

    ########    Add New Student     #####################################

    def show_add_new_student_tab(self):
        self.tabWidget.setCurrentIndex(2)
        self.fill_next_registration_number()

    def fill_next_registration_number(self):
        try:
            rn = 1000
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="school"
            )
            cursor = mydb.cursor()
            cursor.execute("select * from student")
            result = cursor.fetchall()
            if result:
                for stud in result:
                    rn += 1
            self.tb11.setText(str(rn+1))
        except mc.Error as e:
            self.l11.setText("Error in connection" + e)

    def save_student_details(self):
        try:

            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="school"
            )
            cursor = mydb.cursor()

            registration_number = self.tb11.text()
            full_name = self.tb12.text()
            gender = self.cb11.currentText()
            date_of_birth = self.de11.text()
            age = self.tb15.text()
            address = self.tb16.toPlainText()
            phone = self.tb13.text()
            email = self.tb14.text()
            standard = self.cb12.currentText()

            qry = "Insert into student (registration_number,full_name,gender,date_of_birth,age,address,phone,email,standard)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            value = (registration_number, full_name, gender, date_of_birth, age, address, phone, email, standard)
            cursor.execute(qry, value)
            mydb.commit()
            self.tb12.clear()
            #self.l11.setText("Student registration saved")
            #self.l11.setStyleSheet("background-color: yellow; border:1px solid black;")
            QMessageBox.information(self, "School Management system","Student name saved successfully")
            #self.tabWidget.setCurrentIndex(1)
        except mc.Error as e:
            self.l11.setText("error in save student form" + e)

    ########## edit or delete Student ################################

    def edit_or_delete_student_tab(self):
        self.tabWidget.setCurrentIndex(3)
        self.fill_registration_number_in_combobox()

    def fill_registration_number_in_combobox(self):
        try:
            self.cb21.clear()

            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="school"
            )
            cursor = mydb.cursor()
            cursor.execute("select * from student")
            result = cursor.fetchall()
            if result:
                for stud in result:
                    self.cb21.addItem(str(stud[1]))
        except mc.Error as e:
            self.l11.setText("Error in registration number fill in  combobox " + e)

    def fill_details_when_combo_box_selected(self):
        try:
            self.l11.clear()

            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="school"
            )
            cursor = mydb.cursor()
            cursor.execute("select * from student where registration_number = '" + self.cb21.currentText() + "'")
            result = cursor.fetchall()
            if result:
                for stud in result:
                    self.tb21.setText(str(stud[2]))
                    self.cb22.setCurrentText(str(stud[3]))
                    self.tb23.setText(str(stud[7]))
                    self.tb24.setText(str(stud[8]))
                    self.tb17.setText(str(stud[4]))  # self.de21.setDate(QDate.currentDate())
                    self.tb25.setText(str(stud[5]))
                    self.tb26.setText(str(stud[6]))
                    self.cb23.setCurrentText(str(stud[9]))
        except mc.Error as e:
            self.l11.setText("Error in combobox get data" + e)
    def edit_student_details(self):
        try:
            #self.l21.clear()
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="school"
            )
            cursor = mydb.cursor()
            registration_number = self.cb21.currentText()
            full_name = self.tb21.text()
            gender = self.cb22.currentText()
            date_of_birth = self.tb17.text()
            age = self.tb25.text()
            address = self.tb26.toPlainText()
            phone = self.tb23.text()
            email = self.tb24.text()
            standard = self.cb23.currentText()
            qry = "update student set full_name = '" + full_name + "', gender = '" + gender + "', date_of_birth = '" + date_of_birth + "',age = '" + age + "',address = '" + address + "', phone = '" + phone + "',email = '" + email + "',standard = '" + standard + "' where registration_number = '" + registration_number + "'"
            cursor.execute(qry)
            mydb.commit()

            self.l21.setText("Student registration Modifyed ")
            self.l21.setStyleSheet("background-color: yellow; border:1px solid black;")
        except mc.Error as e:
            self.l21.setText("error in save student form" + e)
    def delete_student_detals(self):
        m = QMessageBox.question(self,"Delete Student ", "Are you sure want to delete ", QMessageBox.Yes|QMessageBox.No)
        if m == QMessageBox.Yes:
            try:

                mydb = mc.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="school"
                )
                cursor = mydb.cursor()

                registration_number = self.cb21.currentText()
                qry = "Delete from student where registration_number = '" + registration_number + "' "
                cursor.execute(qry)
                mydb.commit()
                self.cb21.clear()
                #self.l21.setText("Student registration Deleted ")
                #self.l21.setStyleSheet("background-color: yellow; border:1px solid black;")
                #QMessageBox.information(self,"School Management Sys")
                #self.tabWidget.setCurrentIndex(1)
            except mc.Error as e:
                self.l21.setText("error in save student form" + e)
    ##############################################################################
def main():
    app = QApplication(sys.argv)
    windows = MainApp()
    windows.show()
    app.exec_()


if __name__ == '__main__':
    main()
