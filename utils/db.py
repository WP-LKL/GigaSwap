import sqlite3 
from flask import g

DATABASE = './database.db'

def get_db():
    if 'db' not in g:
        g.db = g._database = sqlite3.connect(DATABASE)
    return g.db
    
def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def clean_db(table):
    cur = get_db().execute('delete from ?', table)
    cur.close()
  
def insert_db(query, rows):
    with sqlite3.connect(DATABASE) as db:
        db.executemany(query, rows)
        db.commit()


# TODO: Convert to async with aiosqlite
