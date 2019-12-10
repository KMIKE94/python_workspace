from flask import Flask
import mysql.connector
import json

app = Flask(__name__)

@app.route("/")
def hello():
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="user",
        password="password",
        database="db"
    )

    mycursor = mydb.cursor()
    stmt = "SELECT * from Users;"
    mycursor.execute(stmt)

    myDict = {}
    for (emp_id, employee_name) in mycursor:
        print(str(emp_id) + "\t" + employee_name)
        myDict.update({emp_id:employee_name})  
    
    j = json.dumps(myDict)
    print(j)
    return j


if __name__ == "__main__":
    app.run()