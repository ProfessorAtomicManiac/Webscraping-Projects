from flask import Flask, render_template
import pandas

app = Flask(__name__)

@app.route('/')
def index():
    items = pandas.read_csv('quotes.csv')
    #quoteList = list(data.values) # convert .csv into a list
    return '<h1> Hi, here are the items:</h1> ' + items.to_html()

@app.route('/search')
def search():
    items = pandas.read_csv('quotes.csv')
    return render_template('index.html') + items.to_html()

if __name__ == '__main__':
    app.run(port = 5000, debug = True) # You can change ports
