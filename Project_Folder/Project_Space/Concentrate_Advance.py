# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Concentrate_Advance.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Concentrate_Advance(object):
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
        self.Display_table.horizontalHeader().setVisible(False)
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
        self.Permission_label = QtWidgets.QLabel(self.Search_Edit_Tab)
        self.Permission_label.setGeometry(QtCore.QRect(50, 250, 81, 20))
        self.Permission_label.setMinimumSize(QtCore.QSize(81, 20))
        self.Permission_label.setObjectName("Permission_label")
        self.User_button = QtWidgets.QRadioButton(self.Search_Edit_Tab)
        self.User_button.setGeometry(QtCore.QRect(140, 250, 100, 20))
        self.User_button.setMinimumSize(QtCore.QSize(100, 20))
        self.User_button.setObjectName("User_button")
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
        self.ID_input_login_history = QtWidgets.QLineEdit(self.Login_History_Tab)
        self.ID_input_login_history.setGeometry(QtCore.QRect(120, 20, 141, 21))
        self.ID_input_login_history.setMinimumSize(QtCore.QSize(141, 21))
        self.ID_input_login_history.setText("")
        self.ID_input_login_history.setObjectName("ID_input_login_history")
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
        self.Show_all_button_Plate_Info.setGeometry(QtCore.QRect(80, 370, 180, 30))
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
        self.Assign_plate_to_user.setGeometry(QtCore.QRect(80, 450, 180, 30))
        self.Assign_plate_to_user.setMinimumSize(QtCore.QSize(150, 30))
        self.Assign_plate_to_user.setObjectName("Assign_plate_to_user")
        self.Deassign_plate_from_user = QtWidgets.QPushButton(self.Plate_Scan_Tab)
        self.Deassign_plate_from_user.setGeometry(QtCore.QRect(80, 410, 180, 30))
        self.Deassign_plate_from_user.setMinimumSize(QtCore.QSize(150, 30))
        self.Deassign_plate_from_user.setObjectName("Deassign_plate_from_user")
        self.Add_new_plate = QtWidgets.QPushButton(self.Plate_Scan_Tab)
        self.Add_new_plate.setGeometry(QtCore.QRect(80, 490, 180, 30))
        self.Add_new_plate.setMinimumSize(QtCore.QSize(150, 30))
        self.Add_new_plate.setObjectName("Add_new_plate")
        self.Remove_plate = QtWidgets.QPushButton(self.Plate_Scan_Tab)
        self.Remove_plate.setGeometry(QtCore.QRect(80, 530, 180, 30))
        self.Remove_plate.setMinimumSize(QtCore.QSize(150, 30))
        self.Remove_plate.setObjectName("Remove_plate")
        Concentrate_Advance.addTab(self.Plate_Scan_Tab, "")

        self.retranslateUi(Concentrate_Advance)
        Concentrate_Advance.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Concentrate_Advance)

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
        Concentrate_Advance.setTabText(Concentrate_Advance.indexOf(self.Plate_Scan_Tab), _translate("Concentrate_Advance", "Plate Scan"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Concentrate_Advance = QtWidgets.QTabWidget()
    ui = Ui_Concentrate_Advance()
    ui.setupUi(Concentrate_Advance)
    Concentrate_Advance.show()
    sys.exit(app.exec_())
