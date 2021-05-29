import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QTableWidget,
    QTableWidgetItem,
    QStyle
)

class Contacts(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QTableView Example")
        self.resize(450, 250)
        # Set up the view1 and load the data
        self.view1 = QTableWidget()
        self.view1.setColumnCount(5)
        self.view1.setHorizontalHeaderLabels(["ID", "Name", "Jobeee", "Email","MyTest"])      #Field Header Label you can put any
        #self.view1.setStyle("font-clolor:red")
        query = QSqlQuery("SELECT id, name, job, email FROM contacts")
        while query.next():
            rows = self.view1.rowCount()
            self.view1.setRowCount(rows + 1)
            self.view1.setItem(rows, 0, QTableWidgetItem(str(query.value(0))))
            self.view1.setItem(rows, 1, QTableWidgetItem(query.value(1)))
            self.view1.setItem(rows, 2, QTableWidgetItem(query.value(2)))
            self.view1.setItem(rows, 3, QTableWidgetItem(query.value(3)))
        self.view1.resizeColumnsToContents()
        self.setCentralWidget(self.view1)

def createConnection():
    con = QSqlDatabase.addDatabase("QSQLITE")
    con.setDatabaseName("contacts.sqlite")
    if not con.open():
        QMessageBox.critical(
            None,
            "QTableview Example - Error!",
            "Database Error: %s" % con.lastError().databaseText(),
        )
        return False
    return True
app = QApplication(sys.argv)
if not createConnection():
    sys.exit(1)
win = Contacts()
win.show()
sys.exit(app.exec_())
