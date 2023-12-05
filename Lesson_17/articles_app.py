import sqlite3
from dataclasses import dataclass

from flask import Flask, abort

DATABASE_FILE = 'sqlite.db'

app = Flask(__name__)


@dataclass
class Article:
    id: int
    title: str
    text: str
    author: str


def get_all_articles() -> list[Article]:
    with sqlite3.connect(DATABASE_FILE) as connection:
        execution_result = connection.execute(
            'SELECT id, title, text, author FROM article')
        return [Article(*values) for values in execution_result.fetchall()]


def get_article(article_id: int) -> Article:
    with sqlite3.connect(DATABASE_FILE) as connection:
        execution_result = connection.execute('SELECT id, title, text, author '
                                              'FROM article '
                                              'WHERE id = ?', (article_id,))
        rows = execution_result.fetchall()
        if len(rows) != 1:
            raise ValueError(f'Expected 1 object with id {article_id}, got {len(rows)}')
        return Article(*rows[0])


def save_article(article: Article):
    with sqlite3.connect(DATABASE_FILE) as connection:
        data = (article.title, article.text, article.author, article.id)
        connection.execute('UPDATE article '
                           'SET title = ?, text = ?, author = ? '
                           'WHERE id = ?', data)


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
            <h4>{article.text}</h4
        </body>
    </html>
    '''



if __name__ == '__main__':
    app.run(port=8080, debug=True)
