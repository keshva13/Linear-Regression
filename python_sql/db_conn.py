import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="mydb", user='postgres', password='Passw0rd@1a', host='127.0.0.1', port= '5432'
)

# #Creating a cursor object using the cursor() method
# cursor = conn.cursor()
#
# #Doping EMPLOYEE table if already exists.
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
#
# #Creating table as per requirement
# sql ='''CREATE TABLE EMPLOYEE(
#    FIRST_NAME CHAR(20) NOT NULL,
#    LAST_NAME CHAR(20),
#    AGE INT,
#    SEX CHAR(1),
#    INCOME FLOAT
# )'''
# cursor.execute(sql)
# print("Table created successfully........")
# conn.commit()
# #Closing the connection
# conn.close()
#


#Setting auto commit false
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing SQL queries to INSERT a record into the database.
cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX,
   INCOME) VALUES ('Ramya', 'Rama priya', 27, 'F', 9000)''')
cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX,
   INCOME) VALUES ('Vinay', 'Battacharya', 20, 'M', 6000)''')
# cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX,
#    INCOME) VALUES ('Sharukh', 'Sheik', 25, 'M', 8300)''')
# cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX,
#    INCOME) VALUES ('Sarmista', 'Sharma', 26, 'F', 10000)''')
# cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX,
#    INCOME) VALUES ('Tripthi', 'Mishra', 24, 'F', 6000)''')

# Commit your changes in the database
conn.commit()
print("Records inserted........")

# Closing the connection
conn.close()