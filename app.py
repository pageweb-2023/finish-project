import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/redirect')
def redirect():
    return redirect(url_for('index.html'))

@app.route('/boyaca')
def boyaca():

    return render_template('BOYACA.html')

@app.route('/cundinamarca')
def cundinamarca():
    return render_template('CUNDINAMARCA.html')

@app.route('/aves')
def aves():
    return render_template('AVES.html')





