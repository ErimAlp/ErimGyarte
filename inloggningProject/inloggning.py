from db.index import db
import bcrypt

def create_account(username, password):
    password = password.encode()
    hash_password = bcrypt.hashpw(password, bcrypt.gensalt())
    hash_password = hash_password.decode()
    print(username, password)
    user = {"name": username, 
    "password": password }
    db.child("users").push(user)
    print(user)

def login(username, password):
    db_user = db.child("users").order_by_child("name").equal_to(username).get().val().values()
    db_user = list(db_user)[0]
    # print(db_user)
    if password == db_user["password"]:
    # if bcrypt.checkpw(password, hash_pw):
        print("logged in")
    else:
        print("wrong password")

# username = input("Username: ")
password = input("Password: ")
password = password.encode()
hash_password = bcrypt.hashpw(password, bcrypt.gensalt())
print(hash_password)


# create_account(username, password)
# login(username, password)