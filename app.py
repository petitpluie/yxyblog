from turtle import title
from flask import Flask, redirect, render_template, request, flash, url_for
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yxyblog_is_online'

# 获取数据库连接
def get_db_conn():
    conn = sqlite3.connect('./db/yxyblog.db')
    # 获取结果为py字典格式
    conn.row_factory = sqlite3.Row
    return conn

# 从数据库取文章数据
def get_db_data_by_id(blog_id):
    conn = get_db_conn()
    blog = conn.execute('select * from blog where id = ?',(blog_id, )).fetchone()
    return blog

# 博客首页，查看博客列表
@app.route('/')
def index():
    conn = get_db_conn()
    blogs = conn.execute('select * from blog order by created desc').fetchall()  # 从句柄获取data
    html = render_template('index.html', blogs = blogs)
    return html

# 创建一篇博客
@app.route('/blog/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if not title:
            flash('请输入文章标题')
        elif not content:
            flash('请输入文章内容')
        else:
            conn = get_db_conn()
            conn.execute(
                'insert into blog (title,content) values (?,?)', (title, content))
            conn.commit()
            conn.close()
            flash('文章保存成功')
            return redirect(url_for('index'))
    return render_template('new.html')

# 查看一篇博客
@app.route('/blog/<int:blog_id>')
def blog(blog_id):
    blog = get_db_data_by_id(blog_id)
    return render_template('blog.html', blog=blog)

# 删除一篇博客
@app.route('/blog/<int:blog_id>/delete', methods=['POST',])
def delete(blog_id):
    blog = get_db_data_by_id(blog_id)
    if(not blog):
        flash('文章不存在')
    conn = get_db_conn()
    conn.execute('DELETE FROM blog WHERE id = ?',(blog_id,))
    conn.commit()
    conn.close()
    flash('文章删除成功')
    return redirect(url_for('index'))

# 修改一篇文章
@app.route('/blog/<int:blog_id>/edit', methods=['GET','POST'])
def edit(blog_id):
    blog = get_db_data_by_id(blog_id)
    if(not blog):
        flash('文章不存在')
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if not title:
            flash('标题不能为空')
        elif not content:
            flash('内容不能为空')
        else:
            conn = get_db_conn()
            conn.execute('UPDATE blog SET title = ?, content = ? WHERE id = ?', (title, content, blog_id))
            conn.commit()
            conn.close()
            flash('修改已保存')
            return redirect(url_for('index'))
    return render_template('edit.html', blog = blog)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8090)
