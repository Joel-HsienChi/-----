from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
import logging
import datetime
import hashlib
import re
import mysql.connector

formatter = logging.Formatter("%(asctime)s - %(levelname)s %(message)s")

# logger for login ui
Login_logger = logging.getLogger("Login_log")
Login_logger.setLevel(logging.INFO)
Login_logger_file_handler = logging.FileHandler("Login.log")
Login_logger_file_handler.setFormatter(formatter)
Login_logger.addHandler(Login_logger_file_handler)

# logger for Register ui
Register_logger = logging.getLogger("Register_log")
Register_logger.setLevel(logging.INFO)
Register_file_handler = logging.FileHandler("Register.log")
Register_file_handler.setFormatter(formatter)
Register_logger.addHandler(Register_file_handler)

# logger for normal user info editor ui
Info_Editor_logger = logging.getLogger("Info_editor_log")
Info_Editor_logger.setLevel(logging.INFO)
Info_Editor_file_handler = logging.FileHandler("Info_editor.log")
Info_Editor_file_handler.setFormatter(formatter)
Info_Editor_logger.addHandler(Info_Editor_file_handler)


Login_logger.info("test1")
Info_Editor_logger.info("test2")
Register_logger.info("test3")

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
        self.Error_Message_for_password.setGeometry(QtCore.QRect(50, 150, 241, 21))
        self.Error_Message_for_password.setObjectName("Error_Message_for_password")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(180, 110, 111, 31))
        self.checkBox.setObjectName("checkBox")
        self.Error_Message_for_permission = QtWidgets.QLabel(self.centralwidget)
        self.Error_Message_for_permission.setGeometry(QtCore.QRect(100, 150, 141, 21))
        self.Error_Message_for_permission.setObjectName("Error_Message_for_permission")
        self.Error_Message_for_ID = QtWidgets.QLabel(self.centralwidget)
        self.Error_Message_for_ID.setGeometry(QtCore.QRect(120, 150, 141, 21))
        self.Error_Message_for_ID.setObjectName("Error_Message_for_ID")
        Login.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)


        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

        # hide the error message
        self.Error_Message_for_password.setHidden(True) 
        self.Error_Message_for_permission.setHidden(True) 
        self.Error_Message_for_ID.setHidden(True)

        # connect button to function 
        self.Login_Button.clicked.connect(lambda: Login_function.check_ID_password_function(self.UserID_Input.text(), self.Password_Input.text()))
    
    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.Login_Button.setText(_translate("Login", "Login"))
        self.Login_Button.setShortcut(_translate("Login", "Return"))
        self.UserID_Label.setText(_translate("Login", "UserID"))
        self.Password_Label.setText(_translate("Login", "Password"))
        self.Error_Message_for_password.setText(_translate("Login", "Wrong Password! Please try again!"))
        self.checkBox.setText(_translate("Login", "Admin mode"))
        self.Error_Message_for_permission.setText(_translate("Login", "You are not an Admin!"))
        self.Error_Message_for_ID.setText(_translate("Login", "ID doesn\'t exist!"))

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
        self.Register_success_message.setGeometry(QtCore.QRect(60, 350, 211, 20))
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


        # connect button to function
        self.Add_a_user_button.clicked.connect(lambda: Register_function.press_register(self.ID_input.text(), self.default_password, self.Name_input.text()))            
    
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
        self.Register_error_message.setText(_translate("Register", "Action failed!"))
        self.Register_success_message.setText(_translate("Register", "Successfully added the user!"))
        self.Other_button.setText(_translate("Register", "Others"))

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
        self.Display_table.setGeometry(QtCore.QRect(40, 30, 741, 71))
        self.Display_table.setMinimumSize(QtCore.QSize(0, 0))
        self.Display_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
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
        
        # hide the error message
        self.Input_Invalid.setHidden(True)

        # connect button to function 
        self.Save_change_button.clicked.connect(lambda: Info_Editor_function.get_data_from_table())
    
    def retranslateUi(self, Info_Editor):
        _translate = QtCore.QCoreApplication.translate
        Info_Editor.setWindowTitle(_translate("Info_Editor", "Info_Editor"))
        self.Save_change_button.setText(_translate("Info_Editor", "Save change"))
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

class Ui_Concentrate_Advance(object):
    current_user_ID = ''
    def setupUi(self, Concentrate_Advance):
        Concentrate_Advance.setObjectName("Concentrate_Advance")
        Concentrate_Advance.resize(1350, 800)
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
        self.buttonGroup = QtWidgets.QButtonGroup(Concentrate_Advance)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.Female_button)
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
        self.buttonGroup.addButton(self.Others_button)
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
        self.buttonGroup_2 = QtWidgets.QButtonGroup(Concentrate_Advance)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.Admin_button)
        self.Edit_error_message = QtWidgets.QLabel(self.Search_Edit_Tab)
        self.Edit_error_message.setGeometry(QtCore.QRect(200, 670, 81, 16))
        self.Edit_error_message.setMinimumSize(QtCore.QSize(71, 16))
        self.Edit_error_message.setObjectName("Edit_error_message")
        self.ID_label = QtWidgets.QLabel(self.Search_Edit_Tab)
        self.ID_label.setGeometry(QtCore.QRect(50, 20, 61, 16))
        self.ID_label.setMinimumSize(QtCore.QSize(61, 16))
        self.ID_label.setObjectName("ID_label")
        self.Display_table = QtWidgets.QTableWidget(self.Search_Edit_Tab)
        self.Display_table.setGeometry(QtCore.QRect(320, 10, 1000, 730))
        self.Display_table.setMinimumSize(QtCore.QSize(800, 361))
        self.Display_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
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
        self.Gender_button = QtWidgets.QPushButton(self.Search_Edit_Tab)
        self.Gender_button.setGeometry(QtCore.QRect(100, 460, 160, 30))
        self.Gender_button.setMinimumSize(QtCore.QSize(160, 30))
        self.Gender_button.setObjectName("Gender_button")
        self.Male_button = QtWidgets.QRadioButton(self.Search_Edit_Tab)
        self.Male_button.setGeometry(QtCore.QRect(140, 380, 100, 20))
        self.Male_button.setMinimumSize(QtCore.QSize(100, 20))
        self.Male_button.setObjectName("Male_button")
        self.buttonGroup.addButton(self.Male_button)
        self.Permission_label = QtWidgets.QLabel(self.Search_Edit_Tab)
        self.Permission_label.setGeometry(QtCore.QRect(50, 250, 81, 20))
        self.Permission_label.setMinimumSize(QtCore.QSize(81, 20))
        self.Permission_label.setObjectName("Permission_label")
        self.User_button = QtWidgets.QRadioButton(self.Search_Edit_Tab)
        self.User_button.setGeometry(QtCore.QRect(140, 250, 100, 20))
        self.User_button.setMinimumSize(QtCore.QSize(100, 20))
        self.User_button.setObjectName("User_button")
        self.buttonGroup_2.addButton(self.User_button)
        self.Save_change_button = QtWidgets.QPushButton(self.Search_Edit_Tab)
        self.Save_change_button.setGeometry(QtCore.QRect(20, 660, 161, 32))
        self.Save_change_button.setMinimumSize(QtCore.QSize(161, 32))
        self.Save_change_button.setObjectName("Save_change_button")
        self.Name_input = QtWidgets.QLineEdit(self.Search_Edit_Tab)
        self.Name_input.setGeometry(QtCore.QRect(120, 140, 141, 21))
        self.Name_input.setMinimumSize(QtCore.QSize(141, 21))
        self.Name_input.setText("")
        self.Name_input.setObjectName("Name_input")
        Concentrate_Advance.addTab(self.Search_Edit_Tab, "")
        self.Login_History_Tab = QtWidgets.QWidget()
        self.Login_History_Tab.setObjectName("Login_History_Tab")
        self.ID_input_login_history = QtWidgets.QLineEdit(self.Login_History_Tab)
        self.ID_input_login_history.setGeometry(QtCore.QRect(120, 20, 141, 21))
        self.ID_input_login_history.setMinimumSize(QtCore.QSize(141, 21))
        self.ID_input_login_history.setText("")
        self.ID_input_login_history.setObjectName("ID_input_login_history")        
        self.Password_doesnt_match_ID_button = QtWidgets.QRadioButton(self.Login_History_Tab)
        self.Password_doesnt_match_ID_button.setGeometry(QtCore.QRect(50, 290, 211, 20))
        self.Password_doesnt_match_ID_button.setMinimumSize(QtCore.QSize(100, 20))
        self.Password_doesnt_match_ID_button.setObjectName("Password_doesnt_match_ID_button")
        self.Success_button = QtWidgets.QRadioButton(self.Login_History_Tab)
        self.Success_button.setGeometry(QtCore.QRect(50, 140, 100, 20))
        self.Success_button.setMinimumSize(QtCore.QSize(100, 20))
        self.Success_button.setObjectName("Success_button")
        self.ID_label_login_history = QtWidgets.QLabel(self.Login_History_Tab)
        self.ID_label_login_history.setGeometry(QtCore.QRect(50, 20, 61, 16))
        self.ID_label_login_history.setMinimumSize(QtCore.QSize(61, 16))
        self.ID_label_login_history.setObjectName("ID_label_login_history")
        self.ID_doesnt_exist_button = QtWidgets.QRadioButton(self.Login_History_Tab)
        self.ID_doesnt_exist_button.setGeometry(QtCore.QRect(50, 260, 121, 20))
        self.ID_doesnt_exist_button.setMinimumSize(QtCore.QSize(100, 20))
        self.ID_doesnt_exist_button.setObjectName("ID_doesnt_exist_button")
        self.ID_search_button_login_history = QtWidgets.QPushButton(self.Login_History_Tab)
        self.ID_search_button_login_history.setGeometry(QtCore.QRect(120, 60, 140, 30))
        self.ID_search_button_login_history.setMinimumSize(QtCore.QSize(0, 0))
        self.ID_search_button_login_history.setObjectName("ID_search_button_login_history")
        self.Display_Login_info = QtWidgets.QTableWidget(self.Login_History_Tab)
        self.Display_Login_info.setGeometry(QtCore.QRect(320, 10, 1000, 730))
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
        self.Show_all_button_login_history = QtWidgets.QPushButton(self.Login_History_Tab)
        self.Show_all_button_login_history.setGeometry(QtCore.QRect(120, 530, 140, 30))
        self.Show_all_button_login_history.setMinimumSize(QtCore.QSize(140, 30))
        self.Show_all_button_login_history.setObjectName("Show_all_button_login_history")
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
        self.User_enter_advance_button = QtWidgets.QRadioButton(self.Login_History_Tab)
        self.User_enter_advance_button.setGeometry(QtCore.QRect(50, 320, 241, 20))
        self.User_enter_advance_button.setMinimumSize(QtCore.QSize(100, 20))
        self.User_enter_advance_button.setObjectName("User_enter_advance_button")
        self.Success_type_button = QtWidgets.QPushButton(self.Login_History_Tab)
        self.Success_type_button.setGeometry(QtCore.QRect(120, 470, 161, 32))
        self.Success_type_button.setMinimumSize(QtCore.QSize(141, 32))
        self.Success_type_button.setObjectName("Success_type_button")
        self.Normal_login_button = QtWidgets.QRadioButton(self.Login_History_Tab)
        self.Normal_login_button.setGeometry(QtCore.QRect(50, 410, 121, 20))
        self.Normal_login_button.setMinimumSize(QtCore.QSize(100, 20))
        self.Normal_login_button.setObjectName("Normal_login_button")
        self.Advance_login_button = QtWidgets.QRadioButton(self.Login_History_Tab)
        self.Advance_login_button.setGeometry(QtCore.QRect(50, 440, 121, 20))
        self.Advance_login_button.setMinimumSize(QtCore.QSize(100, 20))
        self.Advance_login_button.setObjectName("Advance_login_button")
        self.line_8 = QtWidgets.QFrame(self.Login_History_Tab)
        self.line_8.setGeometry(QtCore.QRect(60, 500, 200, 20))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        Concentrate_Advance.addTab(self.Login_History_Tab, "")
        self.Plate_Scan_Tab = QtWidgets.QWidget()
        self.Plate_Scan_Tab.setObjectName("Plate_Scan_Tab")
        self.Display_Plate_Info = QtWidgets.QTableWidget(self.Plate_Scan_Tab)
        self.Display_Plate_Info.setGeometry(QtCore.QRect(320, 10, 1000, 730))
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
        self.Show_all_button_Plate_Info = QtWidgets.QPushButton(self.Plate_Scan_Tab)
        self.Show_all_button_Plate_Info.setGeometry(QtCore.QRect(20, 370, 180, 30))
        self.Show_all_button_Plate_Info.setMinimumSize(QtCore.QSize(150, 30))
        self.Show_all_button_Plate_Info.setObjectName("Show_all_button_Plate_Info")
        self.Plate_ID_label_Plate_Info = QtWidgets.QLabel(self.Plate_Scan_Tab)
        self.Plate_ID_label_Plate_Info.setGeometry(QtCore.QRect(50, 140, 61, 16))
        self.Plate_ID_label_Plate_Info.setMinimumSize(QtCore.QSize(61, 16))
        self.Plate_ID_label_Plate_Info.setObjectName("Plate_ID_label_Plate_Info")
        self.ID_search_button_Plate_Info = QtWidgets.QPushButton(self.Plate_Scan_Tab)
        self.ID_search_button_Plate_Info.setGeometry(QtCore.QRect(120, 60, 140, 30))
        self.ID_search_button_Plate_Info.setMinimumSize(QtCore.QSize(0, 0))
        self.ID_search_button_Plate_Info.setObjectName("ID_search_button_Plate_Info")
        self.Plate_ID_search_button_Plate_Info = QtWidgets.QPushButton(self.Plate_Scan_Tab)
        self.Plate_ID_search_button_Plate_Info.setGeometry(QtCore.QRect(120, 180, 140, 30))
        self.Plate_ID_search_button_Plate_Info.setMinimumSize(QtCore.QSize(140, 30))
        self.Plate_ID_search_button_Plate_Info.setObjectName("Plate_ID_search_button_Plate_Info")
        self.ID_label_Plate_Info = QtWidgets.QLabel(self.Plate_Scan_Tab)
        self.ID_label_Plate_Info.setGeometry(QtCore.QRect(50, 20, 61, 16))
        self.ID_label_Plate_Info.setMinimumSize(QtCore.QSize(61, 16))
        self.ID_label_Plate_Info.setObjectName("ID_label_Plate_Info")
        self.line_9 = QtWidgets.QFrame(self.Plate_Scan_Tab)
        self.line_9.setGeometry(QtCore.QRect(60, 220, 201, 20))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.ID_input_Plate_Info = QtWidgets.QLineEdit(self.Plate_Scan_Tab)
        self.ID_input_Plate_Info.setGeometry(QtCore.QRect(120, 20, 141, 21))
        self.ID_input_Plate_Info.setMinimumSize(QtCore.QSize(141, 21))
        self.ID_input_Plate_Info.setText("")
        self.ID_input_Plate_Info.setObjectName("ID_input_Plate_Info")
        self.line_10 = QtWidgets.QFrame(self.Plate_Scan_Tab)
        self.line_10.setGeometry(QtCore.QRect(60, 100, 200, 20))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.Plate_ID_input_Plate_Info = QtWidgets.QLineEdit(self.Plate_Scan_Tab)
        self.Plate_ID_input_Plate_Info.setGeometry(QtCore.QRect(120, 140, 141, 21))
        self.Plate_ID_input_Plate_Info.setMinimumSize(QtCore.QSize(141, 21))
        self.Plate_ID_input_Plate_Info.setText("")
        self.Plate_ID_input_Plate_Info.setObjectName("Plate_ID_input_Plate_Info")
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
        self.Deassign_plate_from_user = QtWidgets.QPushButton(self.Plate_Scan_Tab)
        self.Deassign_plate_from_user.setGeometry(QtCore.QRect(20, 410, 180, 30))
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
        Concentrate_Advance.addTab(self.Plate_Scan_Tab, "")
        self.buttongroup_permission = QtWidgets.QButtonGroup(Concentrate_Advance)
        self.buttongroup_permission.setObjectName("buttongroup_permission")
        self.buttongroup_permission.addButton(self.Admin_button)
        self.buttongroup_permission.addButton(self.User_button)
        self.buttongroup_gender = QtWidgets.QButtonGroup(Concentrate_Advance)
        self.buttongroup_gender.setObjectName("buttongroup_gender")
        self.buttongroup_gender.addButton(self.Female_button)
        self.buttongroup_gender.addButton(self.Male_button)
        self.buttongroup_gender.addButton(self.Others_button)
        self.buttongroup_success_type = QtWidgets.QButtonGroup(Concentrate_Advance)
        self.buttongroup_success_type.setObjectName("buttongroup_success_type")
        self.buttongroup_success_type.addButton(self.Normal_login_button)
        self.buttongroup_success_type.addButton(self.Advance_login_button)
        self.buttongroup_fail_type = QtWidgets.QButtonGroup(Concentrate_Advance)
        self.buttongroup_fail_type.setObjectName("buttongroup_fail_type")
        self.buttongroup_fail_type.addButton(self.Password_doesnt_match_ID_button)
        self.buttongroup_fail_type.addButton(self.User_enter_advance_button)
        self.buttongroup_fail_type.addButton(self.ID_doesnt_exist_button)


        self.retranslateUi(Concentrate_Advance)
        Concentrate_Advance.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Concentrate_Advance)

# Modding for Search/Edit
        # adjust column size
        header = self.Display_table.horizontalHeader()
        for i in range(5):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)

        # hide the error message
        self.Edit_error_message.setHidden(True)

        # connect button to function
        self.Show_all_button.clicked.connect(lambda: Search_Edit_function.show_user("all", None))
        self.ID_search_button.clicked.connect(lambda: Search_Edit_function.show_user("id",self.ID_input.text()))
        self.Name_search_button.clicked.connect(lambda: Search_Edit_function.show_user("name",self.Name_input.text()))
        self.Gender_button.clicked.connect(lambda: Search_Edit_function.show_user("gender", None))
        self.Permission_button.clicked.connect(lambda: Search_Edit_function.show_user("permission", None))
        self.Save_change_button.clicked.connect(lambda: Search_Edit_function.get_data_from_table())
        self.Delete_User_button.clicked.connect(lambda: Search_Edit_function.show_delete_confirm())
        self.Add_User_button.clicked.connect(lambda: Search_Edit_function.open_Register_window())

        # show all info initially 
        Search_Edit_function.show_user("all", None)


# Modding for Login History
        # adjust column size
        header = self.Display_Login_info.horizontalHeader() 
        for i in range(3):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)    
   
        # connect button to function
        self.Show_all_button_login_history.clicked.connect(lambda: Login_History_function.show_login_history("all", None))
        self.ID_search_button_login_history.clicked.connect(lambda: Login_History_function.show_login_history("id", self.ID_input_login_history.text()))
        self.Status_show_button.clicked.connect(lambda: Login_History_function.show_login_history("status", None))
        self.Fail_type_button.clicked.connect(lambda: Login_History_function.show_login_history("specific_type", None))
        self.Success_type_button.clicked.connect(lambda: Login_History_function.show_login_history("specific_type", None))

        # let table be read only
        self.Display_Login_info.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        # show all info initially 
        Login_History_function.show_login_history("all", None)

# Modding for plate info
        # adjust column size
        header = self.Display_Plate_Info.horizontalHeader() 
        for i in range(5):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)

        # connect button to function
        self.Show_all_button_Plate_Info.clicked.connect(lambda: Plate_Info_function.show_plate_info("all", None))
        self.ID_search_button_Plate_Info.clicked.connect(lambda: Plate_Info_function.show_plate_info("user_id", self.ID_input_Plate_Info.text()))
        self.Plate_ID_search_button_Plate_Info.clicked.connect(lambda: Plate_Info_function.show_plate_info("plate_id", self.Plate_ID_input_Plate_Info.text()))
        self.Availability_button.clicked.connect(lambda: Plate_Info_function.show_plate_info("availability", None))
        self.Add_new_plate.clicked.connect(lambda: Plate_Info_function.show_add_new_plate_window())
        self.Assign_plate_to_user.clicked.connect(lambda: Plate_Info_function.show_assign_plate_to_user_window())
        self.Deassign_plate_from_user.clicked.connect(lambda: Plate_Info_function.show_deassign_plate_to_user_window())
        self.Remove_plate.clicked.connect(lambda: Plate_Info_function.show_delete_plate_confirm())

        # let table be read only
        self.Display_Plate_Info.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        

        # hide the message
        self.Assign_fail_label.setHidden(True)
        self.Assign_success_label.setHidden(True)

        # show all info initially 
        Plate_Info_function.show_plate_info("all", None)

    def retranslateUi(self, Concentrate_Advance):
        _translate = QtCore.QCoreApplication.translate
        Concentrate_Advance.setWindowTitle(_translate("Concentrate_Advance", "Concentrate_Advance"))
        self.Delete_User_button.setText(_translate("Concentrate_Advance", "Delete a User"))
        self.Gender_label.setText(_translate("Concentrate_Advance", "Gender"))
        self.Show_all_button.setText(_translate("Concentrate_Advance", "Show All Users"))
        self.Add_User_button.setText(_translate("Concentrate_Advance", "Add a User"))
        self.Name_label.setText(_translate("Concentrate_Advance", "Name"))
        self.Female_button.setText(_translate("Concentrate_Advance", "Female"))
        self.Permission_button.setText(_translate("Concentrate_Advance", "Search by Permission"))
        self.Name_search_button.setText(_translate("Concentrate_Advance", "Search by Name"))
        self.Others_button.setText(_translate("Concentrate_Advance", "Others"))
        self.ID_search_button.setText(_translate("Concentrate_Advance", "Search by ID"))
        self.Admin_button.setText(_translate("Concentrate_Advance", "Admin"))
        self.Edit_error_message.setText(_translate("Concentrate_Advance", "Invalid input!"))
        self.ID_label.setText(_translate("Concentrate_Advance", "ID"))
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
        self.Gender_button.setText(_translate("Concentrate_Advance", "Search by Gender"))
        self.Male_button.setText(_translate("Concentrate_Advance", "Male"))
        self.Permission_label.setText(_translate("Concentrate_Advance", "Permission"))
        self.User_button.setText(_translate("Concentrate_Advance", "User"))
        self.Save_change_button.setText(_translate("Concentrate_Advance", "Save change"))
        Concentrate_Advance.setTabText(Concentrate_Advance.indexOf(self.Search_Edit_Tab), _translate("Concentrate_Advance", "User info"))
        self.Password_doesnt_match_ID_button.setText(_translate("Concentrate_Advance", "Password doesn\'t match ID"))
        self.Success_button.setText(_translate("Concentrate_Advance", "Success"))
        self.ID_label_login_history.setText(_translate("Concentrate_Advance", "ID"))
        self.ID_doesnt_exist_button.setText(_translate("Concentrate_Advance", "ID doesn\'t exist"))
        self.ID_search_button_login_history.setText(_translate("Concentrate_Advance", "Search by ID"))
        item = self.Display_Login_info.horizontalHeaderItem(0)
        item.setText(_translate("Concentrate_Advance", "Login_ID"))
        item = self.Display_Login_info.horizontalHeaderItem(1)
        item.setText(_translate("Concentrate_Advance", "Login_Time"))
        item = self.Display_Login_info.horizontalHeaderItem(2)
        item.setText(_translate("Concentrate_Advance", "Login_Status"))
        item = self.Display_Login_info.horizontalHeaderItem(3)
        item.setText(_translate("Concentrate_Advance", "Fail_Type"))
        self.Fail_button.setText(_translate("Concentrate_Advance", "Fail "))
        self.Fail_type_button.setText(_translate("Concentrate_Advance", "Show by Fail type"))
        self.Status_show_button.setText(_translate("Concentrate_Advance", "Show by Status"))
        self.Show_all_button_login_history.setText(_translate("Concentrate_Advance", "Show All"))
        self.User_enter_advance_button.setText(_translate("Concentrate_Advance", "Normal user entered Advance mode"))
        self.Success_type_button.setText(_translate("Concentrate_Advance", "Show by Success type"))
        self.Normal_login_button.setText(_translate("Concentrate_Advance", "Normal login"))
        self.Advance_login_button.setText(_translate("Concentrate_Advance", "Advance login"))
        Concentrate_Advance.setTabText(Concentrate_Advance.indexOf(self.Login_History_Tab), _translate("Concentrate_Advance", "Login History"))
        item = self.Display_Plate_Info.horizontalHeaderItem(0)
        item.setText(_translate("Concentrate_Advance", "Checkbox"))
        item = self.Display_Plate_Info.horizontalHeaderItem(1)
        item.setText(_translate("Concentrate_Advance", "Plate_ID"))
        item = self.Display_Plate_Info.horizontalHeaderItem(2)
        item.setText(_translate("Concentrate_Advance", "Last_Assigned_User_ID"))
        item = self.Display_Plate_Info.horizontalHeaderItem(3)
        item.setText(_translate("Concentrate_Advance", "Avaliable_for_assign"))
        item = self.Display_Plate_Info.horizontalHeaderItem(4)
        item.setText(_translate("Concentrate_Advance", "Last_Assign_Time"))
        item = self.Display_Plate_Info.horizontalHeaderItem(5)
        item.setText(_translate("Concentrate_Advance", "Last_Deassign_Time"))
        self.Show_all_button_Plate_Info.setText(_translate("Concentrate_Advance", "Show All"))
        self.Plate_ID_label_Plate_Info.setText(_translate("Concentrate_Advance", "Plate ID"))
        self.ID_search_button_Plate_Info.setText(_translate("Concentrate_Advance", "Search by ID"))
        self.Plate_ID_search_button_Plate_Info.setText(_translate("Concentrate_Advance", "Search by Plate ID"))
        self.ID_label_Plate_Info.setText(_translate("Concentrate_Advance", "ID"))
        self.Availability_button.setText(_translate("Concentrate_Advance", "Show by Availability"))
        self.Available_FALSE.setText(_translate("Concentrate_Advance", "FALSE"))
        self.Available_TRUE.setText(_translate("Concentrate_Advance", "TRUE"))
        self.Assign_plate_to_user.setText(_translate("Concentrate_Advance", "Assign plate to user"))
        self.Deassign_plate_from_user.setText(_translate("Concentrate_Advance", "Deassign plate"))
        self.Add_new_plate.setText(_translate("Concentrate_Advance", "Add new plate"))
        self.Remove_plate.setText(_translate("Concentrate_Advance", "Remove plate"))
        self.Assign_fail_label.setText(_translate("Concentrate_Advance", "Failed!"))
        self.Assign_success_label.setText(_translate("Concentrate_Advance", "Success"))
        Concentrate_Advance.setTabText(Concentrate_Advance.indexOf(self.Plate_Scan_Tab), _translate("Concentrate_Advance", "Plate Scan"))



class UI_Login_function:
    def check_ID_password_function (self, userid, password):

        # initialize 
        ID_password_match = False
        ID_is_admin = False
        ID_exist = SQL_function.check_ID_exist(userid)

        # encrypt the password
        encrypted_password = helper.encode_password(password)

        # check if id and password is correct
        ID_password_match = SQL_function.check_ID_password(userid, encrypted_password)
        # error handler
        if(ID_password_match == -1):
            return

        # check if user is admin
        ID_is_admin = SQL_function.check_ID_is_admin(userid)
        # error handler
        if(ID_is_admin == -1):
            return
        
        if(ID_password_match is True):
            # enter Advance mode
            if(ID_is_admin is True and Loginui.checkBox.isChecked()):
                SQL_function.add_login_record(userid, "SUCCESS", "Login with Advance mode")
                self.open_Concentrate_Advance_window()
                Login.close()
            # Fail: Not admin but try to entering advance mode
            elif(ID_is_admin is False and self.checkBox.isChecked()):
                SQL_function.add_login_record(userid, "FAIL", "A normal user tries to enter Advance mode")
                Loginui.Error_Message_for_permission.setHidden(False) 
                Loginui.Error_Message_for_password.setHidden(True)
                Loginui.Error_Message_for_ID.setHidden(True)
                return
            # Normal user mode
            else:
                self.show_normal_welcome_message()
                SQL_function.add_login_record(userid, "SUCCESS", "Login with normal user mode")
                Login.close()
        # Fail: ID doesn't exist        
        elif(ID_exist is False):
            SQL_function.add_login_record(userid, "FAIL", "ID doesn't exist")
            # display the error message
            Loginui.Error_Message_for_permission.setHidden(True) 
            Loginui.Error_Message_for_password.setHidden(True)
            Loginui.Error_Message_for_ID.setHidden(False)
            return
        # Fail: ID doesn't match password
        elif(ID_password_match is False):
            SQL_function.add_login_record(userid, "FAIL", "ID and Password doesn't match")
            # display the error message
            Loginui.Error_Message_for_password.setHidden(False) 
            Loginui.Error_Message_for_permission.setHidden(True)
            Loginui.Error_Message_for_ID.setHidden(True)
            return
    
    def open_Concentrate_Advance_window(self):
        self.Concentrate_Advance = QtWidgets.QTabWidget()
        self.Concentrate_Advance_ui = Ui_Concentrate_Advance()
        self.Concentrate_Advance_ui.current_user_ID = Loginui.UserID_Input.text()
        self.Concentrate_Advance_ui.setupUi(self.Concentrate_Advance)
        self.Concentrate_Advance.show()

    def open_Info_Editor_window(self):
        self.Info_Editor = QtWidgets.QWidget()
        self.Info_Editor_ui = Ui_Info_Editor()
        self.Info_Editor_ui.current_user_ID = Loginui.UserID_Input.text()
        self.Info_Editor_ui.setupUi(self.Info_Editor)  
        self.Info_Editor.show()
    
    def show_normal_welcome_message(self):
        confirm = QMessageBox()
        confirm.setWindowTitle("Welcome window")
        confirm.setText("Welcome! " + Loginui.UserID_Input.text() + "! Display edit window?")
        confirm.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        confirm.setDefaultButton(QMessageBox.Cancel)
        confirm.accepted.connect(lambda: self.open_Info_Editor_window())
        confirm.accepted.connect(lambda: Info_Editor_function.show_user_info_into_table())
        x = confirm.exec_()
        
class UI_Info_Editor_function:
    def show_user_info_into_table(self):
        data = SQL_function.get_data_from_user_info("id_strict", Login_function.Info_Editor_ui.current_user_ID)
        self.insert_data_into_table_normal_edit(data)
        helper.lock_the_Column(Login_function.Info_Editor_ui.Display_table, 1)
        helper.lock_the_Column(Login_function.Info_Editor_ui.Display_table, 3)   

    def insert_data_into_table_normal_edit(self, data):
        # initialize the table
        Login_function.Info_Editor_ui.Display_table.setRowCount(0) 
        row = 0
        self.check_button_array_normal_edit = []
        for login_record in data:
            Login_function.Info_Editor_ui.Display_table.insertRow(row)
            Login_function.Info_Editor_ui.Display_table.setItem(row, 1, QtWidgets.QTableWidgetItem(login_record[0]))
            Login_function.Info_Editor_ui.Display_table.setItem(row, 2, QtWidgets.QTableWidgetItem("************"))
            Login_function.Info_Editor_ui.Display_table.setItem(row, 3, QtWidgets.QTableWidgetItem(login_record[2]))
            Login_function.Info_Editor_ui.Display_table.setItem(row, 4, QtWidgets.QTableWidgetItem(login_record[3]))
            Login_function.Info_Editor_ui.Display_table.setItem(row, 5, QtWidgets.QTableWidgetItem(login_record[4]))     
            Login_function.Info_Editor_ui.Display_table.setItem(row, 6, QtWidgets.QTableWidgetItem(str(login_record[5]))) 
            
            # set a button to table
            check_box = QtWidgets.QCheckBox()
            Login_function.Info_Editor_ui.Display_table.setCellWidget(row, 0, check_box)
            self.check_button_array_normal_edit.append(check_box)
            row = row+1

    def get_data_from_table(self):
        # go through entire table row by row
        for row in range(Login_function.Info_Editor_ui.Display_table.rowCount()):
            data = []
            for column in range(Login_function.Info_Editor_ui.Display_table.columnCount()):
                if(Login_function.Info_Editor_ui.Display_table.item(row, column) != None):
                    data.append(Login_function.Info_Editor_ui.Display_table.item(row, column).text())

            # check if check box is checked (防呆機制)
            if(self.check_button_array_normal_edit[row].isChecked()):
                # check if input permission and gender fit format
                if(data[2] == "USER" or data[2] == "ADMIN"):
                    if(data[4] == "MALE" or data[4] == "FEMALE" or data[4] == "OTHERS"):
                        # update name, gender, and permission
                        SQL_function.update_data_to_user_info(data[0], None, data[2], data[3], data[4], data[5])
                        Login_function.Info_Editor_ui.Input_Invalid.setHidden(True)

                else:
                    Login_function.Info_Editor_ui.Input_Invalid.setHidden(False)
                    return

                # check if password had been changed
                if(data[1] != "************"):
                    # check if edited password fit format
                    if(helper.check_password_availability( data[1])):
                        SQL_function.update_data_to_user_info(data[0], helper.encode_password(data[1]), data[2], data[3], data[4], data[5])
                        Login_function.Info_Editor_ui.Input_Invalid.setHidden(True)
                    else:
                        Login_function.Info_Editor_ui.Input_Invalid.setHidden(False)
                        return
        self.show_user_info_into_table()
  
class UI_Search_Edit_function:
# Function for Search/Edit
    def show_user(self, type, value):       
        if(type == "permission"):
            if(Login_function.Concentrate_Advance_ui.User_button.isChecked()):
                data = SQL_function.get_data_from_user_info( type, "USER")
            elif(Login_function.Concentrate_Advance_ui.Admin_button.isChecked()):  
                data = SQL_function.get_data_from_user_info( type, "ADMIN")
            else:
                data = SQL_function.get_data_from_user_info(type, None)
        elif(type == "gender"):
            if(Login_function.Concentrate_Advance_ui.Male_button.isChecked()):
                data = SQL_function.get_data_from_user_info(type, "MALE")
            elif(Login_function.Concentrate_Advance_ui.Female_button.isChecked()):  
                data = SQL_function.get_data_from_user_info(type, "FEMALE")
            elif(Login_function.Concentrate_Advance_ui.Others_button.isChecked()):
                data = SQL_function.get_data_from_user_info(type, "OTHERS")
            else:
                data = SQL_function.get_data_from_user_info(type, None)
        else:
            data = SQL_function.get_data_from_user_info(type, value)
        
        self.insert_data_into_table_Search_Edit(data)
        helper.lock_the_Column(Login_function.Concentrate_Advance_ui.Display_table, 1)
        helper.lock_the_Column(Login_function.Concentrate_Advance_ui.Display_table, 6)

# Login_function.Concentrate_Advance_ui

    def insert_data_into_table_Search_Edit(self, data):
        # initialize the table
        Login_function.Concentrate_Advance_ui.Display_table.setRowCount(0) 
        row = 0
        self.check_button_array_search_edit = []
        for login_record in data:
            Login_function.Concentrate_Advance_ui.Display_table.insertRow(row)
            Login_function.Concentrate_Advance_ui.Display_table.setItem(row, 1, QtWidgets.QTableWidgetItem(login_record[0]))
            Login_function.Concentrate_Advance_ui.Display_table.setItem(row, 2, QtWidgets.QTableWidgetItem("************"))
            Login_function.Concentrate_Advance_ui.Display_table.setItem(row, 3, QtWidgets.QTableWidgetItem(login_record[2]))
            Login_function.Concentrate_Advance_ui.Display_table.setItem(row, 4, QtWidgets.QTableWidgetItem(login_record[3]))
            Login_function.Concentrate_Advance_ui.Display_table.setItem(row, 5, QtWidgets.QTableWidgetItem(login_record[4]))     
            Login_function.Concentrate_Advance_ui.Display_table.setItem(row, 6, QtWidgets.QTableWidgetItem(str(login_record[5]))) 
            
            # set a button to table
            check_box = QtWidgets.QCheckBox()
            Login_function.Concentrate_Advance_ui.Display_table.setCellWidget(row, 0, check_box)
            self.check_button_array_search_edit.append(check_box)
            row = row+1
            SQL_function.update_plate_user_have(login_record[0])

    def get_data_from_table(self):
        # go through entire table row by row
        for row in range(Login_function.Concentrate_Advance_ui.Display_table.rowCount()):
            data = []
            for column in range(Login_function.Concentrate_Advance_ui.Display_table.columnCount()):
                if(Login_function.Concentrate_Advance_ui.Display_table.item(row, column) != None):
                    data.append(Login_function.Concentrate_Advance_ui.Display_table.item(row, column).text())

            # update plate_number_nomatter_what
            SQL_function.update_plate_user_have(data[0])
            # check if check box is checked (防呆機制)
            if(self.check_button_array_search_edit[row].isChecked()):
                # check if input permission and gender fit format
                if((data[2] == "USER" or data[2] == "ADMIN")and(data[4] == "MALE" or data[4] == "FEMALE" or data[4] == "OTHERS")):
                    # update name, gender, and permission
                    SQL_function.update_data_to_user_info(data[0], None, data[2], data[3], data[4], data[5])
                    Login_function.Concentrate_Advance_ui.Edit_error_message.setHidden(True)
                else:
                    Login_function.Concentrate_Advance_ui.Edit_error_message.setHidden(False)
                    return
                # check if password had been changed
                if(data[1] != "************"):
                    # check if edited password fit format
                    if(SQL_function.check_password_availability(data[1])):
                        SQL_function.update_data_to_user_info(data[0], helper.encode_password(data[1]), data[2], data[3], data[4], data[5])
                        Login_function.Concentrate_Advance_ui.Edit_error_message.setHidden(True)
                    else:
                        Login_function.Concentrate_Advance_ui.Edit_error_message.setHidden(False)
                        return
            
        self.show_user("all", None)

    def open_Register_window(self):
        self.Register = QtWidgets.QWidget()
        self.Register_ui = Ui_Register()
        self.Register_ui.setupUi(self.Register)
        self.Register.show()

    def delete_users(self):
        # go through entire table row by row
        for row in range(Login_function.Concentrate_Advance_ui.Display_table.rowCount()):
            data = []
            for column in range(Login_function.Concentrate_Advance_ui.Display_table.columnCount()):
                if(Login_function.Concentrate_Advance_ui.Display_table.item(row, column) != None):
                    data.append(Login_function.Concentrate_Advance_ui.Display_table.item(row, column).text())
            if(self.check_button_array_search_edit[row].isChecked()):
                SQL_function.remove_user(data[0])

    def show_delete_confirm(self):
        confirm = QMessageBox()
        confirm.setWindowTitle("Delete Confirm")
        confirm.setText("Remove Users?")
        confirm.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        confirm.setDefaultButton(QMessageBox.Cancel)
        confirm.accepted.connect(lambda: self.delete_users())
        confirm.accepted.connect(lambda: self.show_user("all", None))
        x = confirm.exec_()

class UI_Register_function:

    def press_register(self, userid, password, real_name):
        return_flag = False
        gender_flag = False
        admin_flag = False
        name_flag = False

        # handle invalid input
        if(SQL_function.check_ID_exist(userid) is True or userid == "" or len(userid) < 4 or helper.has_invalid_character(userid)):
            Search_Edit_function.Register_ui.ID_error_message.setHidden(False)
            return_flag = True
        elif(SQL_function.check_ID_exist(userid) is False):
            Search_Edit_function.Register_ui.ID_error_message.setHidden(True)

        if(Search_Edit_function.Register_ui.Male_button.isChecked() or Search_Edit_function.Register_ui.Female_button.isChecked() or Search_Edit_function.Register_ui.Other_button.isChecked()):
            gender_flag = True
        if(Search_Edit_function.Register_ui.Admin_button.isChecked() or Search_Edit_function.Register_ui.Normal_button.isChecked()):
            admin_flag = True
        if(real_name == ""):
            name_flag = True

        if(return_flag is True or name_flag is True or gender_flag is False or admin_flag is False ):
            Search_Edit_function.Register_ui.Register_error_message.setHidden(False)
            Search_Edit_function.Register_ui.Register_success_message.setHidden(True)
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
        SQL_function.add_user(userid, helper.encode_password(password), permission, real_name, gender)
        Search_Edit_function.show_user("all", None)
        Search_Edit_function.Register_ui.Register_error_message.setHidden(True)
        Search_Edit_function.Register_ui.Register_success_message.setHidden(False)

class UI_Login_History_function:
# Function for Login History

    def show_login_history(self, type, value):
        if(type == "all"):
            data = SQL_function.get_data_from_login_history(type, value)
        elif(type == "id"):
            data = SQL_function.get_data_from_login_history(type, value)
        elif(type == "status"):
            data = SQL_function.get_data_from_login_history(type, value)
            if(Login_function.Concentrate_Advance_ui.Success_button.isChecked()):
                data = SQL_function.get_data_from_login_history("status", "SUCCESS")
            if(Login_function.Concentrate_Advance_ui.Fail_button.isChecked()):  
                data = SQL_function.get_data_from_login_history("status", "FAIL")
        elif(type == "specific_type"):
            data = SQL_function.get_data_from_login_history("specific_type", None)
            if(Login_function.Concentrate_Advance_ui.ID_doesnt_exist_button.isChecked()):
                data = SQL_function.get_data_from_login_history("specific_type", "ID doesn't exist")
            if(Login_function.Concentrate_Advance_ui.Password_doesnt_match_ID_button.isChecked()):
                data = SQL_function.get_data_from_login_history("specific_type", "ID and Password doesn't match")
            if(Login_function.Concentrate_Advance_ui.User_enter_advance_button.isChecked()):
                data = SQL_function.get_data_from_login_history("specific_type", "A normal user tries to enter Advance mode")            
            if(Login_function.Concentrate_Advance_ui.Normal_login_button.isChecked()):
                data = SQL_function.get_data_from_login_history("specific_type", "Login with normal user mode")
            if(Login_function.Concentrate_Advance_ui.Advance_login_button.isChecked()):
                data = SQL_function.get_data_from_login_history("specific_type", "Login with Advance mode")
        self.insert_data_into_table(data)

    def insert_data_into_table(self, data):
        # initialize the table
        Login_function.Concentrate_Advance_ui.Display_Login_info.setRowCount(0) 
        row = 0
        for login_record in data:
            Login_function.Concentrate_Advance_ui.Display_Login_info.insertRow(row)
            Login_function.Concentrate_Advance_ui.Display_Login_info.setItem(row, 0, QtWidgets.QTableWidgetItem(login_record[0]))
            Login_function.Concentrate_Advance_ui.Display_Login_info.setItem(row, 1, QtWidgets.QTableWidgetItem(login_record[1]))
            Login_function.Concentrate_Advance_ui.Display_Login_info.setItem(row, 2, QtWidgets.QTableWidgetItem(login_record[2]))
            Login_function.Concentrate_Advance_ui.Display_Login_info.setItem(row, 3, QtWidgets.QTableWidgetItem(login_record[3]))
            row = row+1  

class UI_Plate_info_function:
# Function for Plate Scan
    def show_plate_info(self, type, value):        
        if(type == "availability"):
            if(Login_function.Concentrate_Advance_ui.Available_FALSE.isChecked()):
                data = SQL_function.get_data_from_plate_info(type,"FALSE")
            elif(Login_function.Concentrate_Advance_ui.Available_TRUE.isChecked()):
                data = SQL_function.get_data_from_plate_info(type,"TRUE")
            else:
                data = SQL_function.get_data_from_plate_info(type, None)
        else:
            data = SQL_function.get_data_from_plate_info(type, value)                
        self.insert_data_into_table_plate_info(data)
        helper.lock_the_Column(Login_function.Concentrate_Advance_ui.Display_Plate_Info, 1)

    def insert_data_into_table_plate_info(self, data):

        # initialize the table
        Login_function.Concentrate_Advance_ui.Display_Plate_Info.setRowCount(0) 
        row = 0
        self.check_button_array_plate_info = []

        # goes through every row
        for plate_info in data:
            Login_function.Concentrate_Advance_ui.Display_Plate_Info.insertRow(row)

            # put item into row's column1 ~ column 5
            for i in range(5):
                Login_function.Concentrate_Advance_ui.Display_Plate_Info.setItem(row, i+1, QtWidgets.QTableWidgetItem(plate_info[i]))

            # set a button to table
            check_box = QtWidgets.QCheckBox()
            Login_function.Concentrate_Advance_ui.Display_Plate_Info.setCellWidget(row, 0, check_box)
            self.check_button_array_plate_info.append(check_box)

            row = row+1      
         
    def show_add_new_plate_window(self):
        plateid, read_next_plate = QtWidgets.QInputDialog().getText(Login_function.Concentrate_Advance_ui.Plate_Scan_Tab, '', 'Please scan the bar code on the plate.')
        if(read_next_plate is True and plateid != ''):
            SQL_function.add_new_plate(plateid)        
            self.show_plate_info("all", None)
            self.show_add_new_plate_window()
    
    def show_delete_plate_confirm(self):
        confirm = QMessageBox()
        confirm.setWindowTitle("Remove confirm")
        confirm.setText("Remove these plates from database?")
        confirm.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        confirm.setDefaultButton(QMessageBox.Cancel)
        confirm.accepted.connect(lambda: self.remove_plate())
        x = confirm.exec_()        

    def show_assign_plate_to_user_window(self):
        userid, OK = QtWidgets.QInputDialog().getText(Login_function.Concentrate_Advance_ui.Plate_Scan_Tab, '', 'Please enter the user id that you like to assign to.')
        if(SQL_function.check_ID_exist(userid) is True):
            # go through entire table row by row
            for row in range(Login_function.Concentrate_Advance_ui.Display_Plate_Info.rowCount()):
                data = []
                for column in range(Login_function.Concentrate_Advance_ui.Display_Plate_Info.columnCount()):
                    if(Login_function.Concentrate_Advance_ui.Display_Plate_Info.item(row, column) != None):
                        data.append(Login_function.Concentrate_Advance_ui.Display_Plate_Info.item(row, column).text())
                if(self.check_button_array_plate_info[row].isChecked()):
                    if(data[2] == "TRUE"):
                        SQL_function.assign_plate_to_user(data[0], userid, "FALSE", helper.get_time())
                        Login_function.Concentrate_Advance_ui.Assign_success_label.setHidden(False)
                        Login_function.Concentrate_Advance_ui.Assign_fail_label.setHidden(True)
        else:
            Login_function.Concentrate_Advance_ui.Assign_success_label.setHidden(True)
            Login_function.Concentrate_Advance_ui.Assign_fail_label.setHidden(False)
        self.show_plate_info("all", None)          
        self.update_whole_table()
        Search_Edit_function.show_user("all", None)

    def show_deassign_plate_to_user_window(self):
        confirm = QMessageBox()
        confirm.setWindowTitle("Deassign confirm")
        confirm.setText("Deassign these plates from Users?")
        confirm.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        confirm.setDefaultButton(QMessageBox.Cancel)
        confirm.accepted.connect(lambda: self.deassign_plate())
        x = confirm.exec_()

    def remove_plate(self):
        for row in range(Login_function.Concentrate_Advance_ui.Display_Plate_Info.rowCount()):
            data = []
            for column in range(Login_function.Concentrate_Advance_ui.Display_Plate_Info.columnCount()):
                if(Login_function.Concentrate_Advance_ui.Display_Plate_Info.item(row, column) != None):
                    data.append(Login_function.Concentrate_Advance_ui.Display_Plate_Info.item(row, column).text())
            if(self.check_button_array_plate_info[row].isChecked()):
                SQL_function.remove_plate(data[0])   

        self.show_plate_info("all", None)
        Search_Edit_function.show_user("all", None)

    def deassign_plate(self):
        for row in range(Login_function.Concentrate_Advance_ui.Display_Plate_Info.rowCount()):
            data = []
            for column in range(Login_function.Concentrate_Advance_ui.Display_Plate_Info.columnCount()):
                if(Login_function.Concentrate_Advance_ui.Display_Plate_Info.item(row, column) != None):
                    data.append(Login_function.Concentrate_Advance_ui.Display_Plate_Info.item(row, column).text())        

            if(self.check_button_array_plate_info[row].isChecked()):
                if(data[2] == "FALSE"):
                    SQL_function.deassign_plate_from_user(data[0], "TRUE", helper.get_time())
        self.show_plate_info("all", None)
        self.update_whole_table()
        Search_Edit_function.show_user("all", None)

    def update_whole_table(self):
        for row in range(Login_function.Concentrate_Advance_ui.Display_Plate_Info.rowCount()):
            data = []
            for column in range(Login_function.Concentrate_Advance_ui.Display_Plate_Info.columnCount()):
                if(Login_function.Concentrate_Advance_ui.Display_Plate_Info.item(row, column) != None):
                    data.append(Login_function.Concentrate_Advance_ui.Display_Plate_Info.item(row, column).text())        
            SQL_function.update_plate_user_have(data[1])

class helper_function:
    # helper function
    # change info in connect_to_database() to connect to different database

    def encode_password(self, password):
        hash_md5 = hashlib.md5()
        hash_md5.update(password.encode("utf-8"))
        return hash_md5.hexdigest()

    def get_time(self):
        return datetime.datetime.now()

    def lock_the_Column(self, display_table, lock_column):
        rows = display_table.rowCount()
        for i in range(rows):
            item = display_table.item(i, lock_column)
            item.setFlags(QtCore.Qt.ItemIsEnabled)

    # checker for password
    def has_capital_letters(self, password):
        has_capital = False
        for letters in password:
            # checking for uppercase character and flagging
            if letters.isupper():
                has_capital = True
                break
        return has_capital
 
    def has_lower_letters(self, password):
        has_lower = False
        for letters in password:
            # checking for uppercase character and flagging
            if letters.islower():
                has_lower = True
                break
        return has_lower  
          
    def has_numbers(self, password):
        return any(letters.isdigit() for letters in password)

    def has_invalid_character(self, password):
        # Make own character set and pass
        # this as argument in compile method
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
     
        # Pass the string in search
        # method of regex object.   
        if(regex.search(password) == None):
            return False
        else:
            return True
    
    def check_password_availability(self, password):
        if(len(password) >= 6 and self.has_capital_letters(password) is True and self.has_numbers(password) and self.has_lower_letters(password) is True and self.has_invalid_character(password) is False):
            return True
        return False

class MySQL_function:
    def connect_to_database(self):
        mydb = mysql.connector.connect(
            host="localhost", 
            user="root",
            password="Ar0340252",
            database="UI_database"
        )
        return mydb        

    def create_table_first(self, cursor):
        # CREATE TABLE just in case
        cursor.execute("CREATE TABLE if not exists User_Information (ID VARCHAR(500) PRIMARY KEY, PASSWORD VARCHAR(500), PERMISSION VARCHAR(20), REAL_NAME VARCHAR(50), GENDER VARCHAR(20), PLATE_NUM INT)")
        cursor.execute("CREATE TABLE if not exists Login_record (ID VARCHAR(500), LOGIN_TIME VARCHAR(500), LOGIN_STATE VARCHAR(500), SPECIFIC_TYPE VARCHAR(500))")
        cursor.execute("CREATE TABLE if not exists Plate_Information (PLATE_ID VARCHAR(500) PRIMARY KEY, LAST_ASSIGNED_USER_ID VARCHAR(500), AVAILABLE_FOR_ASSIGN VARCHAR(20), LAST_ASSIGN_TIME VARCHAR(500), LAST_DEASSIGN_TIME VARCHAR(500))")

    def check_ID_password(self, userid, password):
        Match = False
        try:
            # Connect to database
            mydb = self.connect_to_database()
            mycursor = mydb.cursor()
            # Create table if not exist
            self.create_table_first( mycursor)

            # Actually insert plate into table
            mycursor.execute("SELECT * FROM User_Information")
            for User_record in mycursor:
                # compare the id
                if(User_record[0] == userid):
                    # compare the password
                    if(User_record[1] == password):
                        Match = True            
        except:
            logging.error("Check_ID_password Encountered error!")
            return -1
        return Match
    
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
                #compare the id
                if(User_record[0] == userid):
                    # check the permission
                    if(User_record[2] == "ADMIN"):
                        is_admin = True
        except:
            logging.error("check_ID_is_admin Encountered error")
            return -1
        return is_admin   
     
    def check_ID_exist(self, userid):
        Exist = False
        try:
            # Connect to database
            mydb = self.connect_to_database()
            mycursor = mydb.cursor()
            # Create table if not exist
            self.create_table_first( mycursor)  
            mycursor.execute('''SELECT * FROM User_Information''')
            for User_record in mycursor:
                # compare the id
                if(User_record[0] == userid):
                    # ID exists in the database
                    Exist = True
        except:
            logging.error("check_ID_exist Encountered error!")
            return -1
        return Exist             
      
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
        except:
            logging.error("remove_user Encountered error!")
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
        except:
            logging.error("add_user Encountered error!")
            return -1

    # login record function
    def add_login_record(self, userid, login_state, type):
        try:
            # Connect to database
            mydb = self.connect_to_database()
            mycursor = mydb.cursor()
            # Create table if not exist
            self.create_table_first(mycursor)  
            
            sql = ("INSERT INTO Login_record(ID, LOGIN_TIME, LOGIN_STATE, SPECIFIC_TYPE) VALUES (%s, %s, %s, %s)")
            val = (userid, helper_function.get_time(helper_function), login_state, type)
            mycursor.execute(sql, val)
            mydb.commit()
        except:
            logging.error("add_login_record Encountered error!")
            return -1
    
    def get_data_from_login_history(self, type, value):
        # Open database
        try:
            # Connect to database
            mydb = self.connect_to_database()
            mycursor = mydb.cursor()
            # Create table if not exist
            self.create_table_first(mycursor)
            if(type == "all"):
                mycursor.execute("SELECT * FROM Login_record")
            if(type == "id"):
                sql = ("SELECT * FROM Login_record WHERE ID=%s")
                val = (value, )
                mycursor.execute(sql, val)
            if(type == "status"):
                sql = ("SELECT * FROM Login_record WHERE LOGIN_STATE=%s")
                val = (value, )
                mycursor.execute(sql, val)
            if(type == "specific_type"):
                sql = ("SELECT * FROM Login_record WHERE SPECIFIC_TYPE=%s")
                val = (value, )
                mycursor.execute(sql, val)

            data = mycursor.fetchall()            
        except:
            logging.error("get_data_from_login_history Encountered error!")
            return -1
        return data

    # user info function
    def get_data_from_user_info(self, type, value):
        try:
            # Connect to database
            mydb = self.connect_to_database()
            mycursor = mydb.cursor()
            # Create table if not exist
            self.create_table_first(mycursor)
            if(type == "all"):
                mycursor.execute("SELECT * FROM User_Information")
            if(type == "id_strict"):
                sql = ("SELECT * FROM User_Information WHERE ID=%s ORDER BY ID ASC")
                val = (value, )
                mycursor.execute(sql, val)
            if(type == "id"):
                sql = ("SELECT * FROM User_Information WHERE ID LIKE %s ORDER BY ID ASC")
                val = ('%'+value+'%', )
                mycursor.execute(sql, val)                
            if(type == "name"):
                sql = ("SELECT * FROM User_Information WHERE REAL_NAME LIKE %s ORDER BY REAL_NAME ASC")
                val = ('%'+value+'%', )
                mycursor.execute(sql, val)
            if(type == "permission"):
                sql = ("SELECT * FROM User_Information WHERE PERMISSION=%s ORDER BY ID ASC")
                val = (value, )
                mycursor.execute(sql, val) 
            if(type == "gender"):
                sql = ("SELECT * FROM User_Information WHERE GENDER=%s ORDER BY ID ASC")
                val = (value, )
                mycursor.execute(sql, val)                   
            data = mycursor.fetchall()            
        except:
            logging.error("get_data_from_user_info Encountered error!")
            return -1
        return data                     
  
    # update user info function
    def update_data_to_user_info(self, userid, password, permission, real_name, gender, plate_amount):
        try:
            # Connect to database
            mydb = self.connect_to_database()
            mycursor = mydb.cursor()
            # Create table if not exist
            self.create_table_first(mycursor)
            if(password != None):
                sql = ("UPDATE User_Information SET PASSWORD=%s, PERMISSION=%s, REAL_NAME=%s, GENDER=%s, PLATE_NUM=%s WHERE ID=%s")
                val = (password, permission, real_name, gender, plate_amount, userid)
                mycursor.execute(sql, val)
            else:
                sql = ("UPDATE User_Information SET PERMISSION=%s, REAL_NAME=%s, GENDER=%s, PLATE_NUM=%s WHERE ID=%s")
                val = (permission, real_name, gender, plate_amount, userid)
                mycursor.execute(sql, val)
            mydb.commit()                      
            data = mycursor.fetchall()      
            
        except:
            logging.error("update_data_to_user_info Encountered error!")
            return -1
        return data      
            
    # plate info function
    def get_data_from_plate_info(self, type , value):
        # Open database
        try:
            # Connect to database
            mydb = self.connect_to_database()
            mycursor = mydb.cursor()
            # Create table if not exist
            self.create_table_first(mycursor)
            if(type == "all"):
                mycursor.execute("SELECT * FROM Plate_Information")
            if(type == "plate_id"):
                sql = ("SELECT * FROM Plate_Information WHERE PLATE_ID LIKE %s ORDER BY PLATE_ID ASC")
                val = ('%'+value+'%', )
                mycursor.execute(sql, val)                   
            if(type == "user_id"):
                sql = ("SELECT * FROM Plate_Information WHERE LAST_ASSIGNED_USER_ID LIKE %s ORDER BY LAST_ASSIGNED_USER_ID ASC")
                val = ('%'+value+'%', )
                mycursor.execute(sql, val)
            if(type == "availability"):
                sql = ("SELECT * FROM Plate_Information WHERE AVAILABLE_FOR_ASSIGN=%s")
                val = (value, )
                mycursor.execute(sql, val)
            data = mycursor.fetchall()         
        except:
            logging.error("get_data_from_plate_info Encountered error!")
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
            logging.info("the plate: '" + plateid +"' is added")
        except:
            logging.error("add_new_plate Encountered error!")
        return        

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
        except:
            logging.error("assign_plate_to_user Encountered error!")
        self.update_plate_user_have(userid)     

    def deassign_plate_from_user(self, plateid, availability, last_deassign_time):
        try:    
            # Connect to database
            mydb = self.connect_to_database()
            mycursor = mydb.cursor()
            # Create table if not exist
            self.create_table_first(mycursor)

            sql = ("UPDATE Plate_Information SET AVAILABLE_FOR_ASSIGN=%s, LAST_DEASSIGN_TIME=%s WHERE PLATE_ID=%s")
            val = (availability, last_deassign_time, plateid)
            mycursor.execute(sql, val)
            mydb.commit()
        except:
            logging.error("deassign_plate_from_user Encountered error!")
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
        except:
            logging.error("remove_plate Encountered error!")
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
            logging.error("update_plate_user_have Encountered error!")
            return -1  


# main
if __name__ == "__main__":
    Login_function = UI_Login_function()
    Info_Editor_function = UI_Info_Editor_function()
    Search_Edit_function = UI_Search_Edit_function()
    Login_History_function = UI_Login_History_function()
    Plate_Info_function = UI_Plate_info_function()
    Register_function = UI_Register_function()
    SQL_function = MySQL_function()
    helper = helper_function()
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    Loginui = Ui_Login()
    Loginui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())

