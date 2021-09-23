from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 570)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layout=QtWidgets.QVBoxLayout(self.centralwidget)
        # self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        # self.gridLayout.setObjectName("gridLayout")
        # self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        # self.textBrowser.setObjectName("textBrowser")
        # self.textBrowser.setReadOnly(False)
        # self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.layout.addWidget(self.pushButton)
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setObjectName("pushButton1")
        self.layout.addWidget(self.pushButton1)
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setObjectName("pushButton2")
        self.layout.addWidget(self.pushButton2)
        self.pushButton2.clicked.connect(self.printz)
        # self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.webview = QWebEngineView(self.centralwidget)
        self.webview.setObjectName("webview")
        self.webview.setMinimumWidth(400)
        self.layout.addWidget(self.webview)
        # self.gridLayout.addWidget(self.webview, 0, 1, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Sync to web"))
        self.pushButton1.setText(_translate("MainWindow", "Sync to web1"))

    def printz(self):
        print("pushbutton2 clicked")