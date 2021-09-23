import os
import sys

from PyQt5.QtCore import *
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWidgets import QMainWindow, QApplication

from Ui_main import Ui_MainWindow


class TInteractObj(QObject):
    """
         A slot function for js to call (internally, the call of js is finally converted into a signal),
         A signal for js binding,
         This is the most basic component of an interactive object.
    """

    # Define the signal, which will bind a js method in js.
    sig_send_to_js = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        # The callback function executed after the interactive object receives the js call.
        self.receive_str_from_js_callback = None

        # str means receiving str type signal, the signal is sent from js.

    @pyqtSlot(str)
    def receive_str_from_js(self, str):
        self.receive_str_from_js_callback(str)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.index = (os.path.split(os.path.realpath(__file__))[0]) + "/index.html"
        self.webview.load(QUrl.fromLocalFile(self.index))
        self.init_channel()

    def init_channel(self):
        """
                 Bind interactive objects for webview
        """
        self.interact_obj = TInteractObj(self)
        self.interact_obj.receive_str_from_js_callback = self.receive_data

        channel = QWebChannel(self.webview.page())
        # interact_obj is the name of the interactive object, used in js.
        channel.registerObject("interact_obj", self.interact_obj)

        self.webview.page().setWebChannel(channel)

    def receive_data(self, data):
        self.textBrowser.setText(data)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        if not self.textBrowser.toPlainText():
            return
            # This signal is bound to a js method in js, so the corresponding js method will be executed when this signal is emitted.
        self.interact_obj.sig_send_to_js.emit(self.textBrowser.toPlainText())
        self.textBrowser.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())