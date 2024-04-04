import sqlite3 as sq


def sql_start():
    global base, cur
    base = sq.connect("account.db")
    cur = base.cursor()
    if base:
        print("Data base connected OK!")
    base.execute(
        "CREATE TABLE IF NOT EXISTS account(id  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,fio TEXT,date_born TEXT, number TEXT, job_title TEXT,departament TEXT ,gender TEXT,rights TEXT ,created INTEGER, date_created DATETIME DEFAULT (datetime('now','localtime')))"

    )
    base.commit()


async def sql_add_command(data):
    cur.execute("INSERT INTO account (fio, date_born, number, job_title, departament,gender, rights,created) VALUES(?,?,?,?,?,?,?,0)", tuple(data.values()))
    base.commit()
