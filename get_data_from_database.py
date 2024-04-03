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

fields = ['fio', 'date', 'number_phone', 'job_title', 'gender', 'root']
cur.execute('SELECT  * FROM account LIMIT 1')
cur.execute('SELECT fio, date_born, number, job_title, gender, rights FROM account WHERE created=0')
accounts = cur.fetchall()
for account in accounts:
    ...

dictionary_data = dict(zip(fields, account))
print(dictionary_data.keys())
base.close()

fio = (dictionary_data['fio']).split()
family = fio[0]
name = fio[1]
surname = fio[2]
date = dictionary_data['date']
number_phone = dictionary_data['number_phone']
job_title = dictionary_data['job_title']
gender = dictionary_data['gender']
root = dictionary_data['root']



#number_phone
#job_title
#gender
#root



print(family)
print(name)
print(surname)
print(date)
print(number_phone)
print(job_title)
print(gender)
print(root)