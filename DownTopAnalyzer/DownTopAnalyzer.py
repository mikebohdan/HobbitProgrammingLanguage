from flask import Flask, render_template
from Analyzer import create_table
import Analyzer.common

app = Flask(__name__)


@app.route('/')
def hello_world():
    table = create_table()
    return render_template('table_template.html', table=table, alphabet=Analyzer.common.init())


if __name__ == '__main__':
    app.run(debug=True)
