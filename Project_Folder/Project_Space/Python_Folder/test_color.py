# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_color.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.UserID_Input = QtWidgets.QLineEdit(Form)
        self.UserID_Input.setGeometry(QtCore.QRect(140, 50, 113, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(252, 80, 124, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 80, 124, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 236, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.UserID_Input.setPalette(palette)
        self.UserID_Input.setText("")
        self.UserID_Input.setObjectName("UserID_Input")
        self.Password_Label = QtWidgets.QLabel(Form)
        self.Password_Label.setGeometry(QtCore.QRect(60, 90, 60, 16))
        self.Password_Label.setObjectName("Password_Label")
        self.Password_Input = QtWidgets.QLineEdit(Form)
        self.Password_Input.setGeometry(QtCore.QRect(140, 90, 113, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 147, 9, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 200, 23, 94))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 147, 9, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 200, 23, 94))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 147, 9, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 236, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.Password_Input.setPalette(palette)
        self.Password_Input.setText("")
        self.Password_Input.setObjectName("Password_Input")
        self.UserID_Label = QtWidgets.QLabel(Form)
        self.UserID_Label.setGeometry(QtCore.QRect(60, 50, 60, 16))
        self.UserID_Label.setObjectName("UserID_Label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Password_Label.setText(_translate("Form", "Password"))
        self.UserID_Label.setText(_translate("Form", "UserID"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
