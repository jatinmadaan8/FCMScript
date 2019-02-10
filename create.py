#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database = "testdb2", user = "postgres", password = "namespace1", host = "127.0.0.1", port = "5432")
print ('Opened database successfully')

cur = conn.cursor()
cur.execute('''CREATE TABLE COMPANY
      (
      NAME           TEXT    NOT NULL);''')
print ('Table created successfully')

cur.execute("INSERT INTO COMPANY (NAME) \
      VALUES ('rahul')");
print ('Table inserted successfully')

cur.execute("SELECT name  from COMPANY")
rows = cur.fetchall()
for row in rows:
   print ("NAME = ", row[0])

print ("fetched successfully");

conn.commit()
conn.close()
