from flask import g
import sqlite3

def connect_db():
    sql = sqlite3.connect('/home/mickey/Courses_and_Tutorials/Flask/add_food_to_db/food_log.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db
