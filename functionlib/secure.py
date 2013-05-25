import hashlib

def securepw(password):
    sec = hashlib.md5(password).hexdigest()
    return sec

def checkpassword(input_password,db_password):
    input_password = securepw(input_password)
    if input_password == db_password:
        return True
    else:
        return False
