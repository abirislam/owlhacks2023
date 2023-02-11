import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Abirthefool7',
    port='3306',
    database='owlhacks2023'
)

c = connection.cursor()
c.execute('SELECT * FROM userdata')
print(c.fetchall())
