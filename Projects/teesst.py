from project1 import table_accounts, ragister_accounts

# first_name = input("Firstname: ")
# last_name = input("lastname: ")
# while True:
#     gmail = input("Create new gmail: ")
#     if gmail[-10:]=='@gmail.com':
#         break
#     else:
#         print("Error!")
#         continue
#
# username = input("Enter your username: ")
# while True:
#     password1 = input("Enter your password: ")
#     if len(password1) >= 8:
#         break
#     else:
#         print("Error!")
#         continue
#
# password2 = input("Password confirm: ")

data =dict(
    first_name = input("Firstname: "),
    last_name = input("lastname: "),
    gmail = input("Create new gmail: "),
    username = input("Enter your username: "),
    password=input("Enter your password: "),
    password1 = input("Password confirm: "),
    phone = input("Phone: ")
)

response = ragister_accounts(data)
if response == 201:
    print("okeey")

if __name__ == '__main__':
    table_accounts()