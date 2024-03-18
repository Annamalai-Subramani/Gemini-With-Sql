import sqlite3

## Connectt to SQlite
connection=sqlite3.connect("student.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()

## create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""
cursor.execute(table_info)

## Insert Some more records

cursor.execute('''Insert Into STUDENT values('Jaso','Data Science','A',96)''')
cursor.execute('''Insert Into STUDENT values('Nilani','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Hari sri','Data Science','A',97)''')
cursor.execute('''Insert Into STUDENT values('Annamalai','DEVOPS','A',70)''')
cursor.execute('''Insert Into STUDENT values('Gopi','DEVOPS','A',85)''')

## Disspaly ALl the records

print("The isnerted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()