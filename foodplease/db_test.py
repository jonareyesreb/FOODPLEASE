import MySQLdb

try:
    db = MySQLdb.connect(
        host="127.0.0.1",
        user="root",
        passwd="",  
        db="menu"
    )
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print("Database version : %s " % data)
    db.close()
except MySQLdb.OperationalError as e:
    print(f"Error: {e}")

