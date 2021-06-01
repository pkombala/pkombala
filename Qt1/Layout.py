import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QFormLayout,
    QLineEdit,
    QPushButton,
    QDialogButtonBox
)
from PyQt5.QtGui import QPalette, QColor

class Color(QWidget):
    def __init__ (self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)





class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")
        ### set Widget ########

        mainwidget = Color("Brown")
        self.setCentralWidget(mainwidget)



        #### Set Layout
        layout = QHBoxLayout()
        rlayout = QVBoxLayout()
        llayout = QVBoxLayout()

        ltoplayout = QHBoxLayout()
        lbotlayout = QVBoxLayout()
        rtoplayout = QHBoxLayout()
        rbotlayout = QFormLayout()
        llayout.addLayout(ltoplayout)
        llayout.addLayout(lbotlayout)
        rlayout.addLayout(rtoplayout)
        rlayout.addLayout(rbotlayout)
        layout.addLayout(llayout)
        layout.addLayout(rlayout)

        ltoplayout.addWidget(QPushButton("Left "))
        ltoplayout.addWidget(QPushButton("Center "))
        ltoplayout.addWidget(QPushButton("Right" ))
        llayout.addWidget(Color("green"))
        lbotlayout.addWidget(QPushButton("Left Butten"))
        lbotlayout.addWidget(QPushButton("Center Butten"))
        lbotlayout.addWidget(QPushButton("Right Butten"))
        lbotlayout.addStretch()


        rtoplayout.addStretch()
        rtoplayout.addWidget(QPushButton("Butten"))
        rtoplayout.addWidget(QPushButton("Butten"))

        rbotlayout.addRow("User Name:  ", QLineEdit())
        rbotlayout.addRow("Password:  ", QLineEdit())


        mainwidget.setLayout(layout)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()