import pymysql
pymysql.install_as_MySQLdb()

#打开数据库连接
db = pymysql.connect("localhost", "root", "1995","demos_db")

#使用cursor()方法获取操作游标
cursor = db.cursor()

#使用execute方法执行SQL操作
cursor.execute("SELECT VERSION()")

#使用fetchone()方法获取一条数据库
data = cursor.fetchone()

print("Database version : %s "%data)

#关闭数据库连接
db.close()