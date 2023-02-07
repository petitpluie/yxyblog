import sqlite3

conn = sqlite3.connect('./db/blog.db')  # db/blog.db

with open('./db/db.sql') as f:
    str_sql = f.read()
    conn.executescript(str_sql)

# 创建一个执行句柄
cur = conn.cursor()

# 执行sql语句
cur.execute('INSERT INTO posts (title, content) VALUES (?, ?)', ('文章一', '如何学习python?')) 
cur.execute('INSERT INTO posts (title, content) VALUES (?, ?)', ('第二篇文章', 'python基础语法'))

conn.commit()
conn.close()
