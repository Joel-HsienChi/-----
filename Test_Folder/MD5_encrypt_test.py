import hashlib

def get_md5(str):
    hash_md5 = hashlib.md5()
    hash_md5.update(str.encode("utf-8"))
    return hash_md5.hexdigest()

password = ('1')

print(get_md5(password))