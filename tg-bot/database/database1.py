import sqlite3 as sq

def sql_start():
    global base, cur
    base = sq.connect('account.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    base.execute('CREATE TABLE IF NOT EXISTS account(id INTEGER,surname TEXT, name TEXT,surname_1 TEXT ,date_born TEXT, job_title TEXT, departament TEXT, gender TEXT, root TEXT)')
    base.commit()

    async def sql_add_command(state):
        async with state.proxy() as data:
            cur.execute('INSERT INTO account VALUES(?,?,?,?)', tuple(data.values()))
            base.commit()