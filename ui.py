from PyQt5 import QtCore, QtGui, QtWidgets
import func

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(720, 434)
        palette = QtGui.QPalette()
        Dialog.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        Dialog.setFont(font)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Dialog.setStyleSheet("background-image:url(\"background.jpg\");")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(310, 260, 141, 41))
        self.pushButton.setStyleSheet("font: 12pt \"YouYuan\";\n"
"color:white;\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(330, 20, 95, 25))
        self.comboBox.setStyleSheet("font: 12pt \"YouYuan\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(150, 80, 451, 141))
        self.frame.setStyleSheet("background:rgb(170, 255, 255);\n"
"border-radius:20px;\n"
"border-color:black;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.frame)
        self.doubleSpinBox.setGeometry(QtCore.QRect(65, 107, 62, 22))
        self.doubleSpinBox.setStyleSheet("background:rgb(170, 255, 255);\n"
"font: 12pt \"YouYuan\";\n"
"border:none;")
        self.doubleSpinBox.setMinimum(-10.0)
        self.doubleSpinBox.setMaximum(10.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.frame)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(65, 10, 62, 22))
        self.doubleSpinBox_2.setStyleSheet("background:rgb(170, 255, 255);\n"
"font: 12pt \"YouYuan\";\n"
"border:none;")
        self.doubleSpinBox_2.setMinimum(-10.0)
        self.doubleSpinBox_2.setMaximum(10.0)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(90, 50, 301, 61))
        self.label.setStyleSheet("background:rgb(170, 255, 255);\n"
"border:0;\n"
"font: 36pt \"YouYuan\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(45, 10, 55, 111))
        self.label_2.setStyleSheet("background:rgb(170, 255, 255);\n"
"border:0;\n"
"font: 48pt \"YouYuan\";")
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.doubleSpinBox_2.raise_()
        self.doubleSpinBox.raise_()
        self.label.raise_()
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(120, 320, 521, 71))
        self.tableWidget.setMinimumSize(QtCore.QSize(381, 0))
        self.tableWidget.setStyleSheet("font: 10pt \"YouYuan\";\n"
"background:rgb(170, 255, 255);\n"
"border:none;")
        self.tableWidget.setTabKeyNavigation(True)
        self.tableWidget.setProperty("showDropIndicator", True)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.CustomDashLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(149)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(47)
        self.tableWidget.verticalHeader().setDefaultSectionSize(45)
        self.frame.raise_()
        self.pushButton.raise_()
        self.comboBox.raise_()
        self.tableWidget.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Calculate"))
        self.comboBox.setItemText(0, _translate("Dialog", "sin(x)"))
        self.comboBox.setItemText(1, _translate("Dialog", "cos^2(x)"))
        self.comboBox.setItemText(2, _translate("Dialog", "3*(x^4)"))
        self.comboBox.setItemText(3, _translate("Dialog", "x^3"))
        self.comboBox.setItemText(4, _translate("Dialog", "cos(x)"))
        self.comboBox.setItemText(5, _translate("Dialog", "x^2"))
        self.comboBox.currentTextChanged.connect(self.on_change_fun)
        self.pushButton.clicked.connect(self.on_click_button)
        self.label.setText(_translate("Dialog", "sin(x)"))
        self.label_2.setText(_translate("Dialog", "∫"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "Meaning"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "simpson"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "3/8 meth"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "5dot meth"))


    def on_change_fun(self):
        self.label.setText(str(self.comboBox.currentText()))


    def on_click_button(self):
        s = func.get_result(self.doubleSpinBox.value(),self.doubleSpinBox_2.value(),self.comboBox.currentText())
        self.tableWidget.setItem(0,0,QtWidgets.QTableWidgetItem(str(s[0])))
        self.tableWidget.setItem(0,1,QtWidgets.QTableWidgetItem(str(s[1])))
        self.tableWidget.setItem(0,2,QtWidgets.QTableWidgetItem(str(s[2])))

