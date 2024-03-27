import sqlite3 as sq


def sql_start():
    global base, cur
    base = sq.connect("account.db")
    cur = base.cursor()
    if base:
        print("Data base connected OK!")
    base.execute(
        "CREATE TABLE IF NOT EXISTS account(fio TEXT,date_born TEXT, number TEXT, job_title TEXT, gender TEXT,rights TEXT ,created INTEGER)"
    )
    base.commit()


async def sql_add_command(data):
    cur.execute("INSERT INTO account VALUES(?,?,?,?,?,?,0)", tuple(data.values()))
    base.commit()
