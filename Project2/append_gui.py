# Form implementation generated from reading ui file 'append_gui.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow4(object):
    def setupUi(self, MainWindow4):
        MainWindow4.setObjectName("MainWindow4")
        MainWindow4.resize(200, 151)
        MainWindow4.setMinimumSize(QtCore.QSize(200, 151))
        MainWindow4.setMaximumSize(QtCore.QSize(200, 151))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow4)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 181, 121))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.Button_yes = QtWidgets.QPushButton(parent=self.groupBox)
        self.Button_yes.setGeometry(QtCore.QRect(40, 30, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Button_yes.setFont(font)
        self.Button_yes.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Button_yes.setObjectName("Button_yes")
        self.Button_no = QtWidgets.QPushButton(parent=self.groupBox)
        self.Button_no.setGeometry(QtCore.QRect(40, 70, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Button_no.setFont(font)
        self.Button_no.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Button_no.setObjectName("Button_no")
        MainWindow4.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow4)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 200, 21))
        self.menubar.setObjectName("menubar")
        MainWindow4.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow4)
        self.statusbar.setObjectName("statusbar")
        MainWindow4.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow4)

    def retranslateUi(self, MainWindow4):
        _translate = QtCore.QCoreApplication.translate
        MainWindow4.setWindowTitle(_translate("MainWindow4", "Append"))
        self.groupBox.setTitle(_translate("MainWindow4", "Append Existing File?"))
        self.Button_yes.setText(_translate("MainWindow4", "Yes"))
        self.Button_no.setText(_translate("MainWindow4", "No"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow4 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow4()
    ui.setupUi(MainWindow4)
    MainWindow4.show()
    sys.exit(app.exec())
