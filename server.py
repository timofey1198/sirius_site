# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import session
from flask import redirect
from flask import url_for
from flask import escape
from content import html_all
import data
import os

app = Flask(__name__)
app.secret_key = 'd&hnkj;84H(Ffn97@)#38rf3c7uhf39^&@Tb8'

def valid_login(login, password):
    return ((data.is_password(login, password)))


@app.route("/login", methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['login'],
                       request.form['password']):
            session['login'] = request.form['login']
            return profile()
        else:
            error = 'error!!!'
    return index()

@app.route("/reg", methods=['POST', 'GET'])
def reg():
    if request.method == 'POST':
        if session['key'] == request.form['captcha']:
            user = request.form['login']
            password = request.form['password']
            if(not data.is_user(user)):
                data.new_user(user, password)
                return index()
    return register()

@app.route("/logout", methods=['POST', 'GET'])
def logout():
    session.pop('login', None)
    return index()

def login_form():
    if 'login' in session:
        login_form = ('<div class="enter_form">Hi, %s' 
                   % escape(session['login']) +
                   """
                    <br><br>
                    <a href="/logout">
                    <div class="button">Выйти</div>
                    </a>
                    </div>
                """)
    else:
        login_form = """
            <div class="enter_form">
                <form action="/login" method="POST">
                    <input type="text" name="login">
                    <input type="password" name="password">
                    <input type="submit" value="Войти">
                </form>
                <br>
                <a href="/register">
                <div class="button">Регистрация</div>
                </a>
            </div>
            """
    return login_form

def page_not_found_error():
    html = """
        <html>
            <body>
                <center>
                    <h1>Страница не найдена...</h1><br>
                    <a href="index">На главную</a>
                </center>
            </body>
        </html>
        """
    return html


@app.route("/news_handler", methods=['POST', 'GET'])
def news_handler():
    if request.method == 'POST':
        title = request.form['news_title']
        body = request.form['news_text']
        author = session['login']
        data.new_article(title, body, author)
        return news()
    return edit()

#------------------------------------PAGES--------------------------------------

@app.route("/")
@app.route("/index")
def index():
    menu = """
            <div class="menu_box">
                <a href="index"><div class="Menu-opened">Главная</div></a>
                <a href="news"><div class="Menu">Новости</div></a>
            </div>"""
    content = ''
    right_sidebar = login_form()
    return html_all(menu, content, right_sidebar)


@app.route("/register")
def register():
    
    menu = """
            <div class="menu_box">
                <a href="index"><div class="Menu">Главная</div></a>
                <a href="about"><div class="Menu">Обо мне</div></a>
                <a href="science"><div class="Menu">Наука</div></a>
                <a href="contacts"><div class="Menu">Контакты</div></a>
            </div>
            """
    content = """
            <div class="enter_form">
                <form action="/reg" method="POST">
                    <input type="text" name="login" required placeholder="Логин"><br>
                    <input type="password" name="password" required placeholder="Пароль"><br><br>
                    <img src="/captcha"><br><br>
                    <input type="text" name="captcha" required placeholder="Введите текст с картинки"><br>
                    <input type="submit" value="Регистрация">
                </form>
            </div>
            """
    return html_all(menu, content, '')

@app.route("/news")
def news():
    edit = ''
    if 'login' in session:
        user = session['login']
        if data.is_access(user, 0):
            edit = """
                <div class="header_block">
                <center><a href="edit">
                    <div class="add_new">Добавить новость</div>
                </a><center>
                </div>
            """
    menu = """
            <div class="menu_box">
                <a href="index"><div class="Menu">Главная</div></a>
                <a href="news"><div class="Menu-opened">Новости</div></a>
            </div>
            """
    news = ''
    files = os.listdir(path = 'pages/news')
    files.sort(key=lambda x: -int(x.split('.')[0]))
    for name in files:
        f = open('pages/news/' + name, 'r', encoding='utf-8')
        text = f.read()
        f.close()
        number = int(name.split('.')[0])
        info = data.get_articles_info(number)
        title = info[1]
        author = info[3]
        article = """
            <div class="news">
                <h3>%s</h3>
                <p>%s</p>
                <form action="news/article" method="POST">
                <input type="hidden" name="article_id" value="%s">
                <input type="submit" value="Подробнее" style="
                        background: inherit;
                        border: 0px;
                        color: red;
                        cursor: pointer;
                        ">
                </form>
                <br>
                <i>Автор: %s</i>
                <br><br>
                <hr>
            </div>
        """%(title, text, str(number), author)
        news += article
    content = edit + news
    right_sidebar = login_form() 
    return html_all(menu, content, right_sidebar)


@app.route("/news/article", methods=['POST', 'GET'])
def article():
    if request.method == 'POST':
        number = request.form['article_id']
        info = data.get_articles_info(int(number))
        title = info[1]
        author = info[3]
        path = 'pages/news/%s.txt'%info[2]
        f = open(path, 'r', encoding='utf-8')
        text = f.read()
        html = """
            <div class="news">
                <h3>%s</h3>
                <p>%s</p>
                <br>
                <i>Автор: %s</i>
                <br><br>
            </div>
        """%(title, text, author)
        menu = """
                <div class="menu_box">
                    <a href="/index"><div class="Menu">Главная</div></a>
                    <a href="/news"><div class="Menu">Новости</div></a>
                </div>
                    """        
        return html_all(menu, html, '')
    else:
        return redirect(url_for("news"))


@app.route("/contacts")
def contacts():
    return page_not_found_error()


@app.route("/science")
def science(): 
    return page_not_found_error()


@app.route("/edit")
def edit():
    menu = """
                <div class="menu_box">
                    <a href="index"><div class="Menu">Главная</div></a>
                    <a href="news"><div class="Menu">Новости</div></a>
                    <a href="profile"><div class="Menu">Профиль</div></a>
                </div>"""
    content = """
        <div class="news">
            <form action="/news_handler" method="POST">
                <input type="text" name="news_title" value="Заголовок"><br>
                <input type="text" name="news_text" value="введите текст новости" 
                  style="
                  width: 500px;
                  height: 400px;
                  text-align: left;
                  "><br>
                <input type="submit" value="Создать">
            </form>
        </div>
    """
    return html_all(menu, content, '')


@app.route("/profile")
def profile():
    menu = """
            <div class="menu_box">
                <a href="index"><div class="Menu">Главная</div></a>
                <a href="news"><div class="Menu">Новости</div></a>
                <a href="profile"><div class="Menu-opened">Профиль</div></a>
            </div>"""    
    if 'login' in session:
        content = ('<div class="content">Logged in as %s</div>' 
                   % escape(session['login']))
    else:
        content = '<div class="content">You are not logged in</div>'
    return html_all(menu, content, '')


#---------------------------------RESOURCES------------------------------------

@app.route("/style")
@app.route("/style.css")
def style():
    st = open('resources/style.css', 'r', encoding='utf-8')
    style = st.read()
    return style


@app.route("/img/top")
def top():
    img = open('resources/img/top.png', 'rb')
    return img.read()

@app.route("/captcha")
def captcha():
    key = data.captcha()
    session['key'] = key
    img = open('resources/img/captcha/%s.jpg' %key, 'rb')
    return img.read()


if __name__ == "__main__":
    app.run()