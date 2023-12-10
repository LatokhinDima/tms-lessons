import sqlite3
from dataclasses import dataclass
from typing import Optional

from flask import Flask, abort, redirect, session, request
from flask_session import Session

DATABASE_FILE = 'sqlite.db'

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@dataclass
class Article:
    id: int
    title: str
    text: str
    author: str
    like_count: int


@dataclass
class User:
    id: int
    login: str
    password: str


def aut_user(login, password):
    with sqlite3.connect(DATABASE_FILE) as connection:
        execution_result = connection.execute(
            f'SELECT * FROM users WHERE login = ?', (login,))
        if x_user := execution_result.fetchone():
            user = User(*x_user)
        return user.password == password


def get_user(login) -> User:
    with sqlite3.connect(DATABASE_FILE) as connection:
        execution_result = connection.execute(f'''SELECT * FROM users WHERE login = ?''', (login,))
        return User(*execution_result.fetchone())


def get_all_articles() -> list[Article]:
    with sqlite3.connect(DATABASE_FILE) as connection:
        execution_result = connection.execute(
            'SELECT id, title, text, author, like_count FROM article')
        return [Article(*values) for values in execution_result.fetchall()]


def get_article(article_id: int) -> Article:
    with sqlite3.connect(DATABASE_FILE) as connection:
        execution_result = connection.execute('SELECT id, title, text, author, like_count '
                                              'FROM article '
                                              'WHERE id = ?', (article_id,))
        rows = execution_result.fetchall()
        if len(rows) != 1:
            raise ValueError(f'Expected 1 object with id {article_id}, got {len(rows)}')
        return Article(*rows[0])


def save_article(article: Article):
    with sqlite3.connect(DATABASE_FILE) as connection:
        data = (article.title, article.text, article.author, article.like_count, article.id)
        connection.execute('UPDATE article '
                           'SET title = ?, text = ?, author = ?, like_count = ?  '
                           'WHERE id = ?', data)


@app.route("/auth")
def page_auth():
    return f'''
                <html>
                    <head>
                        <title>Authenticate</title>
                    </head>
                        <body>
                            <h1 style="text-align: center;">Authenticate</h1>
                            <form action="/auth" method="post">
                                Login:    <input type="text" name="login"/><br>
                                Password: <input type="text" name="password"/><br>
                                <input type="submit" value="Sign in">                        
                            </form>
                        </body>
                </html>
            '''


@app.route('/')
@app.route('/articles')
def articles_view():
    articles = get_all_articles()
    articles_html = '\n'.join(
        f'<li><a href="/article/{article.id}">{article.title}</a></li>'
        for article in articles)

    return f'''
    <html>
        <head>
            <title>Articles APP</title>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.4.1/dist/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">
        </head>
        <body>
            <h1>All Articles</h1>
            <ul>
                {articles_html}
            </ul>
        </body>
    </html>
    '''


@app.route('/article/<int:id>')
def articles_id_view(id: int):
    article = get_article(id)
    if article is None:
        abort(404, 'Article not found')
    return f'''
    <html>
        <head>
            <title>Articles APP</title>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.4.1/dist/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">
        </head>
        <body>
            <p><a href="/articles">Go to home page</a></p>
            <h1>{article.title}</h1>
            <h3>{article.author}</h3
            <p>{article.text}</p>
            <form method="post" action="/article/like">
                <input type="hidden" name="article_id" value="{article.id}"/>
                <input type="submit" value="Like"/>
                <p>{article.like_count}</p>
            </form>
        </body>
    </html>
    '''


@app.route('/article/like', methods=['POST'])
def like_article():
    article_id = int(request.form['article_id'])
    article = get_article(article_id)
    liked_articles = session.setdefault('liked_articles', set())
    if article.id in liked_articles:
        article.like_count -= 1
        liked_articles.remove(article.id)
    else:
        article.like_count += 1
        liked_articles.add(article.id)
    save_article(article)
    return redirect(f'/article/{article.id}')


@app.route("/auth", methods=["POST"])
def authenticate():
    login = request.form["login"]
    password = request.form["password"]

    if aut_user(login, password):
        session["is_authenticated"] = True
        user = get_user(login)
        session["login"] = user.login
        session["password"] = user.password
        session["id"] = user.id
        return redirect('/articles')
    else:
        return f'''
                <html>
                    <head>
                        <title>Authenticate</title>
                    </head>
                        <body>
                            <h1 style="text-align: center;">Authenticate</h1>
                            <p>Invalid username or password!</p>
                            <form action="/auth" method="post">
                                Login:    <input type="text" name="login"/><br>
                                Password: <input type="text" name="password"/><br>
                                <input type="submit" value="Sign in">
                            </form>
                        </body>
                </html>
            '''


if __name__ == '__main__':
    app.run(port=8080, debug=True)
