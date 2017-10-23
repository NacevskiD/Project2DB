import sqlite3
import pandas as pd

class myDB():
    def __init__(self):
        self.dbName = "Database.sqlite"
        self.conn = sqlite3.connect(self.dbName)
        self.c = self.conn.cursor()
        self.tableName1 = "Information"
        self.id1 = "ID"
        self.column1 = "FirstName"
        self.column2 = "LastName"
        self.column3 = "Employed"
        self.column4 = "Phone"
        self.column5 = "Salary"
        self.column6 = "Date"

    def dropTable(self):
        self.c.execute('DROP TABLE Information')
        self.conn.commit()

    def createTable(self):
        try:
            self.c.execute('CREATE TABLE Information (ID INTEGER PRIMARY KEY ,FirstName TEXT,LastName TEXT,'
                           'Employed BOOLEAN DEFAULT FALSE,Phone INTEGER,Salary FLOAT DEFAULT 0,Date DATE)')
            self.conn.commit()
            print("Database and table created.")
        except sqlite3.OperationalError:
            print("Table and database already exist.")

    def alterDatabase(self,id,firstName,lastName,employed,phone,salary,date):
        arguments = [firstName, lastName, employed, phone, salary,date,id]
        self.c.execute('UPDATE Information SET FirstName = ?, LastName = ?, Employed = ? , Phone = ?,Salary = ?,Date = ? WHERE ID = ?',arguments)
        self.conn.commit()

    def addItem(self,firstName,lastName,employed,phone,salary,date):
        arguments = [firstName,lastName,employed,phone,salary,date]
        self.c.execute('INSERT INTO Information(FirstName,LastName,Employed,Phone,Salary,Date) VALUES (?,?,?,?,?,?)',arguments)
        self.conn.commit()

    def deleteItem(self,id):

        self.c.execute('DELETE FROM Information WHERE ID =?',(id,))
        self.conn.commit()

    def showAll(self):
        print(pd.read_sql_query('SELECT * FROM Information',self.conn))

    def showSingle(self,id):
        print(pd.read_sql_query('SELECT * FROM Information WHERE ID=?',self.conn,params= id))

    def closeConnection(self):
        self.conn.close()
