
import sys
import time

from PyQt5.QtCore import *
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtWidgets
from dronekit import VehicleMode
from Widgets.add_waypoint import Ui_Dialog

from Ui_main1 import Ui_MainWindow
from auto_mission1 import vehicle

class MyThread(QThread):

    change_value=pyqtSignal(float)
    change_gspeed=pyqtSignal(float)
    change_vspeed=pyqtSignal(float)
    change_mode=pyqtSignal(str)


    def run(self):
        print("Arming drone")

        while not vehicle.is_armable:
            time.sleep(1)

        vehicle.mode = VehicleMode("GUIDED")
        vehicle.armed = True

        while not vehicle.armed:
            time.sleep(1)

        print("Takeoff")
        vehicle.simple_takeoff(ui.talt)

        while True:
            altitude = vehicle.location.global_relative_frame.alt
            print(altitude)

            if altitude >= ui.talt - 0.05:
                print("Altitude reached")
                break

            time.sleep(0.3)
            self.change_value.emit(altitude)
            self.change_gspeed.emit(vehicle.groundspeed)
            self.change_vspeed.emit(-1*vehicle.velocity[2])
            self.change_mode.emit(vehicle.mode.name)

        self.change_value.emit(vehicle.location.global_relative_frame.alt)
        vehicle.mode = VehicleMode("AUTO")
        time.sleep(3)
        self.change_mode.emit(vehicle.mode.name)
        print(vehicle.mode.name)
        while vehicle.mode.name=="AUTO":
            time.sleep(0.3)
            print(vehicle.location.global_relative_frame.alt)
            self.change_value.emit(vehicle.location.global_relative_frame.alt)
            self.change_gspeed.emit(vehicle.groundspeed)
            self.change_vspeed.emit(-1*vehicle.velocity[2])

            #distance_home()
            #vehicle.velocity[2]
            if (vehicle.location.global_relative_frame.alt)<=0.005:
                break

        vehicle.mode.name="STABILIZE"
        time.sleep(3)
        self.change_mode.emit(vehicle.mode.name)


class TInteractObj(QObject):
    """
         A slot function for js to call (internally, the call of js is finally converted into a signal),
         A signal for js binding,
         This is the most basic component of an interactive object.
    """

    # Define the signal, which will bind a js method in js.
    sig_send_to_js = pyqtSignal(list)
    sig_send_to_js_1=pyqtSignal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        # The callback function executed after the interactive object receives the js call.
        # self.receive_str_from_js_callback = None

        # str means receiving str type signal, the signal is sent from js.

    # @pyqtSlot(str)
    # def receive_str_from_js(self, str):
    #     self.receive_str_from_js_callback(str)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.addWaypoint.clicked.connect(self.addwaypoint)
        url = QUrl.fromLocalFile(r"C:\Users\DELL\PycharmProjects\map\Map new\index1.html")
        self.webview.load(url)
        self.takeoff.clicked.connect(self.armTakeoff)


        self.init_channel()

    def armTakeoff(self):
        self.newMission.setEnabled(False)
        self.addWaypoint.setEnabled(False)
        self.rtl.setEnabled(False)
        self.altSave.setEnabled(False)
        self.thread = MyThread()
        self.thread.change_value.connect(self.setAltitudeValue)
        self.thread.change_gspeed.connect(self.setgspeed)
        self.thread.change_vspeed.connect(self.setvspeed)
        self.thread.change_mode.connect(self.setmode)
        self.thread.start()

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


    @pyqtSlot()
    def on_pushButton_clicked(self):

            # This signal is bound to a js method in js, so the corresponding js method will be executed when this signal is emitted.
        self.interact_obj.sig_send_to_js.emit([vehicle.home_location.lat, vehicle.home_location.lon])

    # @pyqtSlot()
    def addwaypoint(self):
        # This signal is bound to a js method in js, so the corresponding js method will be executed when this signal is emitted.

        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()
        resp = self.Dialog.exec_()
        if resp == QtWidgets.QDialog.Accepted:
            if (self.ui.latvalidator.validate(self.ui.lineEdit.text(), 0)[0] == 2 and
                    self.ui.longvalidator.validate(self.ui.lineEdit_2.text(), 0)[0] == 2 and
                    self.ui.altvalidator.validate(self.ui.lineEdit_3.text(), 0)[0] == 2):
                self.newwaypoint()
            else:
                self.addwaypoint()

    def newwaypoint(self):
        state, lat, pos = self.ui.latvalidator.validate(self.ui.lineEdit.text(), 0)
        self.lati = float(lat)
        state, long, pos = self.ui.longvalidator.validate(self.ui.lineEdit_2.text(), 0)
        self.longi = float(long)
        state, alt, pos = self.ui.altvalidator.validate(self.ui.lineEdit_3.text(), 0)
        self.alti = float(alt)
        print(lat + " " + long + " " + alt)
        print(type(self.lati))
        print(type(self.longi))
        print(type(self.alti))
        self.addnewrow("WAYPOINT", lat, long, alt, "RELATIVE")
        self.interact_obj.sig_send_to_js_1.emit([lat,long])



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())