import os
import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import *
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView




class TInteractObj(QObject):
    """
         A slot function for js to call (internally, the call of js is finally converted into a signal),
         A signal for js binding,
         This is the most basic component of an interactive object.
    """

    # Define the signal, which will bind a js method in js.
    addwaypoint = pyqtSignal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        # The callback function executed after the interactive object receives the js call.
        #self.receive_str_from_js_callback = None

        # str means receiving str type signal, the signal is sent from js.

    # @pyqtSlot(str)
    # def receive_str_from_js(self, str):
    #     self.receive_str_from_js_callback(str)


class MainWindow(QMainWindow ):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        #self.index = (os.path.split(os.path.realpath(__file__))[0]) + "/index.html"
        #self.webview.load(QUrl.fromLocalFile(self.index))
        self.init_channel()

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
        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setObjectName("pushButton")
        self.layout.addWidget(self.pushButton)
        #self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.webview = QWebEngineView()
        self.webview.setObjectName("webview")
        url = QtCore.QUrl.fromLocalFile(r"C:\Users\DELL\PycharmProjects\map\index.html")
        self.webview.load(url)
        # file = open(r"C:\Users\DELL\PycharmProjects\map\index.html", "r")
        # html = file.read()
        # html = html.replace("lat", "20.4793264")
        # html = html.replace("long", "85.8995999")
        # self.webview.setHtml(html)
        self.webview.setMinimumWidth(400)
        self.layout.addWidget(self.webview)
        #self.gridLayout.addWidget(self.webview, 0, 1, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Sync to web"))

    def init_channel(self):
        """
                 Bind interactive objects for webview
        """
        self.interact_obj = TInteractObj(self)
        #self.interact_obj.receive_str_from_js_callback = self.receive_data

        channel = QWebChannel(self.webview.page())
        # interact_obj is the name of the interactive object, used in js.
        channel.registerObject("interact_obj", self.interact_obj)

        self.webview.page().setWebChannel(channel)

    # def receive_data(self, data):
    #     self.textBrowser.setText(data)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        # if not self.textBrowser.toPlainText():
        #     return
            # This signal is bound to a js method in js, so the corresponding js method will be executed when this signal is emitted.
        self.interact_obj.addwaypoint.emit([20.4793259, 85.8995998])
        #self.textBrowser.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())