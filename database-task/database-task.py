import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def select_rows_by_conditions(conn, first_condition=None, second_condition=None, sort_condition=None):
    cur = conn.cursor()
    sql_select_query = """select * from Talks where """ + first_condition + """ and """ + \
                       second_condition + """ order by """ + sort_condition + """ asc """ + """;"""
    cur.execute(sql_select_query)
    rows = cur.fetchall()
    for row in rows:
        print(row[1])


database = input()
first_condition = str(input())
second_condition = str(input())
sort_condition = str(input())
conn = create_connection(database)
with conn:
    select_rows_by_conditions(conn,
                              first_condition,
                              second_condition,
                              sort_condition)
