import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="user",
    passwd="password",
    database="db"
)

mycursor = mydb.cursor()

create_stmt = "CREATE TABLE User(emp_id int, name varchar(255))"
mycursor.execute(create_stmt)

insert_stmt = "INSERT INTO User (emp_id, name) VALUES (%d, %s)"
val = [
    (1, 'Keith'),
    (2, 'Emma'),
    (3, 'Yuri'),
    (4, 'James'),
    (5, 'Jack'),
    (6, 'Shane'),
]

mycursor.executemany(insert_stmt, val)
mydb.commit()

print("LastRow: ", mycursor.lastrowid)