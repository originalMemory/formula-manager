# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'export.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Export(object):
    def setupUi(self, Export):
        Export.setObjectName("Export")
        Export.resize(1193, 849)
        self.verticalLayout = QtWidgets.QVBoxLayout(Export)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Export)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 150))
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 40, 40, 20))
        self.label.setObjectName("label")
        self.lineEditCustomName = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditCustomName.setGeometry(QtCore.QRect(70, 40, 111, 20))
        self.lineEditCustomName.setObjectName("lineEditCustomName")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 72, 40, 20))
        self.label_2.setObjectName("label_2")
        self.lineEditColorNo = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditColorNo.setGeometry(QtCore.QRect(70, 72, 111, 20))
        self.lineEditColorNo.setObjectName("lineEditColorNo")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(320, 40, 40, 20))
        self.label_3.setObjectName("label_3")
        self.lineEditWeight = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditWeight.setGeometry(QtCore.QRect(360, 40, 111, 20))
        self.lineEditWeight.setObjectName("lineEditWeight")
        self.pushButtonSearch = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonSearch.setGeometry(QtCore.QRect(220, 40, 75, 23))
        self.pushButtonSearch.setObjectName("pushButtonSearch")
        self.pushButtonExport = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonExport.setGeometry(QtCore.QRect(220, 70, 75, 23))
        self.pushButtonExport.setObjectName("pushButtonExport")
        self.pushButtonCompute = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonCompute.setGeometry(QtCore.QRect(490, 37, 75, 23))
        self.pushButtonCompute.setObjectName("pushButtonCompute")
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Export)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableView = QtWidgets.QTableView(self.groupBox_2)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setObjectName("tableView")
        self.horizontalLayout.addWidget(self.tableView)
        self.verticalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(Export)
        QtCore.QMetaObject.connectSlotsByName(Export)

    def retranslateUi(self, Export):
        _translate = QtCore.QCoreApplication.translate
        Export.setWindowTitle(_translate("Export", "Form"))
        self.groupBox.setTitle(_translate("Export", "?????????"))
        self.label.setText(_translate("Export", "?????????"))
        self.label_2.setText(_translate("Export", "??????"))
        self.label_3.setText(_translate("Export", "??????"))
        self.pushButtonSearch.setText(_translate("Export", "??????"))
        self.pushButtonExport.setText(_translate("Export", "??????Excel"))
        self.pushButtonCompute.setText(_translate("Export", "????????????"))
        self.groupBox_2.setTitle(_translate("Export", "????????????"))
