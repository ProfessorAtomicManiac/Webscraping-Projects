from flask import Flask, render_template, request
import pandas

app = Flask(__name__)

@app.route('/')
def homepage():
    df = pandas.read_csv('quoted.csv')
    return df.to_html()

@app.route('/search', methods=['GET', 'POST']) # Can handle get and post
def searchpage():
    df = pandas.read_csv('quoted.csv')
    if request.method == 'GET':
        return render_template('mySearch.html')
    elif request.method == 'POST':
        return render_template('mySearch.html')

if __name__ == '__main__':
    app.run(debug=True)
