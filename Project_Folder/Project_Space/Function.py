import datetime
import sqlite3
import hashlib
import re
from functools import partial
from PyQt5.QtCore import pyqtSignal

class function_class:
    ID_PASSWORD_MATCH = pyqtSignal()

    # helper function
    def encode_password(self, password):
        hash_md5 = hashlib.md5()
        hash_md5.update(password.encode("utf-8"))
        return hash_md5.hexdigest()

    def print_time(self):
        # Get login time
        login_time = datetime.datetime.now()
        print("login time : ", login_time)

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
        login_time = datetime.datetime.now()
        
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
            data = project_db.execute('''SELECT * FROM User_Information''')
        except:
            print("get_all_data_from_login_history Encountered error!")
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
            ''', (userid,))
        except:
            print("get_data_from_user_info_by_id Encountered error!")
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
            ''', ('%'+userid+'%', ))
        except:
            print("get_data_from_user_info_contains_id Encountered error!")
            return -1   
                 
        # Apply changes
        project_db.commit()        
        
        # Close the data base
        project_db.close 
    
        return data        

    def get_data_from_user_info_by_name(self, name):
        # Open database
        project_db = sqlite3.connect('Project.db')

        try:
            self.create_User_information_table(project_db)
            # go through the entire database
            data = project_db.execute('''
            SELECT * 
            FROM User_Information
            WHERE REAL_NAME=?
            ''', (name,))
        except:
            print("get_data_from_user_info_by_name Encountered error!")
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
    def update_data_to_user_info(self, userid, password, permission, real_name, gender):
        # Open database
        project_db = sqlite3.connect('Project.db')
        if(password != None):
            self.update_password(project_db, userid, password)

        self.update_permission(project_db, userid, permission)

        self.update_name(project_db, userid, real_name)

        self.update_gender(project_db, userid, gender)

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


