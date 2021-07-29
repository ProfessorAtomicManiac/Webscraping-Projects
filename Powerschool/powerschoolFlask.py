from flask import Flask, render_template
import pandas

app = Flask(__name__)

@app.route('/pg1')
def pg_1():
    items = pandas.read_csv('students1.csv')
    return render_template('index.html', page = "1") + items.to_html()

@app.route('/pg2')
def pg_2():
    items = pandas.read_csv('students2.csv')
    return render_template('index.html', page = "2") + items.to_html()

@app.route('/pg3')
def pg_3():
    items = pandas.read_csv('students3.csv')
    return render_template('index.html', page = "3") + items.to_html()

if __name__ == '__main__':
    app.run(port = 5000, debug = True) # You can change ports
