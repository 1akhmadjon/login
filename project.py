import json
import os

class File:
    def __init__(self,file):
        self.file=file

    def read(self):
        with open(self.file)as f:
            try:
                arr=json.load(f)
            except:
                arr =[]
            return arr
    def write(self,data):
        with open(self.file,'w')as f:
            json.dump(data,f,indent=3)


class User:
    def __init__(self,Firstname=None,Lastname=None,Username=None,Password=None):
        self.Firstname = Firstname
        self.Lastname = Lastname
        self.Username = Username
        self.Password = Password

    def save_user(self):
        f = File("data.json")
        date = f.read()
        date.append(self.__dict__)
        f.write(date)
    def check_register(self):
        with open('data.json', 'r') as f:
            data = json.load(f)
        b = True
        for i in data:
            if i["Username"]==self.Username and i["Password"]==self.Password:
                b = False
                break
        return b


    def check_login(self,uname,password):
        with open('data.json', 'r') as f:
            data = json.load(f)
        for i in data:
            if i["Username"]==uname and i["Password"]==password:
                return True

        return False




print("1 Login")
print("2 Register")
n = int(input(">>>"))
if n==1:
    os.system('cls')
    name = input("User name:")
    password = input("Password:")
    Email = input("Email:")
    save = User(Username=name,Password=password)
    if save.check_login(name,password):
        print("Login successful!")
    else:
        raise Exception("Login Error!")

if n==2:
    os.system('cls')
    Firstname = input("Firstname:")
    Lastname = input("Lastname:")
    Username = input("Username:")
    Email = input("Email:")
    Password = input("Password:")
    save = User(Firstname,Lastname,Username,Password)
    if save.check_register():
        save.save_user()
        print("Registration successful")
    else:
        raise Exception("Registration Error!")
