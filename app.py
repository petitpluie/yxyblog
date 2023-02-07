from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# 获取数据库连接
def get_db_conn():
    conn = sqlite3.connect('./db/blog.db')
    # 获取结果为py字典格式
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_conn()
    data = conn.execute('select * from posts').fetchall() # 从句柄获取data
    html = render_template('index.html', data = data)
    print('******')
    print('ffff')
    return html

if __name__ == '__main__':
    app.run(debug = False, host = '0.0.0.0', port = 8090)
