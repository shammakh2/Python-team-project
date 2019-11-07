from flask import Flask, send_from_directory, make_response
from flask import render_template
import os.path

app = Flask(__name__)
home_message= "Hello Team 48! This is the homepage to the web app. This web app's purpose is to represent our teams work" \
              " in a web interface. You can navigate by clicking the hyperlinks at the top."

spec_1_header="Text Frequency Analyser"
global spec_1_message

spec_1_message=""
with open("../specification-1/README.md", "r") as file:
    for line in file:
        spec_1_message= spec_1_message.rstrip() + line.rstrip()

global spec_1_python
spec_1_python=""
with open("../specification-1/ata.py", "r") as file:
    for line in file:
        spec_1_python= spec_1_python.rstrip() + line.rstrip()


spec_2_header= "Image Analyser"

global spec_2_message
spec_2_message=""
with open("../specification-2/README.md", "r") as file:
    for line in file:
        spec_2_message= spec_2_message.rstrip() + line.rstrip()


spec_3_header= "This Web Interface"

global spec_3_message
spec_3_message=""
with open("../specification-3/README.md", "r") as file:
    for line in file:
        spec_3_message= spec_3_message.rstrip() + line.rstrip()

spec_4_header="Custom app"

global spec_4_message
spec_4_message=""
with open("../specification-4/README.md", "r") as file:
    for line in file:
        spec_4_message= spec_4_message.rstrip() + line.rstrip()

@app.route('/')
def home():
    return render_template('index.html', title="Homepage", header="Home Page",  message= home_message, code= spec_1_python)

@app.route('/page_1')
def page_1():
    return render_template('index.html', title="Specification 1", header=spec_1_header, message= spec_1_message, code="")

@app.route('/page_2')
def page_2():
    return render_template('index.html', title="Specification 2", header=spec_2_header, message= spec_2_message, code="")

@app.route('/page_3')
def page_3():
    return render_template('index.html', title="Specification 3", header=spec_3_header, message= spec_3_message, code="")

@app.route('/page_4')
def page_4():
    return render_template('index.html', title="Specification 4", header=spec_4_header, message= spec_4_message, code="")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
