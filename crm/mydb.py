import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shaurya@123!",
)
# Prepare a cursor object
cursorObject = dataBase.cursor()

# create a cursor object
cursorObject.execute("CREATE  DATABASE  elderco")

print("ALL done")