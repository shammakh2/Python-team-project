from flask import Flask
from flask import render_template

app = Flask(__name__)
home_message= "Hello Team 48! This is the homepage to the web app. This web app's purpose is to represent our teams work" \
              " in a web interface. You can navigate by clicking the hyperlinks at the top."

spec_1_header="Text Frequency Analyser"
spec_1_message= "In this challenge you are going to be exploring frequency analysis of large text files and producing" \
                " a visual way of presenting your analysis results. Write a program that takes a large text file and " \
                "perform a frequency analysis of the characters and words in that file. You should then present your " \
                "findings visually using the python 2D graph plotting library, Matplotlib."

spec_2_header= "Image Analyser"
spec_2_message= "In this challenge, you are going to be exploring image manipulation using the Pillow Python library. " \
                "Write a program that modifies a selection of images of various sizes and file formats and converts " \
                "them to JPEG thumbnails. Your program should allow the user to apply a selection of modifications to " \
                "an image and then store the modified image. To be able to modify images in this way, you will have to " \
                "make use of the Pillow Python library. This library is a fork of the Python Imaging Library (PIL), so" \
                " much of the existing functionality is still there, however, the library has been expanded further." \
                "After you completed the core features of the program, expand your program by experimenting with " \
                "different features of the Pillow library and showing your results. For example, you could manipulate " \
                "the specific RGB values of each pixel of an image. If applicable, make sure to discuss what features " \
                "you have experimented with in your individual report."

spec_3_header= "This Web Interface"
spec_3_message= "In this challenge you are going to build a web application using a Python-based web framework. Flask " \
                "is a common web framework that is easy to setup and allows extensibility. \nYou are going to build a " \
                "simple web application that presents the code written in the previous challenge specifications. " \
                "The purpose of the webpages is to present the code neatly with some brief documentation explaining " \
                "the purpose of the code. What you do here is entirely experimental and open for creativity, therefore" \
                " you can make use of any external libraries for the presentation of your code. However, be sure not to" \
                " 'feature creep'. \nThis challenge is about your ability to investigate a Python web framework library" \
                " and its applications rather than your HTML, CSS, and JavaScript abilities. I suggest looking through" \
                " my guide on creating a simple web application that uses HTML templates."

spec_4_header="Custom app"
spec_4_message= "In this challenge it is up to you to choose a Python library that hasn't been mentioned before in the " \
                "previous challenges and develop a software artefact around that library. The software artefact " \
                "should make use of some of the skills you have learned so far in CSC1031, CSC1032, CSC1033, and " \
                "CSC1034 so that it clearly displays your programming and theoretical abilities.\nThis challenge has " \
                "complete creative freedom. Meaning, you can build anything you like as long as it doesn't make use " \
                "of an aforementioned library in the previous challenges."

@app.route('/')
def home():
    return render_template('index.html', title="Homepage", header="Home Page",  message= home_message)

@app.route('/page_1')
def page_1():
    return render_template('index.html', title="Specification 1", header=spec_1_header, message= spec_1_message)

@app.route('/page_2')
def page_2():
    return render_template('index.html', title="Specification 2", header=spec_2_header, message= spec_2_message)

@app.route('/page_3')
def page_3():
    return render_template('index.html', title="Specification 3", header=spec_3_header, message= spec_3_message)

@app.route('/page_4')
def page_4():
    return render_template('index.html', title="Specification 4", header=spec_4_header, message= spec_4_message)



if __name__ == '__main__':
    app.run()
