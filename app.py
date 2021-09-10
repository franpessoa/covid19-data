from flask import Flask, render_template
from covidapi_py import getdata

app = Flask('')

headings = ('Nome', 'Casos', 'Mortes', 'Mortes/Casos')
data = getdata()

@app.route('/')
def home():
    return render_template('table.html', headings=headings, data=data)
