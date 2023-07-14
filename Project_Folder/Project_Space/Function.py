import datetime
import sqlite3
import hashlib
import re
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QStyledItemDelegate, QApplication, QTableWidget, QMessageBox


class function_class:

    # helper function
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

    # SQLite3 related function
    def check_ID_password(self, userid, password):
        Match = False
        # Open database
        project_db = sqlite3.connect('Project.db')
        try:
            self.create_User_information_table(project_db)
            # go through the entire database
            data = project_db.execute('''SELECT * FROM User_Information''')
            for User_record in data:
                # compare the id
                if(User_record[0] == userid):
                    # compare the password
                    if(User_record[1] == password):
                        Match = True
        except:
            print("Check_ID_password Encountered error!")
            return -1

        # Apply changes
        project_db.commit()        
        
        # Close the data base
        project_db.close 
    
        return Match
    
    def check_ID_is_admin(self, userid):
        is_admin = False

        project_db = sqlite3.connect('Project.db')
        try:
            self.create_User_information_table(project_db)       
            data = project_db.execute('''SELECT * FROM User_Information''')
            for User_record in data:
                #compare the id
                if(User_record[0] == userid):
                    # check the permission
                    if(User_record[2] == "ADMIN"):
                        is_admin = True
        except:
            print("check_ID_is_admin Encountered error")
        return is_admin    

    def check_ID_exist(self, userid):
        Exist = False
        # Open database
        project_db = sqlite3.connect('Project.db')
        try:
            self.create_User_information_table(project_db)
            # go through the entire database
            data = project_db.execute('''SELECT * FROM User_Information''')
            for User_record in data:
                # compare the id
                if(User_record[0] == userid):
                    # ID exists in the database
                    Exist = True
        except:
            print("Encountered error, please check if your input is valid!")
            return -1

        # Apply changes
        project_db.commit()        
        
        # Close the data base
        project_db.close 
    
        return Exist       

    def create_User_information_table(self, db):
        db.execute('''CREATE TABLE IF NOT EXISTS User_Information(
            ID TEXT PRIMARY KEY NOT NULL,
            PASSWORD TEXT NOT NULL,
            PERMISSION TEXT NOT NULL,
            REAL_NAME TEXT NOT NULL,
            GENDER TEXT NOT NULL,
            PLATE_NUM INTEGER
        )''')
        
    def remove_user(self, userid):
        # Open database
        project_db = sqlite3.connect('Project.db')
        try:
            self.create_User_information_table(project_db)
            # delete the user
            project_db.execute('''DELETE FROM User_Information WHERE ID=?''', (userid,))
        except:
            print("Encountered error, please check if your input is valid!")
            return -1
        # Apply changes
        project_db.commit()        
        
        # Close the data base
        project_db.close 

    def add_user(self, userid, password, permission, real_name, gender):
        # Open the database
        project_db = sqlite3.connect('Project.db')
        try:
            self.create_User_information_table(project_db)
        
            # go through the entire database
            project_db.execute('''INSERT INTO User_Information(ID, PASSWORD, PERMISSION, REAL_NAME, GENDER, PLATE_NUM)
                VALUES(?, ?, ?, ?, ?, ?)
            ''', (userid, password, permission, real_name, gender, 0)) 
        except:
            print("Encountered error, please check if your input is valid!")

        # Apply changes
        project_db.commit()        
        
        # Close the data base
        project_db.close 
    
        return


    # login record function
    def add_login_record(self, userid, login_state, fail_type):
        # Open database
        project_db = sqlite3.connect('Project.db')
        login_time = self.get_time()
        
        project_db.execute('''CREATE TABLE IF NOT EXISTS Login_record(
            ID TEXT NOT NULL,
            LOGIN_TIME TEXT NOT NULL,
            LOGIN_STATE TEXT NOT NULL,
            SPECIFIC_TYPE TEXT 
        )''')        
        
        project_db.execute('''INSERT INTO Login_record(ID, LOGIN_TIME, LOGIN_STATE, SPECIFIC_TYPE)
            VALUES(?, ?, ?, ?)
        ''', (userid, login_time, login_state, fail_type))  
        
        # Apply changes
        project_db.commit()        
        
        # Close the data base
        project_db.close
        
        return
    
    def get_all_data_from_login_history(self):
        # Open database
        project_db = sqlite3.connect('Project.db')
        try:
            self.create_User_information_table(project_db)
            # go through the entire database
            data = project_db.execute('''SELECT * FROM Login_record''')
        except:
            print("get_all_data_from_login_history Encountered error!")
            return -1

        # Apply changes
        project_db.commit()        
        
        # Close the data base
        project_db.close 
    
        return data

    def get_data_from_login_history_by_id(self, userid):
        # Open database
        project_db = sqlite3.connect('Project.db')

        try:
            self.create_User_information_table(project_db)
            # go through the entire database
            data = project_db.execute('''
            SELECT * 
            FROM Login_record
            WHERE ID=?
            ''', (userid,))
        except:
            print("get_all_data_from_login_history Encountered error!")
            return -1   
                 
        # Apply changes
        project_db.commit()        
        
        # Close the data base
        project_db.close 
    
        return data

    def get_data_from_login_history_by_status(self, status):
        # Open database
        project_db = sqlite3.connect('Project.db')

        try:
            self.create_User_information_table(project_db)
            # go through the entire database
            data = project_db.execute('''
            SELECT * 
            FROM Login_record
            WHERE LOGIN_STATE=?
            ''', (status,))
        except:
            print("get_data_from_login_history_by_status Encountered error!")
            return -1   
                 
        # Apply changes
        project_db.commit()        
        
        # Close the data base
        project_db.close 
    
        return data        

    def get_data_from_login_history_by_fail_type(self, failtype):
        # Open database
        project_db = sqlite3.connect('Project.db')

        try:
            self.create_User_information_table(project_db)
            # go through the entire database
            data = project_db.execute('''
            SELECT * 
            FROM Login_record
            WHERE SPECIFIC_TYPE=?
            ''', (failtype,))
        except:
            print("get_data_from_login_history_by_fail_type Encountered error!")
            return -1   
                 
        # Apply changes
        project_db.commit()        
        
        # Close the data base
        project_db.close 
    
        return data        

    def get_data_from_login_history_by_success_type(self, successtype):
        # Open database
        project_db = sqlite3.connect('Project.db')

        try:
            self.create_User_information_table(project_db)
            # go through the entire database
            data = project_db.execute('''
            SELECT * 
            FROM Login_record
            WHERE SPECIFIC_TYPE=?
            ''', (successtype,))
        except:
            print("get_data_from_login_history_by_fail_type Encountered error!")
            return -1   
                 
        # Apply changes
        project_db.commit()        
        
        # Close the data base
        project_db.close 
    
        return data        
    
    # user info function
    def get_all_data_from_user_info(self):

        # Open database
        project_db = sqlite3.connect('Project.db')
        try:
            self.create_User_information_table(project_db)
            # go through the entire database
            data = project_db.execute('''SELECT * FROM User_Information ORDER BY ID''')
        except:
            print("get_all_data_from_user_info Encountered error!")
            return -1

        # Apply changes
        project_db.commit()        
        
        # Close the data base
        project_db.close 
    
        return data        

    def get_data_from_user_info_by_id(self, userid):
        # Open database
        project_db = sqlite3.connect('Project.db')

        try:
            self.create_User_information_table(project_db)
            # go through the entire database
            data = project_db.execute('''
            SELECT * 
            FROM User_Information
            WHERE ID=?
            ORDER BY ID ASC                                      
            ''', (userid, ))
        except:
            print("get_data_from_user_info_contains_id Encountered error!")
            return -1   
                 
        # Apply changes
        project_db.commit()        
        
        # Close the data base
        project_db.close 
    
        return data   
    
    def get_data_from_user_info_contains_id(self, userid):
        # Open database
        project_db = sqlite3.connect('Project.db')

        try:
            self.create_User_information_table(project_db)
            # go through the entire database
            data = project_db.execute('''
            SELECT * 
            FROM User_Information
            WHERE ID
            LIKE ?
            ORDER BY ID ASC                                      
            ''', ('%'+userid+'%', ))
        except:
            print("get_data_from_user_info_contains_id Encountered error!")
            return -1   
                 
        # Apply changes
        project_db.commit()        
        
        # Close the data base
        project_db.close 
    
        return data        

    def get_data_from_user_info_contains_name(self, name):
        # Open database
        project_db = sqlite3.connect('Project.db')

        try:
            self.create_User_information_table(project_db)
            # go through the entire database
            data = project_db.execute('''
            SELECT * 
            FROM User_Information
            WHERE REAL_NAME
            LIKE ?
            ORDER BY REAL_NAME ASC
            ''', ('%'+name+'%', ))
        except:
            print("get_data_from_user_info_contains_name Encountered error!")
            return -1   
                 
        # Apply changes
        project_db.commit()        
        
        # Close the data base
        project_db.close 
    
        return data  

    def get_data_from_user_info_by_permission(self, permission):
        # Open database
        project_db = sqlite3.connect('Project.db')

        try:
            self.create_User_information_table(project_db)
            # go through the entire database            
            data = project_db.execute('''
            SELECT * 
            FROM User_Information
            WHERE PERMISSION=?
            ORDER BY ID ASC
            ''', (permission,))
        except:
            print("get_data_from_login_history_by_fail_type Encountered error!")
            return -1   
                 
        # Apply changes
        project_db.commit()        
        
        # Close the data base
        project_db.close 
    
        return data        
    
    def get_data_from_user_info_by_gender(self, gender):
        # Open database
        project_db = sqlite3.connect('Project.db')

        try:
            self.create_User_information_table(project_db)
            # go through the entire database        
            data = project_db.execute('''
            SELECT * 
            FROM User_Information
            WHERE GENDER=?
            ORDER BY ID ASC    
            ''', (gender,))
        except:
            print("get_data_from_login_history_by_fail_type Encountered error!")
            return -1   
                 
        # Apply changes
        project_db.commit()        
        
        # Close the data base
        project_db.close 
    
        return data        

  
    # update user info function
    def update_data_to_user_info(self, userid, password, permission, real_name, gender, plate_amount):
        # Open database
        project_db = sqlite3.connect('Project.db')
        if(password != None):
            self.update_password(project_db, userid, password)

        self.update_permission(project_db, userid, permission)

        self.update_name(project_db, userid, real_name)

        self.update_gender(project_db, userid, gender)

        self.update_plate_amount(project_db, userid, plate_amount)

        # Apply changes
        project_db.commit()        
        
        # Close the data base
        project_db.close 
    
        return          

    def update_password(self, database, userid, password):
        try:
            self.create_User_information_table(database)
            # go through the entire database
            data = database.execute('''
            UPDATE User_Information
            SET PASSWORD=?
            WHERE ID=?
            ''', (password, userid))
        except:
            print("update_password Encountered error!")
            return -1   
        return data
    
    def update_name(self, database, userid, name):
        try:
            self.create_User_information_table(database)
            # go through the entire database
            data = database.execute('''
            UPDATE User_Information
            SET REAL_NAME=?
            WHERE ID=?
            ''', (name, userid))
        except:
            print("update_name Encountered error!")
            return -1   
        return data                 

    def update_permission(self, database, userid, permission):
        try:
            self.create_User_information_table(database)
            # go through the entire database
            data = database.execute('''
            UPDATE User_Information
            SET PERMISSION=?
            WHERE ID=?
            ''', (permission, userid))
        except:
            print("update_permission Encountered error!")
            return -1   
        return data   
  
    def update_gender(self, database, userid, gender):
        try:
            self.create_User_information_table(database)
            # go through the entire database
            data = database.execute('''
            UPDATE User_Information
            SET GENDER=?
            WHERE ID=?
            ''', (gender, userid))
        except:
            print("update_gender Encountered error!")
            return -1   
        return data         

    def update_plate_amount(self, database, userid, plateamount):
        try:
            self.create_User_information_table(database)
            # go through the entire database
            data = database.execute('''
            UPDATE User_Information
            SET PLATE_NUM=?
            WHERE ID=?
            ''', (plateamount, userid))
        except:
            print("update_gender Encountered error!")
            return -1   
        return data            

    # plate info function
    def create_plate_info_table(self, db):
        db.execute('''CREATE TABLE IF NOT EXISTS Plate_Information(
            PLATE_ID TEXT PRIMARY KEY NOT NULL,
            LAST_ASSIGNED_USER_ID TEXT NOT NULL,
            AVAILABLE_FOR_ASSIGN TEXT NOT NULL,
            LAST_ASSIGN_TIME TEXT NOT NULL,
            LAST_DEASSIGN_TIME TEXT NOT NULL
        )''')

    def get_all_data_from_plate_info(self):

        # Open database
        project_db = sqlite3.connect('Project.db')
        try:
            self.create_plate_info_table(project_db)
            # go through the entire database
            data = project_db.execute('''SELECT * FROM Plate_Information ORDER BY PLATE_ID ASC''')
        except:
            print("get_all_data_from_plate_info Encountered error!")
            return -1

        # Apply changes
        project_db.commit()        
        
        # Close the data base
        project_db.close 
    
        return data    
    
    def get_data_from_plate_info_by_plate_id(self, plateid):
        # Open database
        project_db = sqlite3.connect('Project.db')

        try:
            self.create_User_information_table(project_db)
            # go through the entire database
            data = project_db.execute('''
            SELECT * 
            FROM Plate_Information                                      
            WHERE PLATE_ID
            LIKE ?                
            ORDER BY PLATE_ID ASC                                                                                                 
            ''', ('%'+plateid+'%',))
        except:
            print("get_data_from_user_info_by_id Encountered error!")
            return -1   
                 
        # Apply changes
        project_db.commit()        
        
        # Close the data base
        project_db.close 
    
        return data        

    def get_data_from_plate_info_by_user_id(self, userid):
        # Open database
        project_db = sqlite3.connect('Project.db')

        try:
            self.create_User_information_table(project_db)
            # go through the entire database
            data = project_db.execute('''
            SELECT * 
            FROM Plate_Information                                      
            WHERE LAST_ASSIGNED_USER_ID
            LIKE ?                
            ORDER BY LAST_ASSIGNED_USER_ID ASC                                                                                                 
            ''', ('%'+userid+'%',))
        except:
            print("get_data_from_user_info_by_id Encountered error!")
            return -1   
                 
        # Apply changes
        project_db.commit()        
        
        # Close the data base
        project_db.close 
    
        return data        

    def get_data_from_plate_info_by_availability(self, availability):
        # Open database
        project_db = sqlite3.connect('Project.db')

        try:
            self.create_User_information_table(project_db)
            # go through the entire database
            data = project_db.execute('''
            SELECT * 
            FROM Plate_Information                                      
            WHERE AVAILABLE_FOR_ASSIGN=?
            ORDER BY PLATE_ID ASC  
            ''', (availability,))
        except:
            print("get_data_from_login_history_by_availability Encountered error!")
            return -1   
                 
        # Apply changes
        project_db.commit()        
        
        # Close the data base
        project_db.close 
    
        return data        

    def add_new_plate(self, plateid):
        # Open the database
        project_db = sqlite3.connect('Project.db')
        try:
            self.create_User_information_table(project_db)
        
            # go through the entire database
            project_db.execute('''INSERT INTO Plate_Information(PLATE_ID, LAST_ASSIGNED_USER_ID, AVAILABLE_FOR_ASSIGN, LAST_ASSIGN_TIME, LAST_DEASSIGN_TIME)
                VALUES(?, ?, ?, ?, ?)
            ''', (plateid, "NONE", "TRUE", "NONE", "NONE")) 
        except:
            print("add_new_plate Encountered error!")

        # Apply changes
        project_db.commit()        
        
        # Close the data base
        project_db.close 
    
        return        

    def assign_plate_to_user(self, plateid, userid, availability, last_assign_time):
        # Open the database
        project_db = sqlite3.connect('Project.db')
        try:
            self.create_User_information_table(project_db)
            # go through the entire database
            data = project_db.execute('''
            UPDATE Plate_Information
            SET LAST_ASSIGNED_USER_ID=?, AVAILABLE_FOR_ASSIGN=?, LAST_ASSIGN_TIME=?
            WHERE PLATE_ID=?
            ''', (userid, availability, last_assign_time, plateid))
        except:
            print("assign_plate_to_user Encountered error!")
            return -1   

        # Apply changes
        project_db.commit()        
        
        # Close the data base
        project_db.close 
    
        self.update_plate_user_have(userid)

        return        

    def deassign_plate_from_user(self, plateid, availability, last_deassign_time):
        # Open the database
        project_db = sqlite3.connect('Project.db')
        try:
            self.create_User_information_table(project_db)
            # go through the entire database
            data = project_db.execute('''
            UPDATE Plate_Information
            SET AVAILABLE_FOR_ASSIGN=?, LAST_DEASSIGN_TIME=?
            WHERE PLATE_ID=?
            ''', (availability, last_deassign_time, plateid))
        except:
            print("assign_plate_to_user Encountered error!")
            return -1   

        # Apply changes
        project_db.commit()        
        
        # Close the data base
        project_db.close 
    
        return       
    
    def remove_plate(self, plateid):
        # Open database
        project_db = sqlite3.connect('Project.db')
        try:
            self.create_plate_info_table(project_db)
            # delete the user
            project_db.execute('''DELETE FROM Plate_Information WHERE PLATE_ID=?''', (plateid,))
        except:
            print("Encountered error, please check if your input is valid!")
            return -1
        # Apply changes
        project_db.commit()        
        
        # Close the data base
        project_db.close         

    def update_plate_user_have(self, userid):
        # Open the database
        project_db = sqlite3.connect('Project.db')        

        # get the number of plate user have
        try:
            self.create_User_information_table(project_db)
            # go through the entire database
            project_db.execute('''
            UPDATE User_Information
            SET PLATE_NUM = (
                SELECT count(*) 
                FROM Plate_Information 
                WHERE LAST_ASSIGNED_USER_ID=? AND AVAILABLE_FOR_ASSIGN='FALSE')
            WHERE ID=?
            ''', (userid, userid))        
        except:
            print("get_amount_of_plate_user_have Encountered error!")
            return -1  


        # Apply changes
        project_db.commit()        
        
        # Close the data base
        project_db.close 
        return
