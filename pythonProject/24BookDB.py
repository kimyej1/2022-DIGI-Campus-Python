# 24BookDB.py

import sqlite3

def createTable():
    print(">> CREATE TABLE...")
    conn = sqlite3.connect("customer.db")
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE kb_customer_table(
            idx        integer primary key,
            name       text, 
            age        integer,
            mobile     text
        )    '''
    )

    conn.commit()
    conn.close()

def updateCustomer():
    print(">> UPDATE CUSTOMER...")
    conn = sqlite3.connect("customer.db")
    cur = conn.cursor()

    key = int(input("insert key : "))
    mobile = input("insert mobile : ")

    sql = "UPDATE kb_customer_table SET mobile = ? WHERE idx = ?"
    cur.execute(sql,(mobile, key))
    conn.commit()
    conn.close()

def insertCustomer():
    print(">> INSERT CUSTOMER...")
    conn = sqlite3.connect("customer.db")
    cur = conn.cursor()

    sql = "Insert into kb_customer_table (name, age, mobile)" \
          "values (?, ?, ?)"

    customers = [
        ('김국민', 13, '01012345678'),
        ('이신한', 46, '0119876543'),
        ('최하나', 24, '01013572468'),
        ('박우리', 36, '01024681357'),
        ('신기업', 64, '0192583457')
    ]

    cur.executemany(sql, customers)

    conn.commit()
    conn.close()

def selectCustomer():
    print(">> SELECT CUSTOMER...")
    conn = sqlite3.connect("customer.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM kb_customer_table")
    customers = cur.fetchall()
    for customer in customers:
        print(customer)

    conn.close()

if __name__ == "__main__":

    createTable()
    insertCustomer()

    selectCustomer()
    updateCustomer()
    selectCustomer() # Update 후 확인