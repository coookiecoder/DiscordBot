import os

from psycopg2 import connect

connection = connect(dbname="default", user="postgres", password=os.environ.get('DATABASE_PASSWORD', 'nope'), host="database", port="5432")
cursor = connection.cursor()

def validate_table_role() -> None:
    try:
        cursor.execute(f'CREATE TABLE IF NOT EXISTS role (role_id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL, emoji VARCHAR(255) NOT NULL)')
        connection.commit()
    except:
        connection.rollback()

def validate_table_twitch() -> None:
    try:
        cursor.execute(f'CREATE TABLE IF NOT EXISTS twitch (link VARCHAR(255) NOT NULL PRIMARY KEY)')
        connection.commit()
    except:
        connection.rollback()

def validate_table_youtube() -> None:
    try:
        cursor.execute(f'CREATE TABLE IF NOT EXISTS youtube (link VARCHAR(255) NOT NULL PRIMARY KEY)')
        connection.commit()
    except:
        connection.rollback()

def add_role(name: str, role_id: str, emoji:str) -> None:
    try:
        cursor.execute(f'INSERT INTO role (role_id, name, emoji) VALUES (%s, %s, %s)', (role_id, name, emoji))
        connection.commit()
    except:
        connection.rollback()

def add_twitch(link: str) -> None:
    try:
        cursor.execute(f'INSERT INTO role (link) VALUES (%s, %s, %s)', link)
        connection.commit()
    except:
        connection.rollback()

def add_youtube(link: str) -> None:
    try:
        cursor.execute(f'INSERT INTO role (link) VALUES (%s, %s, %s)', link)
        connection.commit()
    except:
        connection.rollback()

def remove_role(name: str) -> None:
    pass

def remove_twitch(name: str) -> None:
    pass

def remove_youtube(name: str) -> None:
    pass