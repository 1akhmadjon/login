from database import create_table_user,insert_user, login, activate_user
from Eemail import send_mail
from utils import generate_code,generate_token
n = input("""
1.regiter
2.login
>>>""")
if n=='1':
    data = dict(
        first_name = input("Firstname:"),
        last_name = input("Lastname:"),
        email = input("Email:"),
        username = input("Username:"),
        password = input("Password:"),
        password1 = input("Confirm Password:"),
    )
    res = insert_user(data)
    if res == 201:
        code = generate_code()
        send_mail(data['email'], code)
        print("Check your email")

        verification = input("code: ")
        if verification == code:
            activate_user({'username':data['username']})
            print("Done")
        else:
            print("Invalid code!")

elif n=='2':
    user = dict(
        username = input("Username: "),
        password = input("Password: ")
    )
    response = login(user)
    if response:
        print("Welcome to our website")
    else:
        print("Invalid username or password!")

if __name__ == '__main__':
    create_table_user()

