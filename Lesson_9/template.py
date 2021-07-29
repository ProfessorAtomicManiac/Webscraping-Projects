from flask import Flask, render_template
import pandas

app = Flask(__name__)

@app.route('/')
def index():
# Must create templates folder then put html file there
# Then no need to specify file path
    """return render_template('index.html',
                            message = 'This website is a sacrificial temple for the blood god')

    df = pandas.read_csv('quotes.csv')
    return df.to_html()"""

    data = pandas.read_csv('quotes.csv')
    quoteList = list(data.values) # convert .csv into a list
    return render_template('index.html',
                            message = 'This website is a sacrificial temple for the blood god',
                            quotes = quoteList)

if __name__ == '__main__':
    app.run(port = 5000, debug = True) # You can change ports
