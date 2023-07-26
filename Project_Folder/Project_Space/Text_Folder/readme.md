Critical!! Please read following information before start using this UI program.

        1.      Edit the database information located in: 
                        class MySQL_function() --> def connect_to_database(self)
        
        2.      Run the program and check the "Admin mode" checkbox, then Login with following id 
                and password:
                        ID:         "ADMIN"
                        PASSWORD:   "Point1" 
                
        3.      While adding a new users, the default password will be set as "Point1", which the user can 
                edited it after logging in.
        
        4.      In the editing window/tabs, the checkboxes infront of are for mistake-proofing purpose, 
                changes will be applied only when the checkbox of the row is checked, including deletion 
                and edit.

        5.      In Advance UI, the table display 20 row of data per pages.



Please follow the following format while editing user info:

    Edit User info:

        Manual: 
            1. Please check the checkbox at the row that you like to edit, users at rows that aren't checked 
            will not be edited.
            2. After editing, press the "Save change" button.
            3. The change will be applied immediately, please double check if the edit is successful. 

        ID:
            1. Should not be less than 4 characters.
            2. Do not contains special character (e.g.!@#$*) and white space.
            3. Every ID is unique, inputing existing ID is not allowed.
        Password:  
            1. Should not be less than 6 characters.
            2. Do not contains special character (e.g.!@#$*) and white space.
            3. Should be the combination of numbers and alphabets, which should including one upper and lower 
            letter each.
        
        Permission: 
            1. Only accept "ADMIN" and "USER".
            2. Please beware that the editor is capital sensitive.

        Gender:
            1. Only accept "MALE", "FEMALE", and "OTHERS".
            2. Please beware that the editor is capital sensitive.

    Add a User:
        1. When inputing user id, please follow the format mentioned above.
        2. All the information should be filled or checked.
    
    Delete a User:
        1. Please check the checkbox at the row that you like to delete, users at rows that aren't checked 
        will not be deleted.
        2. Deletion will be applied immediately after pressing the OK button in popup window


Please follow the following format while editing plate info:

    Add new plate:
        1. Please press the "Add new plate" button, after the popup window appears, then scan the barcode on 
        the plate.
        2. After the scanning is done, press the "cancel" button.

    Remove plate:
        1. Please check the checkbox at the row that you like to remove, plates at rows that aren't checked 
        will not be removed.
        2. Deletion will be applied immediately after pressing the OK button in popup window
    
    Assign plate to user:
        1. Only the plate that display "TRUE" at "Avaliable_for_assign" column can be assigned.
        2. Please check the checkbox at the row that you like to assign, plates at rows that aren't checked 
        will not be assigned.
        3. Please input the correct user ID, it's capital sensitive.

    Deassign plate from user:
        1. Please check the checkbox at the row that you like to deassign, plates at rows that aren't checked 
        will not be deassigned.
        

