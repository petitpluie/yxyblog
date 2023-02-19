import sqlite3

def get_db_conn():
    conn = sqlite3.connect('./db/yxyblog.db')
    # 获取结果为py字典格式
    conn.row_factory = sqlite3.Row
    return conn

def run_sql_command():
    conn = get_db_conn()
    result = conn.execute('select * from blog').fetchall()
    print(result)


if __name__ == "__main__":
    run_sql_command()
