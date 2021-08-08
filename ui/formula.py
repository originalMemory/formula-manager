# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formula.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Formula(object):
    def setupUi(self, Formula):
        Formula.setObjectName("Formula")
        Formula.resize(1393, 975)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Formula)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(Formula)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter_2 = QtWidgets.QSplitter(self.widget)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 300))
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonFormulaEdit = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButtonFormulaEdit.setMaximumSize(QtCore.QSize(120, 16777215))
        self.pushButtonFormulaEdit.setObjectName("pushButtonFormulaEdit")
        self.gridLayout.addWidget(self.pushButtonFormulaEdit, 0, 1, 1, 1)
        self.pushButtonFormulaSearch = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButtonFormulaSearch.setObjectName("pushButtonFormulaSearch")
        self.gridLayout.addWidget(self.pushButtonFormulaSearch, 1, 0, 1, 1)
        self.pushButtonFormulaAdd = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButtonFormulaAdd.setMaximumSize(QtCore.QSize(120, 16777215))
        self.pushButtonFormulaAdd.setObjectName("pushButtonFormulaAdd")
        self.gridLayout.addWidget(self.pushButtonFormulaAdd, 0, 0, 1, 1)
        self.pushButtonFormulaDel = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButtonFormulaDel.setObjectName("pushButtonFormulaDel")
        self.gridLayout.addWidget(self.pushButtonFormulaDel, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.widget_7 = QtWidgets.QWidget(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setContentsMargins(10, 5, 10, 5)
        self.gridLayout_4.setVerticalSpacing(4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButtonPrePage = QtWidgets.QPushButton(self.widget_7)
        self.pushButtonPrePage.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButtonPrePage.setObjectName("pushButtonPrePage")
        self.gridLayout_4.addWidget(self.pushButtonPrePage, 0, 0, 1, 1)
        self.labelPage = QtWidgets.QLabel(self.widget_7)
        self.labelPage.setMaximumSize(QtCore.QSize(150, 16777215))
        self.labelPage.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPage.setObjectName("labelPage")
        self.gridLayout_4.addWidget(self.labelPage, 0, 1, 1, 1)
        self.pushButtonNextPage = QtWidgets.QPushButton(self.widget_7)
        self.pushButtonNextPage.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButtonNextPage.setObjectName("pushButtonNextPage")
        self.gridLayout_4.addWidget(self.pushButtonNextPage, 0, 2, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_4)
        self.listViewFormula = QtWidgets.QListView(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.listViewFormula.sizePolicy().hasHeightForWidth())
        self.listViewFormula.setSizePolicy(sizePolicy)
        self.listViewFormula.setObjectName("listViewFormula")
        self.verticalLayout_6.addWidget(self.listViewFormula)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.verticalLayout.addWidget(self.splitter_2)
        self.widget_2 = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter_3 = QtWidgets.QSplitter(self.widget_2)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.groupBox = QtWidgets.QGroupBox(self.splitter_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 150))
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout_3.setContentsMargins(10, 10, -1, -1)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEditColorNo = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditColorNo.setObjectName("lineEditColorNo")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditColorNo)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEditColorName = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditColorName.setObjectName("lineEditColorName")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditColorName)
        self.lineEditQuality = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditQuality.setObjectName("lineEditQuality")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditQuality)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout_6.addLayout(self.formLayout_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.splitter_4 = QtWidgets.QSplitter(self.groupBox_2)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.widget_3 = QtWidgets.QWidget(self.splitter_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.splitter_5 = QtWidgets.QSplitter(self.widget_3)
        self.splitter_5.setOrientation(QtCore.Qt.Vertical)
        self.splitter_5.setObjectName("splitter_5")
        self.widget_4 = QtWidgets.QWidget(self.splitter_5)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.widget_4)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEditDyeName = QtWidgets.QLineEdit(self.widget_4)
        self.lineEditDyeName.setObjectName("lineEditDyeName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditDyeName)
        self.label_5 = QtWidgets.QLabel(self.widget_4)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEditDyeNum = QtWidgets.QLineEdit(self.widget_4)
        self.lineEditDyeNum.setObjectName("lineEditDyeNum")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditDyeNum)
        self.horizontalLayout_3.addLayout(self.formLayout)
        self.widget1 = QtWidgets.QWidget(self.splitter_5)
        self.widget1.setObjectName("widget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButtonDyeAdd = QtWidgets.QPushButton(self.widget1)
        self.pushButtonDyeAdd.setMaximumSize(QtCore.QSize(120, 16777215))
        self.pushButtonDyeAdd.setObjectName("pushButtonDyeAdd")
        self.gridLayout_2.addWidget(self.pushButtonDyeAdd, 0, 0, 1, 1)
        self.pushButtonDyeEdit = QtWidgets.QPushButton(self.widget1)
        self.pushButtonDyeEdit.setMaximumSize(QtCore.QSize(120, 16777215))
        self.pushButtonDyeEdit.setObjectName("pushButtonDyeEdit")
        self.gridLayout_2.addWidget(self.pushButtonDyeEdit, 0, 1, 1, 1)
        self.pushButtonDyeSearch = QtWidgets.QPushButton(self.widget1)
        self.pushButtonDyeSearch.setObjectName("pushButtonDyeSearch")
        self.gridLayout_2.addWidget(self.pushButtonDyeSearch, 1, 0, 1, 1)
        self.pushButtonDyeDel = QtWidgets.QPushButton(self.widget1)
        self.pushButtonDyeDel.setObjectName("pushButtonDyeDel")
        self.gridLayout_2.addWidget(self.pushButtonDyeDel, 1, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.splitter_5)
        self.tableViewDye = QtWidgets.QTableView(self.splitter_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableViewDye.sizePolicy().hasHeightForWidth())
        self.tableViewDye.setSizePolicy(sizePolicy)
        self.tableViewDye.setObjectName("tableViewDye")
        self.horizontalLayout_2.addWidget(self.splitter_4)
        self.groupBox_4 = QtWidgets.QGroupBox(self.splitter_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.splitter_6 = QtWidgets.QSplitter(self.groupBox_4)
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setObjectName("splitter_6")
        self.widget_5 = QtWidgets.QWidget(self.splitter_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.splitter_7 = QtWidgets.QSplitter(self.widget_5)
        self.splitter_7.setOrientation(QtCore.Qt.Vertical)
        self.splitter_7.setObjectName("splitter_7")
        self.widget_6 = QtWidgets.QWidget(self.splitter_7)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_6 = QtWidgets.QLabel(self.widget_6)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEditCatalyzerName = QtWidgets.QLineEdit(self.widget_6)
        self.lineEditCatalyzerName.setObjectName("lineEditCatalyzerName")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditCatalyzerName)
        self.label_7 = QtWidgets.QLabel(self.widget_6)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEditCatalyzerNum = QtWidgets.QLineEdit(self.widget_6)
        self.lineEditCatalyzerNum.setObjectName("lineEditCatalyzerNum")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditCatalyzerNum)
        self.horizontalLayout_4.addLayout(self.formLayout_2)
        self.layoutWidget = QtWidgets.QWidget(self.splitter_7)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButtonCatalyzerAdd = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonCatalyzerAdd.setMaximumSize(QtCore.QSize(120, 16777215))
        self.pushButtonCatalyzerAdd.setObjectName("pushButtonCatalyzerAdd")
        self.gridLayout_3.addWidget(self.pushButtonCatalyzerAdd, 0, 0, 1, 1)
        self.pushButtonCatalyzerEdit = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonCatalyzerEdit.setMaximumSize(QtCore.QSize(120, 16777215))
        self.pushButtonCatalyzerEdit.setObjectName("pushButtonCatalyzerEdit")
        self.gridLayout_3.addWidget(self.pushButtonCatalyzerEdit, 0, 1, 1, 1)
        self.pushButtonCatalyzerSearch = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonCatalyzerSearch.setObjectName("pushButtonCatalyzerSearch")
        self.gridLayout_3.addWidget(self.pushButtonCatalyzerSearch, 1, 0, 1, 1)
        self.pushButtonCatalyzerDel = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonCatalyzerDel.setObjectName("pushButtonCatalyzerDel")
        self.gridLayout_3.addWidget(self.pushButtonCatalyzerDel, 1, 1, 1, 1)
        self.verticalLayout_5.addWidget(self.splitter_7)
        self.tableViewCatalyzer = QtWidgets.QTableView(self.splitter_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableViewCatalyzer.sizePolicy().hasHeightForWidth())
        self.tableViewCatalyzer.setSizePolicy(sizePolicy)
        self.tableViewCatalyzer.setObjectName("tableViewCatalyzer")
        self.horizontalLayout_5.addWidget(self.splitter_6)
        self.verticalLayout_3.addWidget(self.splitter_3)
        self.horizontalLayout.addWidget(self.splitter)

        self.retranslateUi(Formula)
        QtCore.QMetaObject.connectSlotsByName(Formula)

    def retranslateUi(self, Formula):
        _translate = QtCore.QCoreApplication.translate
        Formula.setWindowTitle(_translate("Formula", "Form"))
        self.groupBox_3.setTitle(_translate("Formula", "功能区"))
        self.pushButtonFormulaEdit.setText(_translate("Formula", "修改"))
        self.pushButtonFormulaSearch.setText(_translate("Formula", "查找"))
        self.pushButtonFormulaAdd.setText(_translate("Formula", "添加"))
        self.pushButtonFormulaDel.setText(_translate("Formula", "删除"))
        self.pushButtonPrePage.setText(_translate("Formula", "上一页"))
        self.labelPage.setText(_translate("Formula", "1/1"))
        self.pushButtonNextPage.setText(_translate("Formula", "下一页"))
        self.groupBox.setTitle(_translate("Formula", "描述"))
        self.label.setText(_translate("Formula", "色号"))
        self.label_3.setText(_translate("Formula", "颜色"))
        self.label_2.setText(_translate("Formula", "品质"))
        self.groupBox_2.setTitle(_translate("Formula", "染料"))
        self.label_4.setText(_translate("Formula", "名称"))
        self.label_5.setText(_translate("Formula", "数量"))
        self.pushButtonDyeAdd.setText(_translate("Formula", "添加"))
        self.pushButtonDyeEdit.setText(_translate("Formula", "修改"))
        self.pushButtonDyeSearch.setText(_translate("Formula", "查找"))
        self.pushButtonDyeDel.setText(_translate("Formula", "删除"))
        self.groupBox_4.setTitle(_translate("Formula", "催化剂"))
        self.label_6.setText(_translate("Formula", "名称"))
        self.label_7.setText(_translate("Formula", "百分比"))
        self.pushButtonCatalyzerAdd.setText(_translate("Formula", "添加"))
        self.pushButtonCatalyzerEdit.setText(_translate("Formula", "修改"))
        self.pushButtonCatalyzerSearch.setText(_translate("Formula", "查找"))
        self.pushButtonCatalyzerDel.setText(_translate("Formula", "删除"))