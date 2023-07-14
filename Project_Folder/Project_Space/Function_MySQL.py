import datetime
import hashlib
import re
from PyQt5 import QtCore
import mysql.connector

class function_class_MySQL:

    # helper function
    # change info in connect_to_database() to connect to different database
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

    # MySQL C
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
                if(User_record[0] == userid):
                    # compare the password
                    if(User_record[1] == password):
                        Match = True            
        except:
            print("Check_ID_password Encountered error!")
            return -1
        return Match
    
    # MySQL C
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
            print("check_ID_is_admin Encountered error")
            return -1
        return is_admin   
     
    # MySQL C
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
                if(User_record[0] == userid):
                    # ID exists in the database
                    Exist = True
        except:
            print("Encountered error, please check if your input is valid!")
            return -1
        return Exist       

    # MySQL C        
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
            print("remove_user Encountered error!")
            return -1

    # MySQL C
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
            print("add_user Encountered error!")
            return -1

    # login record function
    # MySQL C
    def add_login_record(self, userid, login_state, type):
        try:
            # Connect to database
            mydb = self.connect_to_database()
            mycursor = mydb.cursor()
            # Create table if not exist
            self.create_table_first(mycursor)  
            
            sql = ("INSERT INTO Login_record(ID, LOGIN_TIME, LOGIN_STATE, SPECIFIC_TYPE) VALUES (%s, %s, %s, %s)")
            val = (userid, self.get_time(), login_state, type)
            mycursor.execute(sql, val)
            mydb.commit()
        except:
            print("add_login_record Encountered error!")
            return -1
    
    # MySQL C
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
            print("get_data_from_login_history Encountered error!")
            return -1
        return data

    # user info function
    # MySQL C
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
            print("get_data_from_user_info Encountered error!")
            return -1
        return data                     
  
    # update user info function
    # MySQL C
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
            print("get_data_from_user_info Encountered error!")
            return -1
        return data      
            
    # plate info function
    # MySQL C
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
            print("get_data_from_plate_info Encountered error!")
            return -1
        return data   
    
    # MySQL C
    def add_new_plate(self, plateid):
        try:
            # Connect to database
            mydb = self.connect_to_database()
            mycursor = mydb.cursor()
            # Create table if not exist
            self.create_table_first(mycursor)

            # Actually insert plate into table
            sql = "INSERT INTO Plate_Information(PLATE_ID, LAST_ASSIGNED_USER_ID, AVAILABLE_FOR_ASSIGN, LAST_ASSIGN_TIME, LAST_DEASSIGN_TIME) VALUES (%s, %s, %s, %s, %s)"
            val = (plateid, "NONE", "TRUE", "NONE", "NONE")
            mycursor.execute(sql, val)
            mydb.commit()
        except:
            print("add_new_plate Encountered error!")
        return        
    
    # MySQL C
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
            print("assign_plate_to_user Encountered error!")
        self.update_plate_user_have(userid)     
    
    # MySQL C
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
            print("deassign_plate_from_user Encountered error!")
            return -1     
    
    # MySQL C
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
            print("remove_plate Encountered error!")
            return -1 

    # MySQL C
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
            print("update_plate_user_have Encountered error!")
            return -1  

