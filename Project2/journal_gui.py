# Form implementation generated from reading ui file 'journal_gui.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(811, 722)
        MainWindow.setMinimumSize(QtCore.QSize(811, 722))
        MainWindow.setMaximumSize(QtCore.QSize(811, 722))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 625, 251, 51))
        self.groupBox.setObjectName("groupBox")
        self.label_fileName = QtWidgets.QLabel(parent=self.groupBox)
        self.label_fileName.setGeometry(QtCore.QRect(10, 20, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_fileName.setFont(font)
        self.label_fileName.setObjectName("label_fileName")
        self.Button_open = QtWidgets.QPushButton(parent=self.groupBox)
        self.Button_open.setGeometry(QtCore.QRect(180, 20, 61, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Button_open.setFont(font)
        self.Button_open.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Button_open.setObjectName("Button_open")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 2, 791, 622))
        self.groupBox_3.setObjectName("groupBox_3")
        self.textEntryBox = QtWidgets.QTextEdit(parent=self.groupBox_3)
        self.textEntryBox.setGeometry(QtCore.QRect(10, 18, 771, 592))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.textEntryBox.setFont(font)
        self.textEntryBox.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.textEntryBox.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.textEntryBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.textEntryBox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.textEntryBox.setObjectName("textEntryBox")
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(460, 625, 341, 51))
        self.groupBox_4.setObjectName("groupBox_4")
        self.Button_save = QtWidgets.QPushButton(parent=self.groupBox_4)
        self.Button_save.setGeometry(QtCore.QRect(40, 20, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Button_save.setFont(font)
        self.Button_save.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Button_save.setObjectName("Button_save")
        self.Button_exit = QtWidgets.QPushButton(parent=self.groupBox_4)
        self.Button_exit.setGeometry(QtCore.QRect(180, 20, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Button_exit.setFont(font)
        self.Button_exit.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Button_exit.setObjectName("Button_exit")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(280, 625, 171, 51))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_info = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_info.setGeometry(QtCore.QRect(16, 20, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_info.setFont(font)
        self.label_info.setText("")
        self.label_info.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_info.setObjectName("label_info")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 811, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "JournalApp"))
        self.groupBox.setTitle(_translate("MainWindow", "File"))
        self.label_fileName.setText(_translate("MainWindow", "None"))
        self.Button_open.setText(_translate("MainWindow", "Open"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Journal"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Options"))
        self.Button_save.setText(_translate("MainWindow", "Save"))
        self.Button_exit.setText(_translate("MainWindow", "Exit"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Info"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())