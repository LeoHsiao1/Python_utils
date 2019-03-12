import sqlite3

# 连接到SQLite数据库,如果文件不存在，会自动在当前目录创建

db = sqlite3.connect("2019_03_09_090131.17.db3")
# db = sqlite3.connect(":memory:")# 使用":memory:"可在内存中打开一个数据库，这样就可使用其SQL语句

db.execute("CREATE TABLE table1(id INT PRIMARY KEY, name TEXT)")
db.execute("INSERT INTO table1 (id,name) VALUES (1,'one')")
datas = [(i, str(id(i))) for i in range(1, 100)]
db.executemany("INSERT INTO table1 (id, name) VALUES (?, ?)", datas)  # 从一个可迭代对象中提取一系列元组插入数据库

db.execute("UPDATE table1 set name=? where id=?", ("one", 1))


db.execute("SELECT * FROM table1")  # 执行一条SQL语句，选取指定表中的数据
# db.execute("SELECT * FROM table1 WHERE id=? AND name=?", (1, "one"))

# db.commit()  # 提交对数据库的修改
# connection.rollback() # 该方法回滚自上一次调用 commit() 以来对数据库所做的更改。
db.close()
