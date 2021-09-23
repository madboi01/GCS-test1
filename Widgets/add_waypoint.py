# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Add_waypoint.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from decimal import Decimal

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QDoubleValidator







class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(491, 376)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(20, 70, 431, 171))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.latvalidator = QDoubleValidator(-90.0, 90.0, 8)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setValidator(self.latvalidator)
        self.lineEdit.setObjectName("lineEdit")
        self.float1 = QDoubleValidator()
        self.lineEdit.setValidator(self.float1)
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.longvalidator = QDoubleValidator(-180.0, 180.0, 8)
        self.lineEdit_2.setValidator(self.longvalidator)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.float2 = QDoubleValidator()
        self.lineEdit_2.setValidator(self.float2)
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.altvalidator = QDoubleValidator(0.0, 1000.0, 8)
        self.lineEdit_3.setValidator(self.altvalidator)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.float3 = QDoubleValidator()
        self.lineEdit_3.setValidator(self.float3)
        self.verticalLayout_2.addWidget(self.lineEdit_3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.horizontalLayout_1=QtWidgets.QHBoxLayout()
        self.label_4=QtWidgets.QLabel(self.widget)
        # self.label_4.setObjectName("label_4")
        # self.label_4.setText("Invalid Parameters")
        # self.label_4.setStyleSheet("QLabel{color:rgb(255, 0, 0);}")
        # self.verticalLayout_4=QtWidgets.QVBoxLayout(self.widget)
        # self.verticalLayout_4.addLayout(self.horizontalLayout)
        # self.verticalLayout_4.addWidget(self.label_4)
        # self.widget.setLayout(self.verticalLayout_4)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        #self.buttonBox.accepted.connect(self.addWaypoint)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # def addWaypoint(self):
    #     state, lat, pos = self.validator.validate(self.lineEdit.text(), 0)
    #     self.lati = float(lat)
    #     print(pos)
    #     state, long, pos = self.validator.validate(self.lineEdit_2.text(), 0)
    #     self.longi = float(long)
    #     print(state)
    #     state, alt, pos = self.validator.validate(self.lineEdit_3.text(), 0)
    #     self.alti = float(alt)



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "ADD WAYPOINT"))
        self.label.setText(_translate("Dialog", "LATITUDE:"))
        self.label_2.setText(_translate("Dialog", "LONGIITUDE:"))
        self.label_3.setText(_translate("Dialog", "ALTITUDE:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
