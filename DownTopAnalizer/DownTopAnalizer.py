from flask import Flask
from DownTopAnalizer.Analyzer import create_table

app = Flask(__name__)

@app.route('/')
def hello_world():
    table = create_table()

    return 'Hello World!'


if __name__ == '__main__':
    app.run()
