import sqlite3 as sq



def sql_start():
    global base, cur
    base = sq.connect("account.db")
    cur = base.cursor()
    if base:
        print("Data base connected OK!")
    base.execute(
        "CREATE TABLE IF NOT EXISTS account(surname TEXT)"
    )
    base.commit()

async def sql_add_command(data):
    cur.execute("INSERT INTO account VALUES(?)", tuple(data.values()))
    base.commit()
