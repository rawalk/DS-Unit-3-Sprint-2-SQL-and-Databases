import psycopg2
import pandas as pd 

conn = psycopg2.connect(dbname = 'zobapumt', 
                        user = 'zobapumt',
                        password = '0q0ngkWVlh7bI5r0V11BwlS7eX5R9Ni-',
                        host = 'ruby.db.elephantsql.com')
curs = conn.cursor()

df = pd.read_csv("titanic.csv")
print(df.shape)

query = '''
CREATE TABLE titanic (
    id SERIAL PRIMARY KEY,
    Survived boolean,
    Pclass int4,
    Name text,
    Sex text,
    Age int4,
    Siblings int4,
    Parents int4,
    Fare float8
);
'''
curs.execute(query)
def get_statement(row):
    base =  "INSERT INTO titanic (Survived, Pclass, Name, Sex, Age, Siblings, Parents, Fare) VALUES "
    row[2] = row[2].replace("'", "")
    return base + str(tuple(row)) + ";"
for row in df.values:
    query = get_statement(row)
    curs.execute(query)
conn.commit()
query = "SELECT COUNT(*) FROM titanic"
curs.execute(query)
print(curs.fetchone())