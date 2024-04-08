import logging

import sqlite3 as sq

logging.basicConfig(filename="app.log", level=logging.INFO)

base = sq.connect("account.db")
if base:
    logging.info("База подключена ОК")
else:
    logging.error("База не подключилась, чиниииииии")
    exit()
cur = base.cursor()


fields = [
    "id",
    "fio",
    "date",
    "number_phone",
    "job_title",
    "departament",
    "gender",
    "root",
]
cur.execute("SELECT  * FROM account LIMIT 1")
cur.execute("SELECT id, fio, date_born, number, job_title, departament,gender, rights FROM account WHERE created=0")

accounts = cur.fetchall()
for account in accounts:
    ...

dictionary_data = dict(zip(fields, account))


id = dictionary_data["id"]
fio = (dictionary_data["fio"]).split()
family = fio[0]
name = fio[1]
surname = fio[2]
date = dictionary_data["date"]
number_phone = dictionary_data["number_phone"]
job_title = dictionary_data["job_title"]
departament = dictionary_data["departament"]
gender = dictionary_data["gender"]
root = dictionary_data["root"]

cur.execute(f"UPDATE account SET created=1 WHERE id = {id}")
base.commit()
base.close()


# def account_created():
#    cur.execute(f'UPDATE account SET created=1 WHERE id = {id}')
#    base.commit()
#    base.close()
# number_phone
# job_title
# gender
# root
# print(family)
# print(name)
# print(surname)
# print(date)
# print(number_phone)
# print(job_title)
# print(departament)
# print(gender)
# print(root)
