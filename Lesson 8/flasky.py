from flask import Flask
import pandas

"""
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run()

"""
# Must be run on cmd, not IDLE. Also type "localhost:5000" to
# access the website

app = Flask(__name__)
# The two underlines are for reserved variables/functions

@app.route('/')
# Nothing after the url
def hello_world():
    return "Hello BRUH <style> html{background-color: powderblue; font-size: 50px}</style>"

@app.route('/items')
# items after the url
def showItems():
    items = pandas.read_csv(
        'C:\\Users\\djxgh\\Desktop\\Web Crawler\\Lesson 8\\craig.csv')
    return '<h1> Hi, here are the items:</h1> ' + items.to_html()

@app.route('/bruh')
def Zou():
    # Typically an html file isn't inputed in the code, instead it uses a "template"
    return """<!DOCTYPE html>
<html>
    <head>
        <title>
            CS and Programming
        </title>
        <link rel="stylesheet" type="text/css" href="style.css" />
    </head>
    <body>

        <div class="header">
            <h1>Welcome to Computer Science and Programming Class</h1>
        </div>

        <div class="container">

             <div class="textbooks">
                <p>Textbooks</p>

                <ol>
                    <li><a href="http://greenteapress.com/thinkjava6/thinkjava.pdf"> Book 1: Think Java -- How to think like a computer scientist (6.1.3 version)</a> By Allen B. Downey and Chris Mayfield.</li>
                    <ul>
                        <li>You can also visit: <a href="https://books.trinket.io/thinkjava/">Think Java Online Interactive Version</a></li>
                        <li><a href="https://github.com/AllenDowney/ThinkJavaCode">Example codes of the book</a></li>
                    </ul>
                    <li><a href="https://kulslide.com/download/java-software-solutions-foundations-of-program-design-eighth-edition-_59ff7a25d64ab2f1053a5fda_pdf">Book 2: Java Software Solutions: Foundations of program design (8th edition)</a> By John Lewis and William Loftus.</li>
                </ol>
            </div>

            <div class="computer">
                <p>AP Computer Science A</p>
                <ol>
                    <li><a href="https://cs.iupui.edu/~xzou/ProgAtCarmel/CommonDocuments/ap-computer-science-a-course-and-exam-description.pdf">AP Computer Science A: course and exam description</a></li>
                    <li><a href="https://cs.iupui.edu/~xzou/ProgAtCarmel/CommonDocuments/ThinkJava-Vs-AP-CSA.pdf">Correspondence between Think Java and AP Computer Science A</a></li>
                </ol>
            </div>

            <div class="lectures">
                <p>Lectures</p>
                <table>
                    <thead>
                        <tr>
                            <th>Lectures</th>
                            <th>Date</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td colspawn="5">
                                <a href="Chapter1.pptx">Chapter 1: Introduction -- The way of the program</a>
                            </td>
                            <td>April 4th, 2020</td>
                        </tr>

                    </tbody>
                </table>
            </div>

            <div class="assignments">
                <p>Assignments</p>
                    <ol>
                        <li>Install Java IDE if not yet. If possible, play with the installed IDE by writing and running your first program called "Hello World!".</li>
                        <br>
                        <li>Read the textbook from beginning and until page 6. If possible, submit (at least) one question/concept/term that you do not understand when you read the textbook (via email).</li>
                    </ol>
            </div>

            <div class="resources">
                <p>Resources</p>
                <ol>
                    <li>Online programming platforms:</li>
                    <ul>
                        <li><a href="jdoodle.com">jdoodle.com</a></li>
                        <li><a href="compilejava.net">compilejava.net</a></li>
                        <li><a href="tutorialspoint.com">tutorialspoint.com</a></li>
                        <li><a href="coderbyte.com">coderbyte.com</a></li>
                    </ul>
                    <li>There are three popular Java Integrated Devlopment Environments (JDE). You should download and install on JDE (anyone):</li>
                    <ul>
                        <li>NetBeans <a href="../Install-NetBeans-IDE.docx">How to install NetBeans</a></li>
                        <li>Eclipse</li>
                        <li>IntelliJ</li>
                    </ul>
                    <li>In addition, In Appendix A of Book 1, it presents DrJava</li>
                </ol>
            </div>

        </div>
    </body>
</html>"""
if __name__ == '__main__':
    app.run()
