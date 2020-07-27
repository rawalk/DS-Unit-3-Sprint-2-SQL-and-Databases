import psycopg2

DB_NAME = 'zobapumt'
DB_USER = 'zobapumt'
DB_PASSWORD = '0q0ngkWVlh7bI5r0V11BwlS7eX5R9Ni-'
DB_HOST = 'ruby.db.elephantsql.com'

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR:", cursor)

cursor.execute('SELECT * from test_table;')
result = cursor.fetchall()
print("RESULT:", type(result))
print(result)