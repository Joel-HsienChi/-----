# importing base64 modules for
# encoding & decoding string
import base64
 
password = "Thisisthepassword"
 
# Encoding the string
encode = base64.b64encode(password.encode("utf-8"))
print("str-byte : ", encode)
 
# Decoding the string
decode = base64.b64decode(encode).decode("utf-8")
print("byte-str : ", decode)