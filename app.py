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
    boyaca = pd.read_csv('boyaca.csv')

    df2 = pd.DataFrame(boyaca)
    print(df2.head())
    filtered_df = df2[df2['label_region']
    .isin(['Almeida', 'Aquitania', 'Belén', 'Duitama', 'Iza', 'Sogamoso', 'Tunja', 'Fira', 'Cuitiva', 'El Cocuy'])]

    sns.pairplot(data=df2,
                 hue='indicador', )

    plt.plot(filtered_df['count'],
             filtered_df['label_region'], )

    sns.catplot(data=filtered_df,
                x='label_region',
                y='count',
                kind='bar',
                )
    plt.xticks(rotation=90)

    plt.savefig('static/imgGraficas/BIODIVERSIDAD EN DIFERENTES1.jpg')

    return render_template('BOYACA.html')

@app.route('/cundinamarca')
def cundinamarca():
    cundi = pd.read_csv('CUNDINAMARCA.csv')

    df3 = pd.DataFrame(cundi)
    print(df3.head())

    filtrado = df3[df3['label_region'].isin(['Agua de Dios',
                                             'Albán', 'Bojacá',
                                             'Cajicá', 'Carmen de Carupa', 'Chía', 'Sibaté', 'Soacha',
                                             'subachoque', 'Susa', 'Tocancipá', 'Zipaquirá', 'Yacopí', 'viota',
                                             'villapinzon', 'vergara',
                                             'tocaima', 'pacho', 'madrid', 'silvania'])]

    sns.pairplot(data=df3,
                 hue='indicador', )
    plt.plot(filtrado['count'],
             filtrado['label_region'], )
    sns.catplot(data=filtrado,
                x='label_region',
                y='count',
                kind='bar',
                )
    plt.xticks(rotation=90)

    plt.savefig('static/imgGraficas/biocun2')
    return render_template('CUNDINAMARCA.html')

@app.route('/aves')
def aves():
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
    plt.savefig('static/imgGraficas/aves2.jpg')

    return render_template('AVES.html')





