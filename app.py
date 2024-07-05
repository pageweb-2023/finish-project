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

@app.route('/otros')
def otros():
    return render_template('OTROS.html')

proyect = pd.read_csv('aves.csv')

df = pd.DataFrame(proyect)

print(df.head())

sns.pairplot(data=df,
            hue='indicador')
sns.catplot(data=df,
            x='slug_region',
            y='count',
            )

plt.grid(True)

plt.xticks(rotation=90)

plt.title('aves en el pais')




