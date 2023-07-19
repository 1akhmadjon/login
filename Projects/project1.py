import sqlite3
import os
from datetime import datetime
def con():
    conn = sqlite3.connect('base.db')
    return conn

def table_accounts():
    conn = con()
    cur = conn.cursor()
    cur.execute("""
        create table if not exists accounts(
            id integer not null primary key autoincrement,
            first_name varchar(30),   
            last_name varchar(30),
            gmail varchar(50),
            username varchar(50),
            password varchar(50),
            phone varchar(13),
            reg_datatime datatime
        )
    """)
    conn.commit()
    conn.close()
table_accounts()

#
# def ragister_accounts(data: dict):
#     conn = con()
#     cur = conn.cursor()
#     query = """
#         insert into accounts(
#             first_name,
#             last_name,
#             gmail,
#             username,
#             password,
#             phone,
#             reg_datatime
#         )values (?, ?, ?, ?, ?, ?)
#     """
#     values = (data['first_name'], data['last_name'], data['gmail'], data['username'], data['password'], data['phone'],datetime.now())
#     if data['password'] == data['password1']:
#         if is_exist('username',data['username']):
#             print("This username is already exists!!!")
#             return 405
#         if is_exist('gmail', data['gmail']):
#             print("This gmail is already exists!!!")
#             return 405
#         cur.execute(query, values)
#         conn.commit()
#         conn.close()
#         return 201
#     else:
#         print('Password are not same!!!')
#         return 405
#
# def is_exist(field, field_data):
#     query = f"""
#         select count(id) from accounts where{field}=?
#     """
#     value = (field_data)
#     conn = con()
#     cur = conn.cursor()
#     cur.execute(query, value)
#     return cur.fetchone()[0]