import pymysql

dataBase = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Tien@@1994'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE quoctien")

print("All done!")