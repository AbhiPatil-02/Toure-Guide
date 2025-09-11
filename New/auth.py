import hashlib
from data_manager import add_user, check_user

def hash_pwd(password):
    return hashlib.sha256(password.encode()).hexdigest()

def signup(username, password):
    add_user(username, hash_pwd(password))

def login(username, password):
    return check_user(username, hash_pwd(password))
