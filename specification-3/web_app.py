from flask import Flask
from flask import render_template

app = Flask(__name__)
home_message= "Hello Team 48! This is the homepage to the web app."
spec_1_message= "In this challenge you are going to be exploring frequency analysis of large text files and producing" \
                " a visual way of presenting your analysis results. Write a program that takes a large text file and " \
                "perform a frequency analysis of the characters and words in that file. You should then present your " \
                "findings visually using the python 2D graph plotting library, Matplotlib."
spec_1_header="Specification 1:"
spec_2_message= "This is the Specification 2"
spec_2_header="Specification 2:"
spec_3_message= "This is the Specification 3"
spec_3_header="Specification 3:"
spec_4_message= "This is the Specification 4"
spec_4_header="Specification 4:"

@app.route('/')
def home():
    return render_template('index.html', title="Homepage", header="Home Page",  message= home_message)

@app.route('/page_1')
def page_1():
    return render_template('index.html', title="Specification 1 - ", message= spec_1_message)

@app.route('/page_2')
def page_2():
    return render_template('index.html', title="Specification 2 - ", message= spec_2_message)

@app.route('/page_3')
def page_3():
    return render_template('index.html', title="Specification 3 - ", message= spec_3_message)

@app.route('/page_4')
def page_4():
    return render_template('index.html', title="Specification 4 - ", message= spec_4_message)



if __name__ == '__main__':
    app.run()
