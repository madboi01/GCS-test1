# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
import io
import folium
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
#from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
#from PyQt5.QtWebEngineWidgets import QWebEngineView

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):
        self.setWindowTitle(self.tr("MAP PROJECT"))
        self.setFixedSize(1500, 800)
        self.buttonUI()

    def buttonUI(self):
        shortPathButton = QtWidgets.QPushButton(self.tr("Find shortest path"))
        button2 = QtWidgets.QPushButton(self.tr("Another path"))
        button3 = QtWidgets.QPushButton(self.tr("Another path"))

        shortPathButton.setFixedSize(120, 50)
        button2.setFixedSize(120, 50)
        button3.setFixedSize(120, 50)

        self.view = QtWebEngineWidgets.QWebEngineView()
        self.view.setContentsMargins(50, 50, 50, 50)

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        lay = QtWidgets.QHBoxLayout(central_widget)

        button_container = QtWidgets.QWidget()
        vlay = QtWidgets.QVBoxLayout(button_container)
        vlay.setSpacing(20)
        vlay.addStretch()
        vlay.addWidget(shortPathButton)
        vlay.addWidget(button2)
        vlay.addWidget(button3)
        vlay.addStretch()
        lay.addWidget(button_container)
        lay.addWidget(self.view, stretch=1)

        token = "pk.eyJ1IjoiYW5raXQyMDAxIiwiYSI6ImNrcms4dHhodTBobGQycGxmbXM3NjB6ZTYifQ.VBdyp--xzk-nP7-_EM7PPg"  # your mapbox token
        tileurl = 'https://api.mapbox.com/v4/mapbox.satellite/{z}/{x}/{y}@2x.png?access_token=' + str(token)

        m = folium.Map(
            location=[48.73596, 11.18434], zoom_start=9, tiles=tileurl, attr='Mapbox')

        # m = folium.Map(
        #     location=[45.5236, -122.6750],tiles="Stamen Terrain", zoom_start=13
        # )

        data = io.BytesIO()
        m.save(data, close_file=False)
        self.view.setHtml(data.getvalue().decode())


if __name__ == "__main__":
    App = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(App.exec())
