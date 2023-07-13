import base64
import datetime
from tkinter import *
from functools import partial



# Initial UI design
# window
tkWindow = Tk()  
tkWindow.title('Login_Page')
tkWindow.geometry('500x300')	
  
# Printout login information
def validateLogin(username, password):
	# Print the username and password
	print("username entered :", username.get())
	print("password entered :", password.get())

	# Encoding the string
	encode = base64.b64encode(password.get().encode("utf-8"))
	print("str-byte : ", encode)	

	# Decoding the string
	decode = base64.b64decode(encode).decode("utf-8")
	print("byte-str : ", decode)

	# Get login time
	login_time = datetime.datetime.now()
	print("login time : ", login_time)
	return

def register(username, password):
	# Print the username and password
	print("username entered :", username.get())
	print("password entered :", password.get())
	return

def login_window():
	# username label and text entry box
	usernameLabel = Label(tkWindow, text="User Name").pack()
	username = StringVar()
	usernameEntry = Entry(tkWindow, textvariable=username).pack()

	# password label and password entry box
	passwordLabel = Label(tkWindow,text="Password").pack()
	password = StringVar()
	passwordEntry = Entry(tkWindow, textvariable=password, show='*').pack()

	validateLogin_par = partial(validateLogin, username, password)

	#login button
	loginButton = Button(tkWindow, text="Login", command=validateLogin_par).pack()
	
	#register button
	registerButton = Button(tkWindow, text="Register", command=registration_window).pack()

	tkWindow.mainloop()

def registration_window():
	# registration window UI
	tkWindow.destroy()
	registration_tk = Tk()
	registration_tk.title('register')
	registration_tk.geometry('500x300')	

	# username label and text entry box
	usernameLabel = Label(registration_tk, text="Enter the User Name").pack()
	username = StringVar()
	usernameEntry = Entry(registration_tk, textvariable=username).pack()

	# password label and password entry box
	passwordLabel = Label(registration_tk,text="Enter the Password").pack()
	password = StringVar()
	passwordEntry = Entry(registration_tk, textvariable=password, show='*').pack()

	registration = partial(register, username, password)

	registerbutton = Button(registration_tk, text="Register", command=registration).pack()

	registration_tk.mainloop()


login_window()