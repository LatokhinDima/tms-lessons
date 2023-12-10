from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/ping')
def ping():
    return f'''
<html>
<head>
    <title>Ping-Pong</title>
</head>
<body>
    <strong><a href="/pong"">pong</a></strong>
</body>
</html>
'''


@app.route('/pong')
def pong():
    return f'''
<html>
<head>
    <title>Ping-Pong</title>
</head>
<body>
    <strong><a href="/ping"">ping</</a></strong>
</body>
</html>
'''


if __name__ == '__main__':
    app.run(port=8080, debug=True)
