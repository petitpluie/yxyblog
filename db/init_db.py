import sqlite3

conn = sqlite3.connect('./db/yxyblog.db')  # db/blog.db

# 获取结果为字典格式
conn.row_factory = sqlite3.Row

with open('./db/create_db.sql') as f:
    str_sql = f.read()
    conn.executescript(str_sql)

# 创建一个执行句柄
cur = conn.cursor()

# 执行sql语句
cur.execute('INSERT INTO blog (title, content) VALUES (?, ?)', ('文章一', '如何学习python?')) 
cur.execute('INSERT INTO blog (title, content) VALUES (?, ?)', ('第二篇文章', 'python基础语法'))
cur.execute('INSERT INTO blog (title, content) VALUES (?, ?)', ('第三篇', 'python字符串处理'))

conn.commit()
conn.close()
