import hashlib
import os

def Hash(password):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    ret = salt + key
    
    return ret

def verify(newpassword, storedpassword):
    salt = storedpassword[:32]
    key = storedpassword[32:]
    
    newkey = hashlib.pbkdf2_hmac('sha256', newpassword.encode('utf-8'), salt, 100000)
    
    if newkey == key:
        return True
    else:
        return False
    