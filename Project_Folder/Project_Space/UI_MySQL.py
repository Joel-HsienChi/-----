from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QLineEdit
import sys
import logging
import datetime
import hashlib
import re
import mysql.connector
from Logger import logger_class


# UI class
class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(305, 240)
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.Login_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Login_Button.setGeometry(QtCore.QRect(40, 110, 113, 32))
        self.Login_Button.setObjectName("Login_Button")
        self.UserID_Input = QtWidgets.QLineEdit(self.centralwidget)
        self.UserID_Input.setGeometry(QtCore.QRect(130, 30, 113, 21))
        self.UserID_Input.setText("")
        self.UserID_Input.setObjectName("UserID_Input")
        self.UserID_Label = QtWidgets.QLabel(self.centralwidget)
        self.UserID_Label.setGeometry(QtCore.QRect(50, 30, 60, 16))
        self.UserID_Label.setObjectName("UserID_Label")
        self.Password_Label = QtWidgets.QLabel(self.centralwidget)
        self.Password_Label.setGeometry(QtCore.QRect(50, 70, 60, 16))
        self.Password_Label.setObjectName("Password_Label")
        self.Password_Input = QtWidgets.QLineEdit(self.centralwidget)
        self.Password_Input.setGeometry(QtCore.QRect(130, 70, 113, 21))
        self.Password_Input.setText("")
        self.Password_Input.setObjectName("Password_Input")
        self.Error_Message_for_password = QtWidgets.QLabel(self.centralwidget)
        self.Error_Message_for_password.setGeometry(
            QtCore.QRect(50, 150, 241, 21))
        self.Error_Message_for_password.setObjectName(
            "Error_Message_for_password")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(180, 110, 111, 31))
        self.checkBox.setObjectName("checkBox")
        self.Error_Message_for_permission = QtWidgets.QLabel(
            self.centralwidget)
        self.Error_Message_for_permission.setGeometry(
            QtCore.QRect(100, 150, 141, 21))
        self.Error_Message_for_permission.setObjectName(
            "Error_Message_for_permission")
        self.Error_Message_for_ID = QtWidgets.QLabel(self.centralwidget)
        self.Error_Message_for_ID.setGeometry(QtCore.QRect(120, 150, 141, 21))
        self.Error_Message_for_ID.setObjectName("Error_Message_for_ID")
        Login.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

        self.modding()

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.Login_Button.setText(_translate("Login", "Login"))
        self.Login_Button.setShortcut(_translate("Login", "Return"))
        self.UserID_Label.setText(_translate("Login", "UserID"))
        self.Password_Label.setText(_translate("Login", "Password"))
        self.Error_Message_for_password.setText(
            _translate("Login", "Wrong Password! Please try again!"))
        self.checkBox.setText(_translate("Login", "Admin mode"))
        self.Error_Message_for_permission.setText(
            _translate("Login", "You are not an Admin!"))
        self.Error_Message_for_ID.setText(
            _translate("Login", "ID doesn\'t exist!"))

    def modding(self):
        # hide the error message
        self.Error_Message_for_password.setHidden(True)
        self.Error_Message_for_permission.setHidden(True)
        self.Error_Message_for_ID.setHidden(True)

        # connect button to function
        self.Login_Button.clicked.connect(lambda: Login_function.check_ID_password_function(
            self.UserID_Input.text(), self.Password_Input.text()))

        # mask the password
        self.Password_Input.setEchoMode(QLineEdit.Password)


class Ui_Info_Editor(object):
    current_user_ID = ''

    def setupUi(self, Info_Editor):
        Info_Editor.setObjectName("Info_Editor")
        Info_Editor.resize(820, 150)
        self.Save_change_button = QtWidgets.QPushButton(Info_Editor)
        self.Save_change_button.setGeometry(QtCore.QRect(320, 110, 161, 32))
        self.Save_change_button.setMinimumSize(QtCore.QSize(161, 32))
        self.Save_change_button.setObjectName("Save_change_button")
        self.Display_table = QtWidgets.QTableWidget(Info_Editor)
        self.Display_table.setGeometry(QtCore.QRect(40, 30, 740, 53))
        self.Display_table.setMinimumSize(QtCore.QSize(0, 0))
        self.Display_table.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.Display_table.setObjectName("Display_table")
        self.Display_table.setColumnCount(7)
        self.Display_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Display_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Display_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Display_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Display_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Display_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Display_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.Display_table.setHorizontalHeaderItem(6, item)
        self.Display_table.horizontalHeader().setVisible(True)
        self.Display_table.horizontalHeader().setCascadingSectionResizes(False)
        self.Display_table.horizontalHeader().setDefaultSectionSize(100)
        self.Display_table.horizontalHeader().setMinimumSectionSize(20)
        self.Display_table.horizontalHeader().setSortIndicatorShown(False)
        self.Display_table.horizontalHeader().setStretchLastSection(True)
        self.Input_Invalid = QtWidgets.QLabel(Info_Editor)
        self.Input_Invalid.setGeometry(QtCore.QRect(510, 110, 81, 31))
        self.Input_Invalid.setObjectName("Input_Invalid")

        self.retranslateUi(Info_Editor)
        QtCore.QMetaObject.connectSlotsByName(Info_Editor)

        self.modding()

    def retranslateUi(self, Info_Editor):
        _translate = QtCore.QCoreApplication.translate
        Info_Editor.setWindowTitle(_translate("Info_Editor", "Info_Editor"))
        self.Save_change_button.setText(
            _translate("Info_Editor", "Save change"))
        item = self.Display_table.horizontalHeaderItem(0)
        item.setText(_translate("Info_Editor", "Checkbox"))
        item = self.Display_table.horizontalHeaderItem(1)
        item.setText(_translate("Info_Editor", "ID"))
        item = self.Display_table.horizontalHeaderItem(2)
        item.setText(_translate("Info_Editor", "Password"))
        item = self.Display_table.horizontalHeaderItem(3)
        item.setText(_translate("Info_Editor", "Permission"))
        item = self.Display_table.horizontalHeaderItem(4)
        item.setText(_translate("Info_Editor", "Name"))
        item = self.Display_table.horizontalHeaderItem(5)
        item.setText(_translate("Info_Editor", "Gender"))
        item = self.Display_table.horizontalHeaderItem(6)
        item.setText(_translate("Info_Editor", "Plate amount"))
        self.Input_Invalid.setText(_translate("Info_Editor", "Invalid input!"))

    def modding(self):
        # hide the error message
        self.Input_Invalid.setHidden(True)

        # connect button to function
        self.Save_change_button.clicked.connect(
            lambda: Info_Editor_function.get_data_from_table())


class Ui_Concentrate_Advance(object):
    current_user_ID = ''

    def setupUi(self, Concentrate_Advance):
        Concentrate_Advance.setObjectName("Concentrate_Advance")
        Concentrate_Advance.resize(1350, 750)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            Concentrate_Advance.sizePolicy().hasHeightForWidth())
        Concentrate_Advance.setSizePolicy(sizePolicy)
        self.Search_Edit_Tab = QtWidgets.QWidget()
        self.Search_Edit_Tab.setObjectName("Search_Edit_Tab")
        self.Delete_User_button = QtWidgets.QPushButton(self.Search_Edit_Tab)
        self.Delete_User_button.setGeometry(QtCore.QRect(20, 580, 161, 32))
        self.Delete_User_button.setMinimumSize(QtCore.QSize(161, 32))
        self.Delete_User_button.setObjectName("Delete_User_button")
        self.Gender_label = QtWidgets.QLabel(self.Search_Edit_Tab)
        self.Gender_label.setGeometry(QtCore.QRect(50, 380, 81, 20))
        self.Gender_label.setMinimumSize(QtCore.QSize(81, 20))
        self.Gender_label.setObjectName("Gender_label")
        self.Show_all_button = QtWidgets.QPushButton(self.Search_Edit_Tab)
        self.Show_all_button.setGeometry(QtCore.QRect(20, 540, 161, 32))
        self.Show_all_button.setMinimumSize(QtCore.QSize(161, 32))
        self.Show_all_button.setObjectName("Show_all_button")
        self.Add_User_button = QtWidgets.QPushButton(self.Search_Edit_Tab)
        self.Add_User_button.setGeometry(QtCore.QRect(20, 620, 161, 32))
        self.Add_User_button.setMinimumSize(QtCore.QSize(161, 32))
        self.Add_User_button.setObjectName("Add_User_button")
        self.line_3 = QtWidgets.QFrame(self.Search_Edit_Tab)
        self.line_3.setGeometry(QtCore.QRect(60, 350, 201, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.Name_label = QtWidgets.QLabel(self.Search_Edit_Tab)
        self.Name_label.setGeometry(QtCore.QRect(50, 140, 61, 16))
        self.Name_label.setMinimumSize(QtCore.QSize(61, 16))
        self.Name_label.setObjectName("Name_label")
        self.Female_button = QtWidgets.QRadioButton(self.Search_Edit_Tab)
        self.Female_button.setGeometry(QtCore.QRect(140, 410, 100, 20))
        self.Female_button.setMinimumSize(QtCore.QSize(100, 20))
        self.Female_button.setObjectName("Female_button")
        self.buttongroup_gender = QtWidgets.QButtonGroup(Concentrate_Advance)
        self.buttongroup_gender.setObjectName("buttongroup_gender")
        self.buttongroup_gender.addButton(self.Female_button)
        self.line_2 = QtWidgets.QFrame(self.Search_Edit_Tab)
        self.line_2.setGeometry(QtCore.QRect(60, 220, 201, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.Permission_button = QtWidgets.QPushButton(self.Search_Edit_Tab)
        self.Permission_button.setGeometry(QtCore.QRect(100, 310, 160, 30))
        self.Permission_button.setMinimumSize(QtCore.QSize(140, 30))
        self.Permission_button.setObjectName("Permission_button")
        self.ID_input = QtWidgets.QLineEdit(self.Search_Edit_Tab)
        self.ID_input.setGeometry(QtCore.QRect(120, 20, 141, 21))
        self.ID_input.setMinimumSize(QtCore.QSize(141, 21))
        self.ID_input.setText("")
        self.ID_input.setObjectName("ID_input")
        self.line_4 = QtWidgets.QFrame(self.Search_Edit_Tab)
        self.line_4.setGeometry(QtCore.QRect(60, 500, 201, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.Name_search_button = QtWidgets.QPushButton(self.Search_Edit_Tab)
        self.Name_search_button.setGeometry(QtCore.QRect(120, 180, 140, 30))
        self.Name_search_button.setMinimumSize(QtCore.QSize(140, 30))
        self.Name_search_button.setObjectName("Name_search_button")
        self.Others_button = QtWidgets.QRadioButton(self.Search_Edit_Tab)
        self.Others_button.setGeometry(QtCore.QRect(140, 440, 100, 20))
        self.Others_button.setMinimumSize(QtCore.QSize(100, 20))
        self.Others_button.setObjectName("Others_button")
        self.buttongroup_gender.addButton(self.Others_button)
        self.ID_search_button = QtWidgets.QPushButton(self.Search_Edit_Tab)
        self.ID_search_button.setGeometry(QtCore.QRect(120, 60, 140, 30))
        self.ID_search_button.setMinimumSize(QtCore.QSize(0, 0))
        self.ID_search_button.setObjectName("ID_search_button")
        self.line = QtWidgets.QFrame(self.Search_Edit_Tab)
        self.line.setGeometry(QtCore.QRect(60, 100, 200, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.Admin_button = QtWidgets.QRadioButton(self.Search_Edit_Tab)
        self.Admin_button.setGeometry(QtCore.QRect(140, 280, 100, 20))
        self.Admin_button.setMinimumSize(QtCore.QSize(100, 20))
        self.Admin_button.setObjectName("Admin_button")
        self.buttongroup_permission = QtWidgets.QButtonGroup(
            Concentrate_Advance)
        self.buttongroup_permission.setObjectName("buttongroup_permission")
        self.buttongroup_permission.addButton(self.Admin_button)
        self.Edit_error_message = QtWidgets.QLabel(self.Search_Edit_Tab)
        self.Edit_error_message.setGeometry(QtCore.QRect(200, 665, 81, 21))
        self.Edit_error_message.setMinimumSize(QtCore.QSize(71, 16))
        self.Edit_error_message.setObjectName("Edit_error_message")
        self.ID_label = QtWidgets.QLabel(self.Search_Edit_Tab)
        self.ID_label.setGeometry(QtCore.QRect(50, 20, 61, 16))
        self.ID_label.setMinimumSize(QtCore.QSize(61, 16))
        self.ID_label.setObjectName("ID_label")
        self.Gender_button = QtWidgets.QPushButton(self.Search_Edit_Tab)
        self.Gender_button.setGeometry(QtCore.QRect(100, 460, 160, 30))
        self.Gender_button.setMinimumSize(QtCore.QSize(160, 30))
        self.Gender_button.setObjectName("Gender_button")
        self.Male_button = QtWidgets.QRadioButton(self.Search_Edit_Tab)
        self.Male_button.setGeometry(QtCore.QRect(140, 380, 100, 20))
        self.Male_button.setMinimumSize(QtCore.QSize(100, 20))
        self.Male_button.setObjectName("Male_button")
        self.buttongroup_gender.addButton(self.Male_button)
        self.Permission_label = QtWidgets.QLabel(self.Search_Edit_Tab)
        self.Permission_label.setGeometry(QtCore.QRect(50, 250, 81, 20))
        self.Permission_label.setMinimumSize(QtCore.QSize(81, 20))
        self.Permission_label.setObjectName("Permission_label")
        self.User_button = QtWidgets.QRadioButton(self.Search_Edit_Tab)
        self.User_button.setGeometry(QtCore.QRect(140, 250, 100, 20))
        self.User_button.setMinimumSize(QtCore.QSize(100, 20))
        self.User_button.setObjectName("User_button")
        self.buttongroup_permission.addButton(self.User_button)
        self.Save_change_button = QtWidgets.QPushButton(self.Search_Edit_Tab)
        self.Save_change_button.setGeometry(QtCore.QRect(20, 660, 161, 32))
        self.Save_change_button.setMinimumSize(QtCore.QSize(161, 32))
        self.Save_change_button.setObjectName("Save_change_button")
        self.Name_input = QtWidgets.QLineEdit(self.Search_Edit_Tab)
        self.Name_input.setGeometry(QtCore.QRect(120, 140, 141, 21))
        self.Name_input.setMinimumSize(QtCore.QSize(141, 21))
        self.Name_input.setText("")
        self.Name_input.setObjectName("Name_input")
        self.Display_table = QtWidgets.QTableWidget(self.Search_Edit_Tab)
        self.Display_table.setGeometry(QtCore.QRect(320, 10, 1000, 623))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Display_table.sizePolicy().hasHeightForWidth())
        self.Display_table.setSizePolicy(sizePolicy)
        self.Display_table.setMinimumSize(QtCore.QSize(800, 350))
        self.Display_table.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.Display_table.setObjectName("Display_table")
        self.Display_table.setColumnCount(7)
        self.Display_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Display_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Display_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Display_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Display_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Display_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Display_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.Display_table.setHorizontalHeaderItem(6, item)
        self.Display_table.horizontalHeader().setVisible(True)
        self.Display_table.horizontalHeader().setCascadingSectionResizes(False)
        self.Display_table.horizontalHeader().setDefaultSectionSize(100)
        self.Display_table.horizontalHeader().setMinimumSectionSize(20)
        self.Display_table.horizontalHeader().setSortIndicatorShown(False)
        self.Display_table.horizontalHeader().setStretchLastSection(True)
        self.User_info_pages = QtWidgets.QSpinBox(self.Search_Edit_Tab)
        self.User_info_pages.setGeometry(QtCore.QRect(700, 660, 81, 24))
        self.User_info_pages.setKeyboardTracking(False)
        self.User_info_pages.setObjectName("User_info_pages")
        self.ID_input.raise_()
        self.Delete_User_button.raise_()
        self.Gender_label.raise_()
        self.Show_all_button.raise_()
        self.Add_User_button.raise_()
        self.line_3.raise_()
        self.Name_label.raise_()
        self.Female_button.raise_()
        self.line_2.raise_()
        self.Permission_button.raise_()
        self.line_4.raise_()
        self.Name_search_button.raise_()
        self.Others_button.raise_()
        self.ID_search_button.raise_()
        self.line.raise_()
        self.Admin_button.raise_()
        self.Edit_error_message.raise_()
        self.ID_label.raise_()
        self.Gender_button.raise_()
        self.Male_button.raise_()
        self.Permission_label.raise_()
        self.User_button.raise_()
        self.Save_change_button.raise_()
        self.Name_input.raise_()
        self.User_info_pages.raise_()
        self.Display_table.raise_()
        Concentrate_Advance.addTab(self.Search_Edit_Tab, "")
        self.Login_History_Tab = QtWidgets.QWidget()
        self.Login_History_Tab.setObjectName("Login_History_Tab")
        self.ID_input_login_history = QtWidgets.QLineEdit(
            self.Login_History_Tab)
        self.ID_input_login_history.setGeometry(QtCore.QRect(120, 20, 141, 21))
        self.ID_input_login_history.setMinimumSize(QtCore.QSize(141, 21))
        self.ID_input_login_history.setText("")
        self.ID_input_login_history.setObjectName("ID_input_login_history")
        self.ID_label_login_history = QtWidgets.QLabel(self.Login_History_Tab)
        self.ID_label_login_history.setGeometry(QtCore.QRect(50, 20, 61, 16))
        self.ID_label_login_history.setMinimumSize(QtCore.QSize(61, 16))
        self.ID_label_login_history.setObjectName("ID_label_login_history")
        self.Password_doesnt_match_ID_button = QtWidgets.QRadioButton(
            self.Login_History_Tab)
        self.Password_doesnt_match_ID_button.setGeometry(
            QtCore.QRect(50, 290, 211, 20))
        self.Password_doesnt_match_ID_button.setMinimumSize(
            QtCore.QSize(100, 20))
        self.Password_doesnt_match_ID_button.setObjectName(
            "Password_doesnt_match_ID_button")
        self.buttonGroup_fail_type = QtWidgets.QButtonGroup(
            Concentrate_Advance)
        self.buttonGroup_fail_type.setObjectName("buttonGroup_fail_type")
        self.buttonGroup_fail_type.addButton(
            self.Password_doesnt_match_ID_button)
        self.Success_button = QtWidgets.QRadioButton(self.Login_History_Tab)
        self.Success_button.setGeometry(QtCore.QRect(50, 140, 100, 20))
        self.Success_button.setMinimumSize(QtCore.QSize(100, 20))
        self.Success_button.setObjectName("Success_button")
        self.ID_doesnt_exist_button = QtWidgets.QRadioButton(
            self.Login_History_Tab)
        self.ID_doesnt_exist_button.setGeometry(QtCore.QRect(50, 260, 121, 20))
        self.ID_doesnt_exist_button.setMinimumSize(QtCore.QSize(100, 20))
        self.ID_doesnt_exist_button.setObjectName("ID_doesnt_exist_button")
        self.buttonGroup_fail_type.addButton(self.ID_doesnt_exist_button)
        self.ID_search_button_login_history = QtWidgets.QPushButton(
            self.Login_History_Tab)
        self.ID_search_button_login_history.setGeometry(
            QtCore.QRect(120, 60, 140, 30))
        self.ID_search_button_login_history.setMinimumSize(QtCore.QSize(0, 0))
        self.ID_search_button_login_history.setObjectName(
            "ID_search_button_login_history")
        self.Display_Login_info = QtWidgets.QTableWidget(
            self.Login_History_Tab)
        self.Display_Login_info.setGeometry(QtCore.QRect(320, 10, 1000, 623))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Display_Login_info.sizePolicy().hasHeightForWidth())
        self.Display_Login_info.setSizePolicy(sizePolicy)
        self.Display_Login_info.setMinimumSize(QtCore.QSize(800, 360))
        self.Display_Login_info.setObjectName("Display_Login_info")
        self.Display_Login_info.setColumnCount(4)
        self.Display_Login_info.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Display_Login_info.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Display_Login_info.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Display_Login_info.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Display_Login_info.setHorizontalHeaderItem(3, item)
        self.Display_Login_info.horizontalHeader().setCascadingSectionResizes(False)
        self.Display_Login_info.horizontalHeader().setDefaultSectionSize(100)
        self.Display_Login_info.horizontalHeader().setStretchLastSection(True)
        self.Fail_button = QtWidgets.QRadioButton(self.Login_History_Tab)
        self.Fail_button.setGeometry(QtCore.QRect(150, 140, 100, 20))
        self.Fail_button.setMinimumSize(QtCore.QSize(100, 20))
        self.Fail_button.setObjectName("Fail_button")
        self.Fail_type_button = QtWidgets.QPushButton(self.Login_History_Tab)
        self.Fail_type_button.setGeometry(QtCore.QRect(120, 350, 140, 30))
        self.Fail_type_button.setMinimumSize(QtCore.QSize(140, 30))
        self.Fail_type_button.setObjectName("Fail_type_button")
        self.Status_show_button = QtWidgets.QPushButton(self.Login_History_Tab)
        self.Status_show_button.setGeometry(QtCore.QRect(120, 180, 140, 30))
        self.Status_show_button.setMinimumSize(QtCore.QSize(140, 30))
        self.Status_show_button.setObjectName("Status_show_button")
        self.Show_all_button_login_history = QtWidgets.QPushButton(
            self.Login_History_Tab)
        self.Show_all_button_login_history.setGeometry(
            QtCore.QRect(120, 530, 140, 30))
        self.Show_all_button_login_history.setMinimumSize(
            QtCore.QSize(140, 30))
        self.Show_all_button_login_history.setObjectName(
            "Show_all_button_login_history")
        self.line_5 = QtWidgets.QFrame(self.Login_History_Tab)
        self.line_5.setGeometry(QtCore.QRect(60, 100, 200, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.Login_History_Tab)
        self.line_6.setGeometry(QtCore.QRect(60, 220, 200, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.Login_History_Tab)
        self.line_7.setGeometry(QtCore.QRect(60, 380, 200, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.User_enter_advance_button = QtWidgets.QRadioButton(
            self.Login_History_Tab)
        self.User_enter_advance_button.setGeometry(
            QtCore.QRect(50, 320, 241, 20))
        self.User_enter_advance_button.setMinimumSize(QtCore.QSize(100, 20))
        self.User_enter_advance_button.setObjectName(
            "User_enter_advance_button")
        self.buttonGroup_fail_type.addButton(self.User_enter_advance_button)
        self.Success_type_button = QtWidgets.QPushButton(
            self.Login_History_Tab)
        self.Success_type_button.setGeometry(QtCore.QRect(120, 470, 161, 32))
        self.Success_type_button.setMinimumSize(QtCore.QSize(141, 32))
        self.Success_type_button.setObjectName("Success_type_button")
        self.Normal_login_button = QtWidgets.QRadioButton(
            self.Login_History_Tab)
        self.Normal_login_button.setGeometry(QtCore.QRect(50, 410, 121, 20))
        self.Normal_login_button.setMinimumSize(QtCore.QSize(100, 20))
        self.Normal_login_button.setObjectName("Normal_login_button")
        self.buttongroup_success_type = QtWidgets.QButtonGroup(
            Concentrate_Advance)
        self.buttongroup_success_type.setObjectName("buttongroup_success_type")
        self.buttongroup_success_type.addButton(self.Normal_login_button)
        self.Advance_login_button = QtWidgets.QRadioButton(
            self.Login_History_Tab)
        self.Advance_login_button.setGeometry(QtCore.QRect(50, 440, 121, 20))
        self.Advance_login_button.setMinimumSize(QtCore.QSize(100, 20))
        self.Advance_login_button.setObjectName("Advance_login_button")
        self.buttongroup_success_type.addButton(self.Advance_login_button)
        self.line_8 = QtWidgets.QFrame(self.Login_History_Tab)
        self.line_8.setGeometry(QtCore.QRect(60, 500, 200, 20))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.Login_History_Pages = QtWidgets.QSpinBox(self.Login_History_Tab)
        self.Login_History_Pages.setGeometry(QtCore.QRect(700, 660, 81, 24))
        self.Login_History_Pages.setKeyboardTracking(False)
        self.Login_History_Pages.setObjectName("Login_History_Pages")
        self.ID_input_login_history.raise_()
        self.Password_doesnt_match_ID_button.raise_()
        self.Success_button.raise_()
        self.ID_label_login_history.raise_()
        self.ID_doesnt_exist_button.raise_()
        self.ID_search_button_login_history.raise_()
        self.Fail_button.raise_()
        self.Fail_type_button.raise_()
        self.Status_show_button.raise_()
        self.Show_all_button_login_history.raise_()
        self.line_5.raise_()
        self.line_6.raise_()
        self.line_7.raise_()
        self.User_enter_advance_button.raise_()
        self.Success_type_button.raise_()
        self.Normal_login_button.raise_()
        self.Advance_login_button.raise_()
        self.line_8.raise_()
        self.Login_History_Pages.raise_()
        self.Display_Login_info.raise_()
        Concentrate_Advance.addTab(self.Login_History_Tab, "")
        self.Plate_Scan_Tab = QtWidgets.QWidget()
        self.Plate_Scan_Tab.setObjectName("Plate_Scan_Tab")
        self.ID_input_Plate_Info = QtWidgets.QLineEdit(self.Plate_Scan_Tab)
        self.ID_input_Plate_Info.setGeometry(QtCore.QRect(120, 20, 141, 21))
        self.ID_input_Plate_Info.setMinimumSize(QtCore.QSize(141, 21))
        self.ID_input_Plate_Info.setText("")
        self.ID_input_Plate_Info.setObjectName("ID_input_Plate_Info")
        self.Display_Plate_Info = QtWidgets.QTableWidget(self.Plate_Scan_Tab)
        self.Display_Plate_Info.setGeometry(QtCore.QRect(320, 10, 1000, 623))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Display_Plate_Info.sizePolicy().hasHeightForWidth())
        self.Display_Plate_Info.setSizePolicy(sizePolicy)
        self.Display_Plate_Info.setMinimumSize(QtCore.QSize(800, 360))
        self.Display_Plate_Info.setObjectName("Display_Plate_Info")
        self.Display_Plate_Info.setColumnCount(6)
        self.Display_Plate_Info.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Display_Plate_Info.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Display_Plate_Info.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Display_Plate_Info.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Display_Plate_Info.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Display_Plate_Info.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Display_Plate_Info.setHorizontalHeaderItem(5, item)
        self.Display_Plate_Info.horizontalHeader().setCascadingSectionResizes(False)
        self.Display_Plate_Info.horizontalHeader().setDefaultSectionSize(10)
        self.Display_Plate_Info.horizontalHeader().setStretchLastSection(True)
        self.Show_all_button_Plate_Info = QtWidgets.QPushButton(
            self.Plate_Scan_Tab)
        self.Show_all_button_Plate_Info.setGeometry(
            QtCore.QRect(20, 370, 180, 30))
        self.Show_all_button_Plate_Info.setMinimumSize(QtCore.QSize(150, 30))
        self.Show_all_button_Plate_Info.setObjectName(
            "Show_all_button_Plate_Info")
        self.Plate_ID_label_Plate_Info = QtWidgets.QLabel(self.Plate_Scan_Tab)
        self.Plate_ID_label_Plate_Info.setGeometry(
            QtCore.QRect(50, 140, 61, 16))
        self.Plate_ID_label_Plate_Info.setMinimumSize(QtCore.QSize(61, 16))
        self.Plate_ID_label_Plate_Info.setObjectName(
            "Plate_ID_label_Plate_Info")
        self.ID_search_button_Plate_Info = QtWidgets.QPushButton(
            self.Plate_Scan_Tab)
        self.ID_search_button_Plate_Info.setGeometry(
            QtCore.QRect(120, 60, 140, 30))
        self.ID_search_button_Plate_Info.setMinimumSize(QtCore.QSize(0, 0))
        self.ID_search_button_Plate_Info.setObjectName(
            "ID_search_button_Plate_Info")
        self.Plate_ID_search_button_Plate_Info = QtWidgets.QPushButton(
            self.Plate_Scan_Tab)
        self.Plate_ID_search_button_Plate_Info.setGeometry(
            QtCore.QRect(120, 180, 140, 30))
        self.Plate_ID_search_button_Plate_Info.setMinimumSize(
            QtCore.QSize(140, 30))
        self.Plate_ID_search_button_Plate_Info.setObjectName(
            "Plate_ID_search_button_Plate_Info")
        self.ID_label_Plate_Info = QtWidgets.QLabel(self.Plate_Scan_Tab)
        self.ID_label_Plate_Info.setGeometry(QtCore.QRect(50, 20, 61, 16))
        self.ID_label_Plate_Info.setMinimumSize(QtCore.QSize(61, 16))
        self.ID_label_Plate_Info.setObjectName("ID_label_Plate_Info")
        self.line_9 = QtWidgets.QFrame(self.Plate_Scan_Tab)
        self.line_9.setGeometry(QtCore.QRect(60, 220, 201, 20))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.Plate_Scan_Tab)
        self.line_10.setGeometry(QtCore.QRect(60, 100, 200, 20))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.Plate_ID_input_Plate_Info = QtWidgets.QLineEdit(
            self.Plate_Scan_Tab)
        self.Plate_ID_input_Plate_Info.setGeometry(
            QtCore.QRect(120, 140, 141, 21))
        self.Plate_ID_input_Plate_Info.setMinimumSize(QtCore.QSize(141, 21))
        self.Plate_ID_input_Plate_Info.setText("")
        self.Plate_ID_input_Plate_Info.setObjectName(
            "Plate_ID_input_Plate_Info")
        self.Availability_button = QtWidgets.QPushButton(self.Plate_Scan_Tab)
        self.Availability_button.setGeometry(QtCore.QRect(110, 310, 151, 30))
        self.Availability_button.setMinimumSize(QtCore.QSize(140, 30))
        self.Availability_button.setObjectName("Availability_button")
        self.Available_FALSE = QtWidgets.QRadioButton(self.Plate_Scan_Tab)
        self.Available_FALSE.setGeometry(QtCore.QRect(110, 250, 100, 20))
        self.Available_FALSE.setMinimumSize(QtCore.QSize(100, 20))
        self.Available_FALSE.setObjectName("Available_FALSE")
        self.Available_TRUE = QtWidgets.QRadioButton(self.Plate_Scan_Tab)
        self.Available_TRUE.setGeometry(QtCore.QRect(110, 280, 100, 20))
        self.Available_TRUE.setMinimumSize(QtCore.QSize(100, 20))
        self.Available_TRUE.setObjectName("Available_TRUE")
        self.line_11 = QtWidgets.QFrame(self.Plate_Scan_Tab)
        self.line_11.setGeometry(QtCore.QRect(60, 340, 180, 30))
        self.line_11.setMinimumSize(QtCore.QSize(150, 30))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.Assign_plate_to_user = QtWidgets.QPushButton(self.Plate_Scan_Tab)
        self.Assign_plate_to_user.setGeometry(QtCore.QRect(20, 450, 180, 30))
        self.Assign_plate_to_user.setMinimumSize(QtCore.QSize(150, 30))
        self.Assign_plate_to_user.setObjectName("Assign_plate_to_user")
        self.Deassign_plate_from_user = QtWidgets.QPushButton(
            self.Plate_Scan_Tab)
        self.Deassign_plate_from_user.setGeometry(
            QtCore.QRect(20, 410, 180, 30))
        self.Deassign_plate_from_user.setMinimumSize(QtCore.QSize(150, 30))
        self.Deassign_plate_from_user.setObjectName("Deassign_plate_from_user")
        self.Add_new_plate = QtWidgets.QPushButton(self.Plate_Scan_Tab)
        self.Add_new_plate.setGeometry(QtCore.QRect(20, 490, 180, 30))
        self.Add_new_plate.setMinimumSize(QtCore.QSize(150, 30))
        self.Add_new_plate.setObjectName("Add_new_plate")
        self.Remove_plate = QtWidgets.QPushButton(self.Plate_Scan_Tab)
        self.Remove_plate.setGeometry(QtCore.QRect(20, 530, 180, 30))
        self.Remove_plate.setMinimumSize(QtCore.QSize(150, 30))
        self.Remove_plate.setObjectName("Remove_plate")
        self.Assign_fail_label = QtWidgets.QLabel(self.Plate_Scan_Tab)
        self.Assign_fail_label.setGeometry(QtCore.QRect(220, 450, 91, 31))
        self.Assign_fail_label.setMinimumSize(QtCore.QSize(61, 16))
        self.Assign_fail_label.setObjectName("Assign_fail_label")
        self.Assign_success_label = QtWidgets.QLabel(self.Plate_Scan_Tab)
        self.Assign_success_label.setGeometry(QtCore.QRect(220, 450, 91, 31))
        self.Assign_success_label.setMinimumSize(QtCore.QSize(61, 16))
        self.Assign_success_label.setObjectName("Assign_success_label")
        self.Plate_info_pages = QtWidgets.QSpinBox(self.Plate_Scan_Tab)
        self.Plate_info_pages.setGeometry(QtCore.QRect(700, 660, 81, 24))
        self.Plate_info_pages.setKeyboardTracking(False)
        self.Plate_info_pages.setObjectName("Plate_info_pages")
        self.ID_input_Plate_Info.raise_()
        self.Show_all_button_Plate_Info.raise_()
        self.Plate_ID_label_Plate_Info.raise_()
        self.ID_search_button_Plate_Info.raise_()
        self.Plate_ID_search_button_Plate_Info.raise_()
        self.ID_label_Plate_Info.raise_()
        self.line_9.raise_()
        self.line_10.raise_()
        self.Plate_ID_input_Plate_Info.raise_()
        self.Availability_button.raise_()
        self.Available_FALSE.raise_()
        self.Available_TRUE.raise_()
        self.line_11.raise_()
        self.Assign_plate_to_user.raise_()
        self.Deassign_plate_from_user.raise_()
        self.Add_new_plate.raise_()
        self.Remove_plate.raise_()
        self.Assign_fail_label.raise_()
        self.Assign_success_label.raise_()
        self.Plate_info_pages.raise_()
        self.Display_Plate_Info.raise_()
        Concentrate_Advance.addTab(self.Plate_Scan_Tab, "")

        self.retranslateUi(Concentrate_Advance)
        Concentrate_Advance.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Concentrate_Advance)
        self.modding()

    def retranslateUi(self, Concentrate_Advance):
        _translate = QtCore.QCoreApplication.translate
        Concentrate_Advance.setWindowTitle(_translate(
            "Concentrate_Advance", "Concentrate_Advance"))
        self.Delete_User_button.setText(_translate(
            "Concentrate_Advance", "Delete a User"))
        self.Gender_label.setText(_translate("Concentrate_Advance", "Gender"))
        self.Show_all_button.setText(_translate(
            "Concentrate_Advance", "Show All Users"))
        self.Add_User_button.setText(_translate(
            "Concentrate_Advance", "Add a User"))
        self.Name_label.setText(_translate("Concentrate_Advance", "Name"))
        self.Female_button.setText(_translate("Concentrate_Advance", "Female"))
        self.Permission_button.setText(_translate(
            "Concentrate_Advance", "Search by Permission"))
        self.Name_search_button.setText(_translate(
            "Concentrate_Advance", "Search by Name"))
        self.Others_button.setText(_translate("Concentrate_Advance", "Others"))
        self.ID_search_button.setText(_translate(
            "Concentrate_Advance", "Search by ID"))
        self.Admin_button.setText(_translate("Concentrate_Advance", "Admin"))
        self.Edit_error_message.setText(_translate(
            "Concentrate_Advance", "Invalid input!"))
        self.ID_label.setText(_translate("Concentrate_Advance", "ID"))
        self.Gender_button.setText(_translate(
            "Concentrate_Advance", "Search by Gender"))
        self.Male_button.setText(_translate("Concentrate_Advance", "Male"))
        self.Permission_label.setText(_translate(
            "Concentrate_Advance", "Permission"))
        self.User_button.setText(_translate("Concentrate_Advance", "User"))
        self.Save_change_button.setText(
            _translate("Concentrate_Advance", "Save change"))
        item = self.Display_table.horizontalHeaderItem(0)
        item.setText(_translate("Concentrate_Advance", "Checkbox"))
        item = self.Display_table.horizontalHeaderItem(1)
        item.setText(_translate("Concentrate_Advance", "ID"))
        item = self.Display_table.horizontalHeaderItem(2)
        item.setText(_translate("Concentrate_Advance", "Password"))
        item = self.Display_table.horizontalHeaderItem(3)
        item.setText(_translate("Concentrate_Advance", "Permission"))
        item = self.Display_table.horizontalHeaderItem(4)
        item.setText(_translate("Concentrate_Advance", "Name"))
        item = self.Display_table.horizontalHeaderItem(5)
        item.setText(_translate("Concentrate_Advance", "Gender"))
        item = self.Display_table.horizontalHeaderItem(6)
        item.setText(_translate("Concentrate_Advance", "Plate amount"))
        Concentrate_Advance.setTabText(Concentrate_Advance.indexOf(
            self.Search_Edit_Tab), _translate("Concentrate_Advance", "User info"))
        self.Password_doesnt_match_ID_button.setText(_translate(
            "Concentrate_Advance", "Password doesn\'t match ID"))
        self.Success_button.setText(
            _translate("Concentrate_Advance", "Success"))
        self.ID_label_login_history.setText(
            _translate("Concentrate_Advance", "ID"))
        self.ID_doesnt_exist_button.setText(_translate(
            "Concentrate_Advance", "ID doesn\'t exist"))
        self.ID_search_button_login_history.setText(
            _translate("Concentrate_Advance", "Search by ID"))
        item = self.Display_Login_info.horizontalHeaderItem(0)
        item.setText(_translate("Concentrate_Advance", "Login_ID"))
        item = self.Display_Login_info.horizontalHeaderItem(1)
        item.setText(_translate("Concentrate_Advance", "Login_Time"))
        item = self.Display_Login_info.horizontalHeaderItem(2)
        item.setText(_translate("Concentrate_Advance", "Login_Status"))
        item = self.Display_Login_info.horizontalHeaderItem(3)
        item.setText(_translate("Concentrate_Advance", "Specific_type"))
        self.Fail_button.setText(_translate("Concentrate_Advance", "Fail "))
        self.Fail_type_button.setText(_translate(
            "Concentrate_Advance", "Show by Fail type"))
        self.Status_show_button.setText(_translate(
            "Concentrate_Advance", "Show by Status"))
        self.Show_all_button_login_history.setText(
            _translate("Concentrate_Advance", "Show All"))
        self.User_enter_advance_button.setText(_translate(
            "Concentrate_Advance", "Normal user entered Advance mode"))
        self.Success_type_button.setText(_translate(
            "Concentrate_Advance", "Show by Success type"))
        self.Normal_login_button.setText(
            _translate("Concentrate_Advance", "Normal login"))
        self.Advance_login_button.setText(
            _translate("Concentrate_Advance", "Advance login"))
        Concentrate_Advance.setTabText(Concentrate_Advance.indexOf(
            self.Login_History_Tab), _translate("Concentrate_Advance", "Login History"))
        item = self.Display_Plate_Info.horizontalHeaderItem(0)
        item.setText(_translate("Concentrate_Advance", "Checkbox"))
        item = self.Display_Plate_Info.horizontalHeaderItem(1)
        item.setText(_translate("Concentrate_Advance", "Plate_ID"))
        item = self.Display_Plate_Info.horizontalHeaderItem(2)
        item.setText(_translate(
            "Concentrate_Advance", "Last_Assigned_User_ID"))
        item = self.Display_Plate_Info.horizontalHeaderItem(3)
        item.setText(_translate("Concentrate_Advance", "Available_for_assign"))
        item = self.Display_Plate_Info.horizontalHeaderItem(4)
        item.setText(_translate("Concentrate_Advance", "Last_Assign_Time"))
        item = self.Display_Plate_Info.horizontalHeaderItem(5)
        item.setText(_translate("Concentrate_Advance", "Last_Deassign_Time"))
        self.Show_all_button_Plate_Info.setText(
            _translate("Concentrate_Advance", "Show All"))
        self.Plate_ID_label_Plate_Info.setText(
            _translate("Concentrate_Advance", "Plate ID"))
        self.ID_search_button_Plate_Info.setText(
            _translate("Concentrate_Advance", "Search by ID"))
        self.Plate_ID_search_button_Plate_Info.setText(
            _translate("Concentrate_Advance", "Search by Plate ID"))
        self.ID_label_Plate_Info.setText(
            _translate("Concentrate_Advance", "ID"))
        self.Availability_button.setText(_translate(
            "Concentrate_Advance", "Show by Availability"))
        self.Available_FALSE.setText(
            _translate("Concentrate_Advance", "FALSE"))
        self.Available_TRUE.setText(_translate("Concentrate_Advance", "TRUE"))
        self.Assign_plate_to_user.setText(_translate(
            "Concentrate_Advance", "Assign plate to user"))
        self.Deassign_plate_from_user.setText(
            _translate("Concentrate_Advance", "Deassign plate"))
        self.Add_new_plate.setText(_translate(
            "Concentrate_Advance", "Add new plate"))
        self.Remove_plate.setText(_translate(
            "Concentrate_Advance", "Remove plate"))
        self.Assign_fail_label.setText(
            _translate("Concentrate_Advance", "Failed!"))
        self.Assign_success_label.setText(
            _translate("Concentrate_Advance", "Success"))
        Concentrate_Advance.setTabText(Concentrate_Advance.indexOf(
            self.Plate_Scan_Tab), _translate("Concentrate_Advance", "Plate Scan"))

    def modding(self):

        # Modding for Search/Edit

        # adjust column size
        header = self.Display_table.horizontalHeader()
        for i in range(5):
            header.setSectionResizeMode(
                i, QtWidgets.QHeaderView.ResizeToContents)

        # hide the error message
        self.Edit_error_message.setHidden(True)

        # connect button to function
        self.Show_all_button.clicked.connect(
            lambda: Search_Edit_function.set_current_search_type("all"))
        self.Show_all_button.clicked.connect(
            lambda: Search_Edit_function.show_user(0))
        self.ID_search_button.clicked.connect(
            lambda: Search_Edit_function.set_current_search_type("id"))
        self.ID_search_button.clicked.connect(
            lambda: Search_Edit_function.show_user(0))
        self.Name_search_button.clicked.connect(
            lambda: Search_Edit_function.set_current_search_type("name"))
        self.Name_search_button.clicked.connect(
            lambda: Search_Edit_function.show_user(0))
        self.Gender_button.clicked.connect(
            lambda: Search_Edit_function.set_current_search_type("gender"))
        self.Gender_button.clicked.connect(
            lambda: Search_Edit_function.show_user(0))
        self.Permission_button.clicked.connect(
            lambda: Search_Edit_function.set_current_search_type("permission"))
        self.Permission_button.clicked.connect(
            lambda: Search_Edit_function.show_user(0))
        self.Save_change_button.clicked.connect(
            lambda: Search_Edit_function.get_data_from_table())
        self.Delete_User_button.clicked.connect(
            lambda: Search_Edit_function.show_delete_confirm())
        self.Add_User_button.clicked.connect(
            lambda: Search_Edit_function.open_Register_window())

        self.User_info_pages.valueChanged.connect(
            lambda: Search_Edit_function.show_user(self.User_info_pages.value()))

        # get the maximum page number
        Search_Edit_function.set_user_info_pages_maximum(None)

        # set the maximum number for spinbox
        self.User_info_pages.setMaximum(2147483647)

        # show all info initially
        Search_Edit_function.show_user(0)

    # Modding for Login History
        # adjust column size
        header = self.Display_Login_info.horizontalHeader()
        for i in range(3):
            header.setSectionResizeMode(
                i, QtWidgets.QHeaderView.ResizeToContents)

        # connect button to function
        self.Show_all_button_login_history.clicked.connect(
            lambda: Login_History_function.set_current_search_type("all"))
        self.Show_all_button_login_history.clicked.connect(
            lambda: Login_History_function.show_login_history(0))
        self.ID_search_button_login_history.clicked.connect(
            lambda: Login_History_function.set_current_search_type("id"))
        self.ID_search_button_login_history.clicked.connect(
            lambda: Login_History_function.show_login_history(0))
        self.Status_show_button.clicked.connect(
            lambda: Login_History_function.set_current_search_type("status"))
        self.Status_show_button.clicked.connect(
            lambda: Login_History_function.show_login_history(0))
        self.Fail_type_button.clicked.connect(
            lambda: Login_History_function.set_current_search_type("specific_type_fail"))
        self.Fail_type_button.clicked.connect(
            lambda: Login_History_function.show_login_history(0))
        self.Success_type_button.clicked.connect(
            lambda: Login_History_function.set_current_search_type("specific_type_success"))
        self.Success_type_button.clicked.connect(
            lambda: Login_History_function.show_login_history(0))

        self.Login_History_Pages.valueChanged.connect(
            lambda: Login_History_function.show_login_history(self.Login_History_Pages.value()))

        # get the maximum page number
        Login_History_function.set_login_history_pages_maximum(None)

        # set the maximum number for spinbox
        self.Login_History_Pages.setMaximum(2147483647)

        # show all info initially
        Login_History_function.show_login_history(0)

        # let table be read only
        self.Display_Login_info.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)

    # Modding for plate info
        # adjust column size
        header = self.Display_Plate_Info.horizontalHeader()
        for i in range(5):
            header.setSectionResizeMode(
                i, QtWidgets.QHeaderView.ResizeToContents)

        # connect button to function

        self.Show_all_button_Plate_Info.clicked.connect(
            lambda: Plate_Info_function.set_current_search_type("all"))
        self.Show_all_button_Plate_Info.clicked.connect(
            lambda: Plate_Info_function.show_plate_info(0))
        self.ID_search_button_Plate_Info.clicked.connect(
            lambda: Plate_Info_function.set_current_search_type("user_id"))
        self.ID_search_button_Plate_Info.clicked.connect(
            lambda: Plate_Info_function.show_plate_info(0))
        self.Plate_ID_search_button_Plate_Info.clicked.connect(
            lambda: Plate_Info_function.set_current_search_type("plate_id"))
        self.Plate_ID_search_button_Plate_Info.clicked.connect(
            lambda: Plate_Info_function.show_plate_info(0))
        self.Availability_button.clicked.connect(
            lambda: Plate_Info_function.set_current_search_type("availability"))
        self.Availability_button.clicked.connect(
            lambda: Plate_Info_function.show_plate_info(0))

        self.Add_new_plate.clicked.connect(
            lambda: Plate_Info_function.show_add_new_plate_window())
        self.Assign_plate_to_user.clicked.connect(
            lambda: Plate_Info_function.show_assign_plate_to_user_window())
        self.Deassign_plate_from_user.clicked.connect(
            lambda: Plate_Info_function.show_deassign_plate_to_user_window())
        self.Remove_plate.clicked.connect(
            lambda: Plate_Info_function.show_delete_plate_confirm())

        self.Plate_info_pages.valueChanged.connect(
            lambda: Plate_Info_function.show_plate_info(self.Plate_info_pages.value()))

        # let table be read only
        self.Display_Plate_Info.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)

        # hide the message
        self.Assign_fail_label.setHidden(True)
        self.Assign_success_label.setHidden(True)

        # set the maximum number for spinbox
        self.Plate_info_pages.setMaximum(2147483647)

        # show all info initially
        Plate_Info_function.show_plate_info(0)


class Ui_Register(object):
    # global variable
    default_password = "Point1"

    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.resize(294, 402)
        self.ID_input = QtWidgets.QLineEdit(Register)
        self.ID_input.setGeometry(QtCore.QRect(112, 20, 141, 21))
        self.ID_input.setText("")
        self.ID_input.setObjectName("ID_input")
        self.Add_a_user_button = QtWidgets.QPushButton(Register)
        self.Add_a_user_button.setGeometry(QtCore.QRect(100, 300, 113, 32))
        self.Add_a_user_button.setObjectName("Add_a_user_button")
        self.Name_input = QtWidgets.QLineEdit(Register)
        self.Name_input.setGeometry(QtCore.QRect(112, 80, 141, 21))
        self.Name_input.setText("")
        self.Name_input.setObjectName("Name_input")
        self.Gender_label = QtWidgets.QLabel(Register)
        self.Gender_label.setGeometry(QtCore.QRect(30, 130, 81, 16))
        self.Gender_label.setObjectName("Gender_label")
        self.Name_label = QtWidgets.QLabel(Register)
        self.Name_label.setGeometry(QtCore.QRect(30, 80, 81, 16))
        self.Name_label.setObjectName("Name_label")
        self.ID_label = QtWidgets.QLabel(Register)
        self.ID_label.setGeometry(QtCore.QRect(30, 20, 81, 16))
        self.ID_label.setObjectName("ID_label")
        self.Male_button = QtWidgets.QRadioButton(Register)
        self.Male_button.setGeometry(QtCore.QRect(110, 130, 100, 20))
        self.Male_button.setObjectName("Male_button")
        self.Button_group_gender = QtWidgets.QButtonGroup(Register)
        self.Button_group_gender.setObjectName("Button_group_gender")
        self.Button_group_gender.addButton(self.Male_button)
        self.Female_button = QtWidgets.QRadioButton(Register)
        self.Female_button.setGeometry(QtCore.QRect(110, 160, 100, 20))
        self.Female_button.setObjectName("Female_button")
        self.Button_group_gender.addButton(self.Female_button)
        self.Permission_label = QtWidgets.QLabel(Register)
        self.Permission_label.setGeometry(QtCore.QRect(30, 230, 81, 16))
        self.Permission_label.setObjectName("Permission_label")
        self.Admin_button = QtWidgets.QRadioButton(Register)
        self.Admin_button.setGeometry(QtCore.QRect(110, 230, 100, 20))
        self.Admin_button.setObjectName("Admin_button")
        self.Button_group_permission = QtWidgets.QButtonGroup(Register)
        self.Button_group_permission.setObjectName("Button_group_permission")
        self.Button_group_permission.addButton(self.Admin_button)
        self.Normal_button = QtWidgets.QRadioButton(Register)
        self.Normal_button.setGeometry(QtCore.QRect(110, 260, 100, 20))
        self.Normal_button.setObjectName("Normal_button")
        self.Button_group_permission.addButton(self.Normal_button)
        self.ID_error_message = QtWidgets.QLabel(Register)
        self.ID_error_message.setGeometry(QtCore.QRect(150, 40, 101, 16))
        self.ID_error_message.setObjectName("ID_error_message")
        self.Register_error_message = QtWidgets.QLabel(Register)
        self.Register_error_message.setGeometry(QtCore.QRect(100, 350, 81, 20))
        self.Register_error_message.setObjectName("Register_error_message")
        self.Register_success_message = QtWidgets.QLabel(Register)
        self.Register_success_message.setGeometry(
            QtCore.QRect(60, 350, 211, 20))
        self.Register_success_message.setObjectName("Register_success_message")
        self.Other_button = QtWidgets.QRadioButton(Register)
        self.Other_button.setGeometry(QtCore.QRect(110, 190, 100, 20))
        self.Other_button.setObjectName("Other_button")
        self.Button_group_gender.addButton(self.Other_button)
        self.line = QtWidgets.QFrame(Register)
        self.line.setGeometry(QtCore.QRect(30, 60, 251, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Register)
        self.line_2.setGeometry(QtCore.QRect(30, 110, 251, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Register)
        self.line_3.setGeometry(QtCore.QRect(30, 210, 251, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Register)
        self.line_4.setGeometry(QtCore.QRect(30, 280, 251, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        # hide the error message initially
        self.ID_error_message.setHidden(True)
        self.Register_error_message.setHidden(True)
        self.Register_success_message.setHidden(True)

        self.retranslateUi(Register)
        QtCore.QMetaObject.connectSlotsByName(Register)

        self.modding()

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "Register"))
        self.Add_a_user_button.setText(_translate("Register", "Add a user"))
        self.Gender_label.setText(_translate("Register", "Gender"))
        self.Name_label.setText(_translate("Register", "Name"))
        self.ID_label.setText(_translate("Register", "ID"))
        self.Male_button.setText(_translate("Register", "Male"))
        self.Female_button.setText(_translate("Register", "Female"))
        self.Permission_label.setText(_translate("Register", "Permission"))
        self.Admin_button.setText(_translate("Register", "Admin"))
        self.Normal_button.setText(_translate("Register", "Normal"))
        self.ID_error_message.setText(_translate("Register", "Invalid ID!"))
        self.Register_error_message.setText(
            _translate("Register", "Action failed!"))
        self.Register_success_message.setText(
            _translate("Register", "Successfully added the user!"))
        self.Other_button.setText(_translate("Register", "Others"))

    def modding(self):
        # connect button to function
        self.Add_a_user_button.clicked.connect(lambda: Register_function.press_register(
            self.ID_input.text(), self.default_password, self.Name_input.text()))


# Function class
class UI_Login_function:
    def check_ID_password_function(self, userid, password):
        try:
            SQL_function.check_if_user_info_is_empty()
            # initialize
            ID_password_match = False
            ID_is_admin = False
            ID_exist = SQL_function.check_ID_exist(userid)

            # encrypt the password
            encrypted_password = helper.encode_password(password)

            # check if id and password is correct
            ID_password_match = SQL_function.check_ID_password(
                userid, encrypted_password)
            # error handler
            if(ID_password_match == -1):
                return -1

            # check if user is admin
            ID_is_admin = SQL_function.check_ID_is_admin(userid)
            # error handler
            if(ID_is_admin == -1):
                return - 1

            if(ID_password_match is True):
                # enter Advance mode
                if(ID_is_admin is True and Loginui.checkBox.isChecked()):
                    SQL_function.add_login_record(
                        userid, "SUCCESS", "Login with Advance mode")
                    self.open_Concentrate_Advance_window()
                    Login.close()
                    return 1
                # Fail: Not admin but try to entering advance mode
                elif(ID_is_admin is False and self.checkBox.isChecked()):
                    SQL_function.add_login_record(
                        userid, "FAIL", "A normal user tries to enter Advance mode")
                    Loginui.Error_Message_for_permission.setHidden(False)
                    Loginui.Error_Message_for_password.setHidden(True)
                    Loginui.Error_Message_for_ID.setHidden(True)
                    return - 1
                # Normal user mode
                else:
                    self.display_normal_welcome_message()
                    SQL_function.add_login_record(
                        userid, "SUCCESS", "Login with normal user mode")
                    Login.close()
                    return 1
            # Fail: ID doesn't exist
            elif(ID_exist is False):
                SQL_function.add_login_record(
                    userid, "FAIL", "ID doesn't exist")
                # display the error message
                Loginui.Error_Message_for_permission.setHidden(True)
                Loginui.Error_Message_for_password.setHidden(True)
                Loginui.Error_Message_for_ID.setHidden(False)
                return - 1
            # Fail: ID doesn't match password
            elif(ID_password_match is False):
                SQL_function.add_login_record(
                    userid, "FAIL", "ID and Password doesn't match")
                # display the error message
                Loginui.Error_Message_for_password.setHidden(False)
                Loginui.Error_Message_for_permission.setHidden(True)
                Loginui.Error_Message_for_ID.setHidden(True)
                return - 1
        except:
            ErrorLogger.logger.error(
                "check_ID_password_function Encountered error")
            return -1

    def open_Concentrate_Advance_window(self):
        try:
            self.Concentrate_Advance = QtWidgets.QTabWidget()
            self.Concentrate_Advance_ui = Ui_Concentrate_Advance()
            self.Concentrate_Advance_ui.current_user_ID = Loginui.UserID_Input.text()
            self.Concentrate_Advance_ui.setupUi(self.Concentrate_Advance)
            self.Concentrate_Advance.show()
        except:
            ErrorLogger.logger.error(
                "open_Concentrate_Advance_window Encountered error")
            return -1

    def open_Info_Editor_window(self):
        try:
            self.Info_Editor = QtWidgets.QWidget()
            self.Info_Editor_ui = Ui_Info_Editor()
            self.Info_Editor_ui.current_user_ID = Loginui.UserID_Input.text()
            self.Info_Editor_ui.setupUi(self.Info_Editor)
            self.Info_Editor.show()
        except:
            ErrorLogger.logger.error(
                "open_Info_Editor_window Encountered error")
            return -1

    def display_normal_welcome_message(self):
        try:
            confirm = QMessageBox()
            confirm.setWindowTitle("Welcome window")
            confirm.setText(
                "Welcome! " + Loginui.UserID_Input.text() + "! Display edit window?")
            confirm.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
            confirm.setDefaultButton(QMessageBox.Cancel)
            confirm.accepted.connect(lambda: self.open_Info_Editor_window())
            confirm.accepted.connect(
                lambda: Info_Editor_function.show_user_info_into_table())
            x = confirm.exec_()
        except:
            ErrorLogger.logger.error(
                "display_normal_welcome_message Encountered error")
            return -1


class UI_Info_Editor_function:

    initial_data = []
    edited_data = []

    def show_user_info_into_table(self):
        try:
            data = SQL_function.get_data_from_database("User_Information",
                                                       "id_strict", Login_function.Info_Editor_ui.current_user_ID, 0)
            Login_function.Info_Editor_ui.Display_table.setRowCount(0)
            row = 0
            self.check_button_array_normal_edit = []
            self.initial_data = []
            for login_record in data:
                Login_function.Info_Editor_ui.Display_table.insertRow(row)
                Login_function.Info_Editor_ui.Display_table.setItem(
                    row, 1, QtWidgets.QTableWidgetItem(login_record[1]))
                Login_function.Info_Editor_ui.Display_table.setItem(
                    row, 2, QtWidgets.QTableWidgetItem("************"))
                Login_function.Info_Editor_ui.Display_table.setItem(
                    row, 3, QtWidgets.QTableWidgetItem(login_record[3]))
                Login_function.Info_Editor_ui.Display_table.setItem(
                    row, 4, QtWidgets.QTableWidgetItem(login_record[4]))
                Login_function.Info_Editor_ui.Display_table.setItem(
                    row, 5, QtWidgets.QTableWidgetItem(login_record[5]))
                Login_function.Info_Editor_ui.Display_table.setItem(
                    row, 6, QtWidgets.QTableWidgetItem(str(login_record[6])))

                # set a button to table
                check_box = QtWidgets.QCheckBox()
                Login_function.Info_Editor_ui.Display_table.setCellWidget(
                    row, 0, check_box)
                self.check_button_array_normal_edit.append(check_box)
                row = row+1
                SQL_function.update_plate_user_have(login_record[1])
                self.initial_data.append(
                    (login_record[1], login_record[2], login_record[3], login_record[4], login_record[5], login_record[6]))

            helper.lock_the_Column(
                Login_function.Info_Editor_ui.Display_table, 1)
            helper.lock_the_Column(
                Login_function.Info_Editor_ui.Display_table, 3)
            helper.lock_the_Column(
                Login_function.Info_Editor_ui.Display_table, 6)
        except:
            ErrorLogger.logger.error(
                "show_user_info_into_table Encountered error")
            return -1

    def get_data_from_table(self):
        try:
            # this function will reset edited_data
            self.edited_data = []
            # go through entire table row by row
            for row in range(Login_function.Info_Editor_ui.Display_table.rowCount()):
                edited_row = []
                for column in range(Login_function.Info_Editor_ui.Display_table.columnCount()):
                    if(Login_function.Info_Editor_ui.Display_table.item(row, column) != None):
                        edited_row.append(
                            Login_function.Info_Editor_ui.Display_table.item(row, column).text())

                self.edited_data.append(edited_row)
                # check if check box is checked (防呆機制)
                if(self.check_button_array_normal_edit[row].isChecked()):
                    # check if input permission and gender fit format
                    if((edited_row[2] == "USER" or edited_row[2] == "ADMIN") and ((edited_row[4] == "MALE" or edited_row[4] == "FEMALE" or edited_row[4] == "OTHERS"))):
                        # update name, gender, and permission
                        SQL_function.update_data_to_user_info(
                            edited_row[0], None, edited_row[2], edited_row[3], edited_row[4], edited_row[5])
                        Login_function.Info_Editor_ui.Input_Invalid.setHidden(
                            True)
                    else:
                        Login_function.Info_Editor_ui.Input_Invalid.setHidden(
                            False)
                        return
                    # check if password had been changed
                    if(edited_row[1] != "************"):
                        # check if edited password fit format
                        if(helper.check_password_availability(edited_row[1])):
                            SQL_function.update_data_to_user_info(edited_row[0], helper.encode_password(
                                edited_row[1]), edited_row[2], edited_row[3], edited_row[4], edited_row[5])
                            Login_function.Info_Editor_ui.Input_Invalid.setHidden(
                                True)
                        else:
                            Login_function.Info_Editor_ui.Input_Invalid.setHidden(
                                False)
                            return
            helper.data_comparison(self.edited_data, self.initial_data)
            self.show_user_info_into_table()
        except:
            ErrorLogger.logger.error(
                "get_data_from_table Encountered error")
            return -1


class UI_Search_Edit_function:
    initial_data = []
    edited_data = []
    user_info_pages_maximum = 0
    current_search_type = "all"
    check_button_array_search_edit = []
    # Function for Search/Edit

    def show_user(self, pages):
        try:
            if(self.current_search_type == "id"):
                if(Login_function.Concentrate_Advance_ui.ID_input.text() == None):
                    value = ""
                value = Login_function.Concentrate_Advance_ui.ID_input.text()
            elif(self.current_search_type == "name"):
                if(Login_function.Concentrate_Advance_ui.Name_input.text() == None):
                    value = ""
                value = Login_function.Concentrate_Advance_ui.Name_input.text()
            elif(self.current_search_type == "all"):
                value = None
            elif(self.current_search_type == "permission"):
                if(Login_function.Concentrate_Advance_ui.User_button.isChecked()):
                    value = "USER"
                elif(Login_function.Concentrate_Advance_ui.Admin_button.isChecked()):
                    value = "ADMIN"
                else:
                    value = ""
            elif(self.current_search_type == "gender"):
                if(Login_function.Concentrate_Advance_ui.Male_button.isChecked()):
                    value = "MALE"
                elif(Login_function.Concentrate_Advance_ui.Female_button.isChecked()):
                    value = "FEMALE"
                elif(Login_function.Concentrate_Advance_ui.Others_button.isChecked()):
                    value = "OTHERS"
                else:
                    value = ""

            self.set_user_info_pages_maximum(value)
            if(self.user_info_pages_maximum <= pages):
                Login_function.Concentrate_Advance_ui.User_info_pages.setValue(
                    self.user_info_pages_maximum)
                pages = self.user_info_pages_maximum

            data = SQL_function.get_data_from_database("User_Information",
                                                       self.current_search_type, value, pages)

            helper.insert_data_into_table(
                Login_function.Concentrate_Advance_ui.Display_table, data)
            self.insert_checkbox_search_edit(data)
            helper.lock_the_Column(
                Login_function.Concentrate_Advance_ui.Display_table, 1)
            helper.lock_the_Column(
                Login_function.Concentrate_Advance_ui.Display_table, 6)
        except:
            ErrorLogger.logger.error(
                "show_user Encountered error")
            return -1

    def insert_checkbox_search_edit(self, data):
        try:
            for check_box_row in range(len(data)):
                # set a button to table
                check_box = QtWidgets.QCheckBox()
                Login_function.Concentrate_Advance_ui.Display_table.setCellWidget(
                    check_box_row, 0, check_box)
                self.check_button_array_search_edit.append(check_box)
        except:
            ErrorLogger.logger.error(
                "insert_checkbox_search_edit Encountered error")
            return -1

    def get_data_from_table(self):
        try:
            self.edited_data = []
            # go through entire table row by row
            for row in range(Login_function.Concentrate_Advance_ui.Display_table.rowCount()):
                edited_row = []
                for column in range(Login_function.Concentrate_Advance_ui.Display_table.columnCount()):
                    if(Login_function.Concentrate_Advance_ui.Display_table.item(row, column) != None):
                        edited_row.append(
                            Login_function.Concentrate_Advance_ui.Display_table.item(row, column).text())
                # update plate_number_nomatter_what
                SQL_function.update_plate_user_have(edited_row[1])
                self.edited_data.append(edited_row)

                # check if check box is checked (防呆機制)
                if(self.check_button_array_search_edit[row].isChecked()):
                    # check if input permission and gender fit format
                    if((edited_row[2] == "USER" or edited_row[2] == "ADMIN") and (edited_row[4] == "MALE" or edited_row[4] == "FEMALE" or edited_row[4] == "OTHERS")):
                        # update name, gender, and permission
                        SQL_function.update_data_to_user_info(
                            edited_row[0], None, edited_row[2], edited_row[3], edited_row[4], edited_row[5])
                        Login_function.Concentrate_Advance_ui.Edit_error_message.setHidden(
                            True)
                    else:
                        Login_function.Concentrate_Advance_ui.Edit_error_message.setHidden(
                            False)
                        return
                    # check if password had been changed
                    if(edited_row[1] != "************"):
                        # check if edited password fit format
                        if(helper.check_password_availability(edited_row[1])):
                            SQL_function.update_data_to_user_info(edited_row[0], helper.encode_password(
                                edited_row[1]), edited_row[2], edited_row[3], edited_row[4], edited_row[5])
                            Login_function.Concentrate_Advance_ui.Edit_error_message.setHidden(
                                True)
                        else:
                            Login_function.Concentrate_Advance_ui.Edit_error_message.setHidden(
                                False)
                            return
            helper.data_comparison(self.edited_data, self.initial_data)
            self.show_user(0)
        except:
            ErrorLogger.logger.error(
                "get_data_from_table Encountered error")
            return -1

    def open_Register_window(self):
        try:
            self.Register = QtWidgets.QWidget()
            self.Register_ui = Ui_Register()
            self.Register_ui.setupUi(self.Register)
            self.Register.show()
        except:
            ErrorLogger.logger.error(
                "open_Register_window Encountered error")
            return -1

    def show_delete_confirm(self):
        try:
            confirm = QMessageBox()
            confirm.setWindowTitle("Delete Confirm")
            confirm.setText(
                "Remove users will automatically deassign plates that had been assigned to these users.\n Still want to remove users?")
            confirm.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
            confirm.setDefaultButton(QMessageBox.Cancel)
            confirm.accepted.connect(lambda: self.delete_users())
            x = confirm.exec_()
        except:
            ErrorLogger.logger.error(
                "show_delete_confirm Encountered error")
            return -1

    def delete_users(self):
        try:
            # go through entire table row by row
            for row in range(Login_function.Concentrate_Advance_ui.Display_table.rowCount()):
                data = []
                for column in range(Login_function.Concentrate_Advance_ui.Display_table.columnCount()):
                    if(Login_function.Concentrate_Advance_ui.Display_table.item(row, column) != None):
                        data.append(Login_function.Concentrate_Advance_ui.Display_table.item(
                            row, column).text())
                if(self.check_button_array_search_edit[row].isChecked()):
                    plate_list = SQL_function.get_plate_id_user_have(data[0])
                    for plate_id in plate_list:
                        SQL_function.deassign_plate_from_user(
                            plate_id[0], "TRUE", helper.get_time())
                    SQL_function.remove_user(data[0])
            Search_Edit_function.set_current_search_type("all")
            Search_Edit_function.show_user(0)
            Plate_Info_function.show_plate_info(0)

        except:
            ErrorLogger.logger.error(
                "delete_users Encountered error")
            return -1

    def set_user_info_pages_maximum(self, value):
        try:
            self.user_info_pages_maximum = SQL_function.get_row_number_from_database(user_info_table,
                                                                                     self.current_search_type, value) // 20
            if(SQL_function.get_row_number_from_database(user_info_table, self.current_search_type, value) % 20 == 0 and SQL_function.get_row_number_from_database(user_info_table, self.current_search_type, value) > 20):
                self.user_info_pages_maximum = (SQL_function.get_row_number_from_database(user_info_table,
                                                                                          self.current_search_type, value) // 20) - 1
        except:
            ErrorLogger.logger.error(
                "set_user_info_pages_maximum Encountered error")
            return -1

    def set_current_search_type(self, type):
        try:
            self.current_search_type = type
        except:
            ErrorLogger.logger.error(
                "set_current_search_type Encountered error")
            return -1


class UI_Register_function:
    def press_register(self, userid, password, real_name):
        try:
            return_flag = False
            gender_flag = False
            admin_flag = False
            name_flag = False
            # handle invalid input
            if(SQL_function.check_ID_exist(userid) is True or userid == "" or len(userid) < 4 or (helper.has_invalid_character(userid))):
                Search_Edit_function.Register_ui.ID_error_message.setHidden(
                    False)
                return_flag = True
            else:
                Search_Edit_function.Register_ui.ID_error_message.setHidden(
                    True)

            if(Search_Edit_function.Register_ui.Male_button.isChecked() or Search_Edit_function.Register_ui.Female_button.isChecked() or Search_Edit_function.Register_ui.Other_button.isChecked()):
                gender_flag = True
            if(Search_Edit_function.Register_ui.Admin_button.isChecked() or Search_Edit_function.Register_ui.Normal_button.isChecked()):
                admin_flag = True
            if(real_name == ""):
                name_flag = True

            if(return_flag is True or name_flag is True or gender_flag is False or admin_flag is False):
                Search_Edit_function.Register_ui.Register_error_message.setHidden(
                    False)
                Search_Edit_function.Register_ui.Register_success_message.setHidden(
                    True)
                return -1

            # transfer radio button information to string
            if(Search_Edit_function.Register_ui.Male_button.isChecked()):
                gender = "MALE"
            elif(Search_Edit_function.Register_ui.Female_button.isChecked()):
                gender = "FEMALE"
            elif(Search_Edit_function.Register_ui.Other_button.isChecked()):
                gender = "OTHERS"
            if(Search_Edit_function.Register_ui.Admin_button.isChecked()):
                permission = "ADMIN"
            elif(Search_Edit_function.Register_ui.Normal_button.isChecked()):
                permission = "USER"

            # add the user
            SQL_function.add_user(userid, helper.encode_password(
                password), permission, real_name, gender)
            Search_Edit_function.set_current_search_type("all")
            Search_Edit_function.show_user(0)
            Search_Edit_function.Register_ui.Register_error_message.setHidden(
                True)
            Search_Edit_function.Register_ui.Register_success_message.setHidden(
                False)
        except:
            ErrorLogger.logger.error(
                "press_register Encountered error")
            return -1


class UI_Login_History_function:
    login_history_pages_maximum = 0
    current_search_type = "all"

    # Function for Login History
    def show_login_history(self, pages):
        try:
            if(self.current_search_type == "id"):
                if(Login_function.Concentrate_Advance_ui.ID_input_login_history.text() == None):
                    value = ""
                value = Login_function.Concentrate_Advance_ui.ID_input_login_history.text()
            elif(self.current_search_type == "all"):
                value = None
            elif(self.current_search_type == "status"):
                if(Login_function.Concentrate_Advance_ui.Success_button.isChecked()):
                    value = "SUCCESS"
                elif(Login_function.Concentrate_Advance_ui.Fail_button.isChecked()):
                    value = "FAIL"
                else:
                    value = ""
            elif(self.current_search_type == "specific_type_fail"):
                if(Login_function.Concentrate_Advance_ui.ID_doesnt_exist_button.isChecked()):
                    value = "ID doesn't exist"
                elif(Login_function.Concentrate_Advance_ui.Password_doesnt_match_ID_button.isChecked()):
                    value = "ID and Password doesn't match"
                elif(Login_function.Concentrate_Advance_ui.User_enter_advance_button.isChecked()):
                    value = "A normal user tries to enter Advance mode"
                else:
                    value = ""
            elif(self.current_search_type == "specific_type_success"):
                if(Login_function.Concentrate_Advance_ui.Normal_login_button.isChecked()):
                    value = "Login with normal user mode"
                elif(Login_function.Concentrate_Advance_ui.Advance_login_button.isChecked()):
                    value = "Login with Advance mode"
                else:
                    value = ""

            self.set_login_history_pages_maximum(value)
            if(self.login_history_pages_maximum <= pages):
                Login_function.Concentrate_Advance_ui.Login_History_Pages.setValue(
                    self.login_history_pages_maximum)
                pages = self.login_history_pages_maximum
            data = SQL_function.get_data_from_database("Login_record",
                                                       self.current_search_type, value, pages)
            helper.insert_data_into_table(
                Login_function.Concentrate_Advance_ui.Display_Login_info, data)

        except:
            ErrorLogger.logger.error(
                "show_login_history Encountered error")
            return -1

    def set_login_history_pages_maximum(self, value):
        try:
            self.login_history_pages_maximum = SQL_function.get_row_number_from_database(login_record_table,
                                                                                         self.current_search_type, value) // 20
            if(SQL_function.get_row_number_from_database(login_record_table, self.current_search_type, value) % 20 == 0
               and SQL_function.get_row_number_from_database(login_record_table, self.current_search_type, value) > 20):
                self.login_history_pages_maximum = (SQL_function.get_row_number_from_database(login_record_table,
                                                                                              self.current_search_type, value) // 20) - 1
        except:
            ErrorLogger.logger.error(

                "set_login_history_pages_maximum Encountered error")
            return -1

    def set_current_search_type(self, type):
        try:
            self.current_search_type = type
        except:
            ErrorLogger.logger.error(
                "set_current_search_type Encountered error")
            return -1


class UI_Plate_info_function:
    plate_info_pages_maximum = 0
    current_search_type = "all"

    # Function for Plate Scan
    def show_plate_info(self, pages):
        try:
            if(self.current_search_type == "all"):
                value = None
            elif(self.current_search_type == "user_id"):
                if(Login_function.Concentrate_Advance_ui.ID_input_Plate_Info.text() == None):
                    value = ""
                value = Login_function.Concentrate_Advance_ui.ID_input_Plate_Info.text()
            elif(self.current_search_type == "plate_id"):
                if(Login_function.Concentrate_Advance_ui.Plate_ID_input_Plate_Info.text() == None):
                    value = ""
                value = Login_function.Concentrate_Advance_ui.Plate_ID_input_Plate_Info.text()
            elif(self.current_search_type == "availability"):
                if(Login_function.Concentrate_Advance_ui.Available_FALSE.isChecked()):
                    value = "FALSE"
                elif(Login_function.Concentrate_Advance_ui.Available_TRUE.isChecked()):
                    value = "TRUE"
                else:
                    value = ""

            self.set_plate_info_pages_maximum(value)
            if(self.plate_info_pages_maximum <= pages):
                Login_function.Concentrate_Advance_ui.Plate_info_pages.setValue(
                    self.plate_info_pages_maximum)
                pages = self.plate_info_pages_maximum

            data = SQL_function.get_data_from_database("Plate_Information",
                                                       self.current_search_type, value, pages)
            helper.insert_data_into_table(
                Login_function.Concentrate_Advance_ui.Display_Plate_Info, data)
            self.insert_checkbox_plate_info(data)
        except:
            ErrorLogger.logger.error(
                "show_plate_info Encountered error")
            return -1

    def insert_checkbox_plate_info(self, data):
        try:
            for check_box_row in range(len(data)):
                # set a button to table
                check_box = QtWidgets.QCheckBox()
                Login_function.Concentrate_Advance_ui.Display_Plate_Info.setCellWidget(
                    check_box_row, 0, check_box)
                self.check_button_array_plate_info.append(check_box)
        except:
            ErrorLogger.logger.error(
                "insert_checkbox_plate_info Encountered error")
            return -1

    def show_add_new_plate_window(self):
        try:
            plateid, read_next_plate = QtWidgets.QInputDialog().getText(
                Login_function.Concentrate_Advance_ui.Plate_Scan_Tab, '', 'Please scan the bar code on the plate.')
            if(read_next_plate is True and plateid != ''):
                SQL_function.add_new_plate(plateid)
                self.show_plate_info(0)
                self.show_add_new_plate_window()
        except:
            ErrorLogger.logger.error(
                "show_add_new_plate_window Encountered error")
            return -1

    def show_delete_plate_confirm(self):
        try:
            confirm = QMessageBox()
            confirm.setWindowTitle("Remove confirm")
            confirm.setText("Remove these plates from database?")
            confirm.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
            confirm.setDefaultButton(QMessageBox.Cancel)
            confirm.accepted.connect(lambda: self.remove_plate())
            x = confirm.exec_()
        except:
            ErrorLogger.logger.error(
                "show_delete_plate_confirm Encountered error")
            return -1

    def remove_plate(self):
        try:
            for row in range(Login_function.Concentrate_Advance_ui.Display_Plate_Info.rowCount()):
                data = []
                for column in range(Login_function.Concentrate_Advance_ui.Display_Plate_Info.columnCount()):
                    if(Login_function.Concentrate_Advance_ui.Display_Plate_Info.item(row, column) != None):
                        data.append(Login_function.Concentrate_Advance_ui.Display_Plate_Info.item(
                            row, column).text())
                if(self.check_button_array_plate_info[row].isChecked()):
                    SQL_function.remove_plate(data[0])

            self.show_plate_info(0)
            Search_Edit_function.show_user(0)
        except:
            ErrorLogger.logger.error(
                "remove_plate Encountered error")
            return -1

    def show_assign_plate_to_user_window(self):
        try:
            userid, ok = QtWidgets.QInputDialog().getText(Login_function.Concentrate_Advance_ui.Plate_Scan_Tab,
                                                          '', 'Please enter the user id that you like to assign to.')
            if(ok):

                if(SQL_function.check_ID_exist(userid) is True):
                    # go through entire table row by row
                    for row in range(Login_function.Concentrate_Advance_ui.Display_Plate_Info.rowCount()):
                        data = []
                        for column in range(Login_function.Concentrate_Advance_ui.Display_Plate_Info.columnCount()):
                            if(Login_function.Concentrate_Advance_ui.Display_Plate_Info.item(row, column) != None):
                                data.append(Login_function.Concentrate_Advance_ui.Display_Plate_Info.item(
                                    row, column).text())
                        if(self.check_button_array_plate_info[row].isChecked()):
                            if(data[2] == "TRUE"):
                                SQL_function.assign_plate_to_user(
                                    data[0], userid, "FALSE", helper.get_time())
                                Login_function.Concentrate_Advance_ui.Assign_success_label.setHidden(
                                    False)
                                Login_function.Concentrate_Advance_ui.Assign_fail_label.setHidden(
                                    True)
                else:
                    Login_function.Concentrate_Advance_ui.Assign_success_label.setHidden(
                        True)
                    Login_function.Concentrate_Advance_ui.Assign_fail_label.setHidden(
                        False)
            self.show_plate_info(0)
            self.update_whole_table()
            Search_Edit_function.show_user(0)
        except:
            ErrorLogger.logger.error(

                "show_assign_plate_to_user_window Encountered error")
            return -1

    def show_deassign_plate_to_user_window(self):
        try:
            confirm = QMessageBox()
            confirm.setWindowTitle("Deassign confirm")
            confirm.setText("Deassign these plates from Users?")
            confirm.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
            confirm.setDefaultButton(QMessageBox.Cancel)
            confirm.accepted.connect(lambda: self.deassign_plate())
            x = confirm.exec_()
        except:
            ErrorLogger.logger.error(
                "show_deassign_plate_to_user_window Encountered error")
            return -1

    def deassign_plate(self):
        try:
            for row in range(Login_function.Concentrate_Advance_ui.Display_Plate_Info.rowCount()):
                data = []
                for column in range(Login_function.Concentrate_Advance_ui.Display_Plate_Info.columnCount()):
                    if(Login_function.Concentrate_Advance_ui.Display_Plate_Info.item(row, column) != None):
                        data.append(Login_function.Concentrate_Advance_ui.Display_Plate_Info.item(
                            row, column).text())

                if(self.check_button_array_plate_info[row].isChecked()):

                    if(data[2] == "FALSE"):
                        SQL_function.deassign_plate_from_user(
                            data[0], "TRUE", helper.get_time())
            self.show_plate_info(0)
            self.update_whole_table()
            Search_Edit_function.show_user(0)
        except:
            ErrorLogger.logger.error(
                "deassign_plate Encountered error")
            return -1

    def update_whole_table(self):
        try:
            for row in range(Login_function.Concentrate_Advance_ui.Display_Plate_Info.rowCount()):
                data = []
                for column in range(Login_function.Concentrate_Advance_ui.Display_Plate_Info.columnCount()):
                    if(Login_function.Concentrate_Advance_ui.Display_Plate_Info.item(row, column) != None):
                        data.append(Login_function.Concentrate_Advance_ui.Display_Plate_Info.item(
                            row, column).text())
                SQL_function.update_plate_user_have(data[1])
        except:
            ErrorLogger.logger.error(
                "update_whole_table Encountered error")
            return -1

    def set_plate_info_pages_maximum(self, value):
        try:
            self.plate_info_pages_maximum = SQL_function.get_row_number_from_database(plate_info_table,
                                                                                      self.current_search_type, value) // 20
            if(SQL_function.get_row_number_from_database(plate_info_table, self.current_search_type, value) % 20 == 0
               and SQL_function.get_row_number_from_database(plate_info_table, self.current_search_type, value) > 20):
                self.plate_info_pages_maximum = (SQL_function.get_row_number_from_database(plate_info_table,
                                                                                           self.current_search_type, value) // 20) - 1
        except:
            ErrorLogger.logger.error(
                "set_plate_info_pages_maximum Encountered error")
            return -1

    def set_login_history_pages_maximum(self, function_class, value, table):
        try:
            self.login_history_pages_maximum = SQL_function.get_row_number_from_database(table,
                                                                                         self.current_search_type, value) // 20
            if(SQL_function.get_row_number_from_database(table, self.current_search_type, value) % 20 == 0
               and SQL_function.get_row_number_from_database(table, self.current_search_type, value) > 20):
                self.login_history_pages_maximum = (SQL_function.get_row_number_from_database(login_record_table,
                                                                                              self.current_search_type, value) // 20) - 1
        except:
            ErrorLogger.logger.error(
                "set_login_history_pages_maximum Encountered error")
            return -1

    def set_current_search_type(self, type):
        try:
            self.current_search_type = type
        except:
            ErrorLogger.logger.error(
                "set_current_search_type Encountered error")
            return -1


class helper_function:

    # helper function
    # change info in connect_to_database() to connect to different database
    def encode_password(self, password):
        try:
            hash_md5 = hashlib.md5()
            hash_md5.update(password.encode("utf-8"))
            return hash_md5.hexdigest()
        except:
            ErrorLogger.logger.error(
                "encode_password Encountered error")
            return -1

    def get_time(self):
        try:
            return datetime.datetime.now()
        except:
            ErrorLogger.logger.error(
                "get_time Encountered error")
            return -1

    def lock_the_Column(self, display_table, lock_column):
        try:
            rows = display_table.rowCount()
            for i in range(rows):
                item = display_table.item(i, lock_column)
                item.setFlags(QtCore.Qt.ItemIsEnabled)
        except:
            ErrorLogger.logger.error(
                "lock_the_Column Encountered error")
            return -1

    # checker for password
    def has_capital_letters(self, password):
        try:
            has_capital = False
            for letters in password:
                # checking for uppercase character and flagging
                if letters.isupper():
                    has_capital = True
                    break
            return has_capital
        except:
            ErrorLogger.logger.error(
                "has_capital_letters Encountered error")
            return -1

    def has_lower_letters(self, password):
        try:
            has_lower = False
            for letters in password:
                # checking for uppercase character and flagging
                if letters.islower():
                    has_lower = True
                    break
            return has_lower
        except:
            ErrorLogger.logger.error(
                "has_lower_letters Encountered error")
            return -1

    def has_numbers(self, password):
        try:
            return any(letters.isdigit() for letters in password)
        except:
            ErrorLogger.logger.error(
                "has_numbers Encountered error")
            return -1

    def has_invalid_character(self, password):
        try:
            # Make own character set and pass
            # this as argument in compile method
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
            # Pass the string in search
            # method of regex object.
            if(re.search("[^a-zA-Z0-9s]", password) or (' ' in password) is True):
                return True
            else:
                return False
        except:
            ErrorLogger.logger.error(
                "has_invalid_character Encountered error")
            return -1

    def check_password_availability(self, password):
        try:
            if(len(password) >= 6 and self.has_capital_letters(password) is True and self.has_numbers(password) and self.has_lower_letters(password) is True and (self.has_invalid_character(password) is False)):
                return True
            return False
        except:
            ErrorLogger.logger.error(

                "check_password_availablility Encountered error")
            return -1

    def data_comparison(self, edited_data, initial_data):
        try:
            for row in zip(edited_data, initial_data):
                if(row[0][1] != "************"):
                    AdminEditorLogger.logger.info(
                        "USER ID: '" + row[0][0] + "'s password has been edited.")
                if(row[0][2] != row[1][2]):
                    AdminEditorLogger.logger.info(
                        "USER ID: '" + row[0][0] + "'s permission has been edited from '" + row[1][2] + "' to '" + row[0][2] + "'.")
                if(row[0][3] != row[1][3]):
                    AdminEditorLogger.logger.info(
                        "USER ID: '" + row[0][0] + "'s name has been edited from '" + row[1][3] + "' to '" + row[0][3] + "'.")
                if(row[0][4] != row[1][4]):
                    AdminEditorLogger.logger.info(
                        "USER ID: '" + row[0][0] + "'s gender has been edited from '" + row[1][4] + "' to '" + row[0][4] + "'.")
        except:
            ErrorLogger.logger.error(
                "data_comparison Encountered error")
            return -1

    def insert_data_into_table(self, display_table,  data):
        try:
            # initialize the table
            display_table.setRowCount(0)
            row_count = 0

            if(display_table == Login_function.Concentrate_Advance_ui.Display_table):
                Search_Edit_function.check_button_array_search_edit = []
                Search_Edit_function.initial_data = []
                for row in data:
                    display_table.insertRow(
                        row_count)
                    for column in range(1, 7):
                        display_table.setItem(
                            row_count, column, QtWidgets.QTableWidgetItem(str(row[column])))
                    display_table.setItem(
                        row_count, 2, QtWidgets.QTableWidgetItem("************"))

                    SQL_function.update_plate_user_have(row[1])
                    Search_Edit_function.initial_data.append(
                        (row[1], row[2], row[3], row[4], row[5], row[6]))
                    row_count = row_count + 1

            elif(display_table == Login_function.Concentrate_Advance_ui.Display_Login_info):
                for row in data:
                    display_table.insertRow(
                        row_count)
                    display_table.setItem(
                        row_count, 0, QtWidgets.QTableWidgetItem(row[1]))
                    display_table.setItem(
                        row_count, 1, QtWidgets.QTableWidgetItem(row[2]))
                    display_table.setItem(
                        row_count, 2, QtWidgets.QTableWidgetItem(row[3]))
                    display_table.setItem(
                        row_count, 3, QtWidgets.QTableWidgetItem(row[4]))
                    row_count = row_count+1
            elif(display_table == Login_function.Concentrate_Advance_ui.Display_Plate_Info):
                Plate_Info_function.check_button_array_plate_info = []
                # goes through every row
                for row in data:
                    display_table.insertRow(
                        row_count)
                    # put item into row's column1 ~ column 5
                    display_table.setItem(
                        row_count, 1, QtWidgets.QTableWidgetItem(row[1]))
                    display_table.setItem(
                        row_count, 2, QtWidgets.QTableWidgetItem(row[2]))
                    display_table.setItem(
                        row_count, 3, QtWidgets.QTableWidgetItem(row[3]))
                    display_table.setItem(
                        row_count, 4, QtWidgets.QTableWidgetItem(row[4]))
                    display_table.setItem(
                        row_count, 5, QtWidgets.QTableWidgetItem(row[5]))
                    row_count = row_count+1
        except:
            ErrorLogger.logger.error(
                "insert_data_into_table Encountered error")
            return -1


class MySQL_function:
    def connect_to_database(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Ar0340252",
                database="UI_database"
            )
            return mydb
        except:
            ErrorLogger.logger.error(
                "connect_to_database Encountered error")
            return -1

    def create_table_first(self, cursor):
        try:
            # CREATE TABLE just in case
            cursor.execute("CREATE TABLE if not exists " + user_info_table +
                           " (USER_INFORMATION_KEY INT PRIMARY KEY AUTO_INCREMENT, ID VARCHAR(500) UNIQUE, PASSWORD VARCHAR(500), PERMISSION VARCHAR(20), REAL_NAME VARCHAR(50), GENDER VARCHAR(20), PLATE_NUM INT)")
            cursor.execute("CREATE TABLE if not exists " + login_record_table +
                           " (LOGIN_RECORD_KEY INT PRIMARY KEY AUTO_INCREMENT, ID VARCHAR(500), LOGIN_TIME VARCHAR(500), LOGIN_STATE VARCHAR(500), SPECIFIC_TYPE VARCHAR(500))")
            cursor.execute("CREATE TABLE if not exists " + plate_info_table +
                           "(PLATE_INFORMATION_KEY INT PRIMARY KEY AUTO_INCREMENT, PLATE_ID VARCHAR(500) UNIQUE, LAST_ASSIGNED_USER_ID VARCHAR(500), AVAILABLE_FOR_ASSIGN VARCHAR(20), LAST_ASSIGN_TIME VARCHAR(500), LAST_DEASSIGN_TIME VARCHAR(500))")
        except:
            ErrorLogger.logger.error(
                "create_table_first Encountered error")
            return -1

    def check_if_user_info_is_empty(self):
        try:
            # Connect to database
            mydb = self.connect_to_database()
            mycursor = mydb.cursor()
            self.create_table_first(mycursor)

            mycursor.execute(
                "SELECT EXISTS (SELECT 1 FROM `User_Information`)")
            data = mycursor.fetchone()
            user_amount = data[0]
            if(user_amount == 0):
                sql = (
                    "INSERT INTO User_Information(ID, PASSWORD, PERMISSION, REAL_NAME, GENDER, PLATE_NUM) VALUES ('ADMIN', %s, 'ADMIN','name', 'OTHERS', '0')")
                val = (helper.encode_password('Point1'), )
                mycursor.execute(sql, val)
                mydb.commit()
                AdminEditorLogger.logger.info(
                    'the very first user is added, which userid: "ADMIN" and password: "Point1"')
        except:
            ErrorLogger.logger.error(
                "check_if_user_info_is_empty Encountered error")
            return -1

    def check_ID_password(self, userid, password):
        Match = False
        try:
            # Connect to database
            mydb = self.connect_to_database()
            mycursor = mydb.cursor()
            # Create table if not exist
            self.create_table_first(mycursor)

            # Actually insert plate into table
            mycursor.execute("SELECT * FROM User_Information")
            for User_record in mycursor:
                # compare the id
                if(User_record[1] == userid):
                    # compare the password
                    if(User_record[2] == password):
                        Match = True
            return Match
        except:
            ErrorLogger.logger.error(
                "Check_ID_password Encountered error!")
            return -1

    def check_ID_is_admin(self, userid):
        is_admin = False
        try:
            # Connect to database
            mydb = self.connect_to_database()
            mycursor = mydb.cursor()
            # Create table if not exist
            self.create_table_first(mycursor)
            mycursor.execute('''SELECT * FROM User_Information''')
            for User_record in mycursor:
                # compare the id
                if(User_record[1] == userid):
                    # check the permission
                    if(User_record[3] == "ADMIN"):
                        is_admin = True
            return is_admin
        except:
            ErrorLogger.logger.error(
                "check_ID_is_admin Encountered error")
            return -1

    def check_ID_exist(self, userid):
        Exist = False
        try:
            # Connect to database
            mydb = self.connect_to_database()
            mycursor = mydb.cursor()
            # Create table if not exist
            self.create_table_first(mycursor)
            mycursor.execute('''SELECT * FROM User_Information''')
            for User_record in mycursor:
                # compare the id
                if(User_record[1] == userid):
                    # ID exists in the database
                    Exist = True
                    return Exist
            return Exist
        except:
            ErrorLogger.logger.error(
                "check_ID_exist Encountered error!")
            return -1

    def remove_user(self, userid):
        try:
            # Connect to database
            mydb = self.connect_to_database()
            mycursor = mydb.cursor()
            # Create table if not exist
            self.create_table_first(mycursor)
            sql = ("DELETE FROM User_Information WHERE ID=%s")
            val = (userid, )
            mycursor.execute(sql, val)
            mydb.commit()
            AdminEditorLogger.logger.info("User with ID: '" +
                                          userid + "' has been deleted!")
        except:
            ErrorLogger.logger.error(
                "remove_user Encountered error!")
            return -1

    def add_user(self, userid, password, permission, real_name, gender):
        try:
            # Connect to database
            mydb = self.connect_to_database()
            mycursor = mydb.cursor()
            # Create table if not exist
            self.create_table_first(mycursor)
            sql = ("INSERT INTO User_Information(ID, PASSWORD, PERMISSION, REAL_NAME, GENDER, PLATE_NUM) VALUES (%s, %s, %s, %s, %s, %s)")
            val = (userid, password, permission, real_name, gender, 0)
            mycursor.execute(sql, val)
            mydb.commit()
            AdminEditorLogger.logger.info("User with ID: '" +
                                          userid + "' has been added.")
        except:
            ErrorLogger.logger.error(
                "add_user Encountered error!")
            return -1

    def add_login_record(self, userid, login_state, type):
        try:
            # Connect to database
            mydb = self.connect_to_database()
            mycursor = mydb.cursor()
            # Create table if not exist
            self.create_table_first(mycursor)
            sql = (
                "INSERT INTO Login_record(ID, LOGIN_TIME, LOGIN_STATE, SPECIFIC_TYPE) VALUES (%s, %s, %s, %s)")
            val = (userid, helper_function.get_time(
                helper_function), login_state, type)
            mycursor.execute(sql, val)
            mydb.commit()
        except:
            ErrorLogger.logger.error(
                "add_login_record Encountered error!")
            return -1

    def get_data_from_database(self, database, type, value, pages):
        # Open database
        try:
            # Connect to database
            mydb = self.connect_to_database()
            mycursor = mydb.cursor()
            # Create table if not exist
            self.create_table_first(mycursor)
            if(database == login_record_table):
                if(type == "all"):
                    sql = ("SELECT * FROM Login_record LIMIT %s OFFSET %s")
                    val = (20, 20*pages)
                if(type == "id"):
                    sql = (
                        "SELECT * FROM Login_record WHERE ID=%s LIMIT %s OFFSET %s")
                    val = (value, 20, 20*pages)
                if(type == "status"):
                    sql = (
                        "SELECT * FROM Login_record WHERE LOGIN_STATE=%s LIMIT %s OFFSET %s")
                    val = (value, 20, 20*pages)
                if(type == "specific_type_fail" or type == "specific_type_success"):
                    sql = (
                        "SELECT * FROM Login_record WHERE SPECIFIC_TYPE=%s LIMIT %s OFFSET %s")
                    val = (value, 20, 20*pages)
            elif(database == user_info_table):
                if(type == "all"):
                    sql = ("SELECT * FROM User_Information LIMIT %s OFFSET %s")
                    val = (20, 20*pages)
                if(type == "id_strict"):
                    sql = (
                        "SELECT * FROM User_Information WHERE ID=%s ORDER BY ID ASC")
                    val = (value,)
                if(type == "id"):
                    sql = (
                        "SELECT * FROM User_Information WHERE ID LIKE %s ORDER BY ID ASC LIMIT %s OFFSET %s")
                    val = ('%'+value+'%', 20, 20*pages)
                if(type == "name"):
                    sql = (
                        "SELECT * FROM User_Information WHERE REAL_NAME LIKE %s ORDER BY REAL_NAME ASC LIMIT %s OFFSET %s")
                    val = ('%'+value+'%', 20, 20*pages)
                if(type == "permission"):
                    sql = (
                        "SELECT * FROM User_Information WHERE PERMISSION=%s ORDER BY ID ASC LIMIT %s OFFSET %s")
                    val = (value, 20, 20*pages)
                if(type == "gender"):
                    sql = (
                        "SELECT * FROM User_Information WHERE GENDER=%s ORDER BY ID ASC LIMIT %s OFFSET %s")
                    val = (value, 20, 20*pages)
            elif(database == plate_info_table):
                if(type == "all"):
                    sql = ("SELECT * FROM Plate_Information LIMIT %s OFFSET %s")
                    val = (20, 20*pages)
                if(type == "plate_id"):
                    sql = (
                        "SELECT * FROM Plate_Information WHERE PLATE_ID LIKE %s ORDER BY PLATE_ID ASC LIMIT %s OFFSET %s")
                    val = ('%'+value+'%', 20, 20*pages)
                if(type == "user_id"):
                    sql = (
                        "SELECT * FROM Plate_Information WHERE LAST_ASSIGNED_USER_ID LIKE %s ORDER BY LAST_ASSIGNED_USER_ID ASC LIMIT %s OFFSET %s")
                    val = ('%'+value+'%', 20, 20*pages)
                if(type == "availability"):
                    sql = (
                        "SELECT * FROM Plate_Information WHERE AVAILABLE_FOR_ASSIGN=%s LIMIT %s OFFSET %s")
                    val = (value, 20, 20*pages)
            mycursor.execute(sql, val)
            data = mycursor.fetchall()
            return data
        except:
            ErrorLogger.logger.error(
                "get_data_from_database Encountered error!")
            return -1

    def update_data_to_user_info(self, userid, password, permission, real_name, gender, plate_amount):
        try:
            # Connect to database
            mydb = self.connect_to_database()
            mycursor = mydb.cursor()
            # Create table if not exist
            self.create_table_first(mycursor)
            if(password != None):
                sql = (
                    "UPDATE User_Information SET PASSWORD=%s, PERMISSION=%s, REAL_NAME=%s, GENDER=%s, PLATE_NUM=%s WHERE ID=%s")
                val = (password, permission, real_name,
                       gender, plate_amount, userid)
                mycursor.execute(sql, val)
            else:
                sql = (
                    "UPDATE User_Information SET PERMISSION=%s, REAL_NAME=%s, GENDER=%s, PLATE_NUM=%s WHERE ID=%s")
                val = (permission, real_name, gender, plate_amount, userid)
                mycursor.execute(sql, val)
            mydb.commit()
            data = mycursor.fetchall()
        except:
            ErrorLogger.logger.error(
                "update_data_to_user_info Encountered error!")
            return -1
        return data

    def add_new_plate(self, plateid):
        try:
            # Connect to databaseb
            mydb = self.connect_to_database()
            mycursor = mydb.cursor()
            # Create table if not exist
            self.create_table_first(mycursor)

            # Actually insert plate into table
            sql = "INSERT INTO Plate_Information(PLATE_ID, LAST_ASSIGNED_USER_ID, AVAILABLE_FOR_ASSIGN, LAST_ASSIGN_TIME, LAST_DEASSIGN_TIME) VALUES (%s, %s, %s, %s, %s)"
            val = (plateid, "NONE", "TRUE", "NONE", "NONE")
            mycursor.execute(sql, val)
            mydb.commit()
            PlateInfoLogger.logger.info(
                "the plate: '" + plateid + "' has been added")
        except:
            ErrorLogger.logger.error(
                "add_new_plate Encountered error!")
            return -1

    def assign_plate_to_user(self, plateid, userid, availability, last_assign_time):
        try:
            # Connect to database
            mydb = self.connect_to_database()
            mycursor = mydb.cursor()
            # Create table if not exist
            self.create_table_first(mycursor)

            # Assign plate to user
            sql = "UPDATE Plate_Information SET LAST_ASSIGNED_USER_ID=%s, AVAILABLE_FOR_ASSIGN=%s, LAST_ASSIGN_TIME=%s WHERE PLATE_ID=%s"
            val = (userid, availability, last_assign_time, plateid)
            mycursor.execute(sql, val)
            mydb.commit()
            PlateInfoLogger.logger.info(
                "the plate: '" + plateid + "' has been assigned to user with userID: " + userid)
            self.update_plate_user_have(userid)
        except:
            ErrorLogger.logger.error(
                "assign_plate_to_user Encountered error!")
            return -1

    def deassign_plate_from_user(self, plateid, availability, last_deassign_time):
        try:
            # Connect to database
            mydb = self.connect_to_database()
            mycursor = mydb.cursor()
            # Create table if not exist
            self.create_table_first(mycursor)

            sql = (
                "UPDATE Plate_Information SET AVAILABLE_FOR_ASSIGN=%s, LAST_DEASSIGN_TIME=%s WHERE PLATE_ID=%s")
            val = (availability, last_deassign_time, plateid)
            mycursor.execute(sql, val)
            mydb.commit()
            PlateInfoLogger.logger.info(
                "the plate: '" + plateid + "' has been deassigned.")
        except:
            ErrorLogger.logger.error(
                "deassign_plate_from_user Encountered error!")
            return -1

    def remove_plate(self, plateid):
        try:
            # Connect to database
            mydb = self.connect_to_database()
            mycursor = mydb.cursor()
            # Create table if not exist
            self.create_table_first(mycursor)

            sql = ("DELETE FROM Plate_Information WHERE PLATE_ID=%s")
            val = (plateid,)
            mycursor.execute(sql, val)
            mydb.commit()
            PlateInfoLogger.logger.info(
                "the plate: '" + plateid + "' has been removed.")
        except:
            ErrorLogger.logger.error(
                "remove_plate Encountered error!")
            return -1

    def update_plate_user_have(self, userid):
        try:
            # Connect to database
            mydb = self.connect_to_database()
            mycursor = mydb.cursor()
            # Create table if not exist
            self.create_table_first(mycursor)

            sql = ("UPDATE User_Information SET PLATE_NUM = ( SELECT count(*) FROM Plate_Information WHERE LAST_ASSIGNED_USER_ID=%s AND AVAILABLE_FOR_ASSIGN = 'FALSE') WHERE ID=%s")
            val = (userid, userid)
            mycursor.execute(sql, val)
            mydb.commit()
        except:
            ErrorLogger.logger.error(
                "update_plate_user_have Encountered error!")
            return -1

    def get_row_number_from_database(self, database, type, value):
        try:
            # Connect to database
            mydb = self.connect_to_database()
            mycursor = mydb.cursor()
            # Create table if not exist
            self.create_table_first(mycursor)
            if(database == login_record_table):
                if(type == "all"):
                    sql = ("SELECT count(*) FROM Login_record")
                    val = ()
                if(type == "id"):
                    sql = (
                        "SELECT count(*) FROM Login_record WHERE ID=%s ORDER BY ID ASC")
                    val = (value,)
                if(type == "status"):
                    sql = (
                        "SELECT count(*) FROM Login_record WHERE LOGIN_STATE=%s ORDER BY ID ASC ")
                    val = (value,)
                if(type == "specific_type_fail" or type == "specific_type_success"):
                    sql = (
                        "SELECT count(*) FROM Login_record WHERE SPECIFIC_TYPE=%s ORDER BY ID ASC ")
                    val = (value,)
            elif(database == user_info_table):
                if(type == "all"):
                    sql = ("SELECT count(*) FROM User_Information")
                    val = ()
                if(type == "id_strict"):
                    sql = (
                        "SELECT count(*) FROM User_Information WHERE ID=%s ORDER BY ID ASC")
                    val = (value,)
                if(type == "id"):
                    sql = (
                        "SELECT count(*) FROM User_Information WHERE ID LIKE %s ORDER BY ID ASC ")
                    val = ('%'+value+'%',)
                if(type == "name"):
                    sql = (
                        "SELECT count(*) FROM User_Information WHERE REAL_NAME LIKE %s ORDER BY REAL_NAME ASC ")
                    val = ('%'+value+'%',)
                if(type == "permission"):
                    sql = (
                        "SELECT count(*) FROM User_Information WHERE PERMISSION=%s ORDER BY ID ASC ")
                    val = (value,)
                if(type == "gender"):
                    sql = (
                        "SELECT count(*) FROM User_Information WHERE GENDER=%s ORDER BY ID ASC ")
                    val = (value,)
            elif(database == plate_info_table):
                if(type == "all"):
                    sql = ("SELECT count(*) FROM Plate_Information")
                    val = ()
                if(type == "user_id"):
                    sql = (
                        "SELECT count(*) FROM Plate_Information WHERE LAST_ASSIGNED_USER_ID=%s ORDER BY LAST_ASSIGNED_USER_ID ASC")
                    val = (value,)
                if(type == "plate_id"):
                    sql = (
                        "SELECT count(*) FROM Plate_Information WHERE PLATE_ID=%s ORDER BY LAST_ASSIGNED_USER_ID ASC ")
                    val = (value,)
                if(type == "availability"):
                    sql = (
                        "SELECT count(*) FROM Plate_Information WHERE AVAILABLE_FOR_ASSIGN=%s ORDER BY LAST_ASSIGNED_USER_ID ASC ")
                    val = (value,)

            mycursor.execute(sql, val)
            data = mycursor.fetchone()
            page_number = data[0]
            return page_number

        except:
            ErrorLogger.logger.error(
                "get_row_number_from_database Encountered error!")
            return -1

    def get_plate_id_user_have(self, userid):
        try:
            # Connect to database
            mydb = self.connect_to_database()
            mycursor = mydb.cursor()
            # Create table if not exist
            self.create_table_first(mycursor)

            sql = "SELECT `PLATE_ID` FROM `Plate_Information`WHERE `LAST_ASSIGNED_USER_ID` = %s AND `AVAILABLE_FOR_ASSIGN` = 'FALSE'"
            val = (userid, )

            mycursor.execute(sql, val)
            data = mycursor.fetchall()
            return data
        except:
            ErrorLogger.logger.error(
                "get_plate_id_user_have Encountered error!")
            return -1


# main
if __name__ == "__main__":
    Login_function = UI_Login_function()
    Info_Editor_function = UI_Info_Editor_function()
    Search_Edit_function = UI_Search_Edit_function()
    Register_function = UI_Register_function()
    Login_History_function = UI_Login_History_function()
    Plate_Info_function = UI_Plate_info_function()
    helper = helper_function()
    SQL_function = MySQL_function()

    # table in database's name
    user_info_table = "User_Information"
    login_record_table = "Login_record"
    plate_info_table = "Plate_Information"

    # logger
    ErrorLogger = logger_class(
        "Error_Logger", logging.ERROR, "Log_Folder/Error.log")
    AdminEditorLogger = logger_class(
        "Admin_Editor_logger", logging.INFO, "Log_Folder/Admin_editor.log")
    PlateInfoLogger = logger_class(
        "Plate_Infor_logger", logging.INFO, "Log_Folder/Plate_Info.log")
    # open login UI
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    Loginui = Ui_Login()
    Loginui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
