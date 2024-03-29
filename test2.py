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

fields = ['fio', 'date', 'number_phone', 'job_title', 'departament', 'gender', 'root']
cur.execute('SELECT fio, date_born, number, job_title, gender, rights FROM account WHERE created=0;')
cur.execute('SELECT  * FROM account LIMIT 1')
accounts = cur.fetchall()
for account in accounts:
    print(type(account))
print(account)
base.close()
dictionary_data= dict(zip(fields, account))
print(dictionary_data)