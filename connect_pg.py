import psycopg2
import os
import datetime
import setting

# print(psycopg2.apilevel)

DATABASE_URL = os.environ.get('DATABASE_URL')

def get_connection():
    return psycopg2.connect(DATABASE_URL)


def create_table():
    #citiesテーブルが存在したらdrop
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS nightcore')

    #CREATE
    cur.execute('''
        CREATE TABLE nightcore (
            clip_id text UNIQUE,
            t timestamp NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def insert(clip_id):
    
    conn = get_connection()
    cur = conn.cursor()
    #INSERT
    dt = datetime.datetime.now()

    cur.execute('INSERT INTO nightcore VALUES(%s, %s)', (clip_id,  dt))

    # cur.execute('INSERT INTO cities VALUES (%(rank)s, %(city)s, %(population)s)',
    #   {'rank': 2, 'city': 'カラチ', 'population': 23500000})

    # cur.executemany(' INSERT INTO cities VALUES (%(rank)s, %(city)s, %(population)s)', [ 
    #   {'rank': 3, 'city': '北京', 'population': 21516000}, 
    #   {'rank': 4, 'city': '天津', 'population': 14722100}, 
    #   {'rank': 5, 'city': 'イスタンブル', 'population': 14160467}
    # ])


    conn.commit()
    conn.close()

def select(clip_id):
    #SELECT
    res = False
 
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM nightcore WHERE clip_id = %s', (clip_id,))
            if cur:
                 for row in cur:
                     res = True
            else:
                res = False

    conn.close()
    return res


def delete(clip_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute('DELETE FROM nightcore WHERE clip_id = %s', (clip_id,))

    conn.commit()
    conn.close()


def select_all():
    #SELECT
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM nightcore')
            if cur:
                 for row in cur:
                     print(row)
            else:
                return False

    conn.close()
