# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Delete.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Delete(object):
    def setupUi(self, Delete):
        Delete.setObjectName("Delete")
        Delete.resize(251, 174)
        self.Delete_button = QtWidgets.QPushButton(Delete)
        self.Delete_button.setGeometry(QtCore.QRect(70, 80, 113, 32))
        self.Delete_button.setObjectName("Delete_button")
        self.ID_label = QtWidgets.QLabel(Delete)
        self.ID_label.setGeometry(QtCore.QRect(50, 50, 81, 16))
        self.ID_label.setObjectName("ID_label")
        self.ID_input = QtWidgets.QLineEdit(Delete)
        self.ID_input.setGeometry(QtCore.QRect(90, 50, 113, 21))
        self.ID_input.setText("")
        self.ID_input.setObjectName("ID_input")
        self.Delete_message = QtWidgets.QLabel(Delete)
        self.Delete_message.setGeometry(QtCore.QRect(30, 10, 201, 31))
        self.Delete_message.setObjectName("Delete_message")
        self.Delete_success_message = QtWidgets.QLabel(Delete)
        self.Delete_success_message.setGeometry(QtCore.QRect(80, 120, 151, 16))
        self.Delete_success_message.setObjectName("Delete_success_message")
        self.ID_Doesnt_Exist_message = QtWidgets.QLabel(Delete)
        self.ID_Doesnt_Exist_message.setGeometry(QtCore.QRect(80, 120, 151, 16))
        self.ID_Doesnt_Exist_message.setObjectName("ID_Doesnt_Exist_message")

        self.retranslateUi(Delete)
        QtCore.QMetaObject.connectSlotsByName(Delete)

    def retranslateUi(self, Delete):
        _translate = QtCore.QCoreApplication.translate
        Delete.setWindowTitle(_translate("Delete", "Delete"))
        self.Delete_button.setText(_translate("Delete", "Delete"))
        self.ID_label.setText(_translate("Delete", "ID"))
        self.Delete_message.setText(_translate("Delete", "Type the user ID to delete a user"))
        self.Delete_success_message.setText(_translate("Delete", "Delete success!!"))
        self.ID_Doesnt_Exist_message.setText(_translate("Delete", "ID doesn\'t exist!!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Delete = QtWidgets.QWidget()
    ui = Ui_Delete()
    ui.setupUi(Delete)
    Delete.show()
    sys.exit(app.exec_())
