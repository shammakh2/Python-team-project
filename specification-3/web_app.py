from flask import Flask
from flask import render_template
"""
A brief description of what my code does and how it meets the requirement specification:
Lines 18-68 read the README and python files into python strings, removing new line character \n and replacing it with a different newline character
After this I defined 'routes' for each page. I inserted python variables into the HTML file.
I created index.html which is a template for each page.

My code meets requirement 1 because I installed and imported the Flask module
My code meets requirement 2 because I initially produced a homepage that linked to other pages which each display our code.
My code meets requirement 3 because I created a web page for each specification and presented our code on each.
My code meets requirement 4 because I have written this brief description.
"""
app = Flask(__name__)
home_message= "Hello Team 48! This is the homepage to the web app. This web app's purpose is to represent our teams work" \
              " in a web interface. You can navigate by clicking the hyperlinks at the top."

spec_1_header="Text Frequency Analyser"

global spec_1_message
spec_1_message=""
with open("../specification-1/README.md", "r") as file:
    for line in file:
        spec_1_message= spec_1_message.rstrip() + line.rstrip() + "&#10;" # &#10; is the line feed character similar to \n

global spec_1_python
spec_1_python=""
with open("../specification-1/ata.py", "r") as file:
    for line in file:
        spec_1_python= spec_1_python.rstrip() + line.rstrip()+ "&#10;"


spec_2_header= "Image Analyser"

global spec_2_message
spec_2_message=""
with open("../specification-2/README.md", "r") as file:
    for line in file:
        spec_2_message= spec_2_message.rstrip() + line.rstrip()+ "&#10;"

global spec_2_python
spec_2_python=""
with open("../specification-2/img_manip.py", "r") as file:
    for line in file:
        spec_2_python= spec_2_python.rstrip() + line.rstrip()+ "&#10;"

spec_3_header= "This Web Interface"

global spec_3_message
spec_3_message=""
with open("../specification-3/README.md", "r") as file:
    for line in file:
        spec_3_message= spec_3_message.rstrip() + line.rstrip()+ "&#10;"

global spec_3_python
spec_3_python=""
with open("../specification-3/web_app.py", "r") as file:
    for line in file:
        spec_3_python= spec_3_python.rstrip() + line.rstrip()+ "&#10;"

spec_4_header="Custom app"

global spec_4_message
spec_4_message=""
with open("../specification-4/README.md", "r") as file:
    for line in file:
        spec_4_message= spec_4_message.rstrip() + line.rstrip()+ "&#10;"

@app.route('/')
def home():
    #title, header, message and code are all variables. When FLask finds {{ title }} in the HTML it replaces it with the value passed here
    return render_template('index.html', title="Homepage", header="Home Page",  message= home_message, code= "")

@app.route('/page_1')
def page_1():
    return render_template('index.html', title="Specification 1",
                           header=spec_1_header, message= spec_1_message, code=spec_1_python)

@app.route('/page_2')
def page_2():
    return render_template('index.html', title="Specification 2",
                           header=spec_2_header, message= spec_2_message, code=spec_2_python)

@app.route('/page_3')
def page_3():
    return render_template('index.html', title="Specification 3",
                           header=spec_3_header, message= spec_3_message, code=spec_3_python)

@app.route('/page_4')
def page_4():
    return render_template('index.html', title="Specification 4",
                           header=spec_4_header, message= spec_4_message, code="")

if __name__ == '__main__':
    app.run()
