import pandas as pd, sqlite3

conn = sqlite3 .connect('Data.db')

def createTable():
    try:
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS Student_Data
                 (Name, Age, Gender)""")
    except Exception as e:
        pass

def insert(name, age, gender):
    c = conn.cursor()
    c.execute(f"INSERT INTO Student_Data(Name, Age, Gender) values('{name}', {age}, '{gender}')")

def queryExec():
    createTable()
    insert("Jack", 18, "Male")
    insert("Gwen", 20, "Female")
    result = pd.read_sql_query("select * from Student_Data",conn)
    return result

r = queryExec()
print(r)