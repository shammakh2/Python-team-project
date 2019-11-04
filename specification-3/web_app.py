from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def page_1():
    return render_template('index.html', title="Homepage", message="Hello team 48, this is page 1!")

@app.route('/page_2')
def page_2():
    return render_template('index.html', title="Page 2", message= "Hello team 48, this is page 2!")



if __name__ == '__main__':
    app.run()
