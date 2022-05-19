import psycopg2
import pandas as pd
from sqlalchemy import create_engine

conn_string = 'postgresql://postgres:Passw0rd@1a@localhost:5432/mydb'

db = create_engine(conn_string)
conn = db.connect()

df = pd.read_csv("employee1.csv")
df.to_sql('data',con = conn,if_exists='append',index=False)
conn = psycopg2.connect(conn_string)
conn.autocommit = True
cursor = conn.cursor()
print("all okay...")

input()
conn = psycopg2.connect(database = "mydb",user = "postgres",password = "Passw0rd@1a",
                        host = '127.0.0.1',port = '5432')

conn.autocommit = True

cursor = conn.cursor()

df = pd.read_csv("employee1.csv")
df.to_sql('data',con = conn ,index= False)
