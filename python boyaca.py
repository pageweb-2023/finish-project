import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
'''

'''

boyaca = pd.read_csv('boyaca.csv')

df2 = pd.DataFrame(boyaca)
print(df2.head())
filtered_df = df2[df2['label_region']
.isin(['Almeida','Aquitania','Belén','Duitama','Iza','Sogamoso','Tunja','Fira','Cuitiva','El Cocuy'])]


sns.pairplot(data= df2,
             hue='indicador',)

plt.plot(filtered_df['count'],
         filtered_df['label_region'],)


sns.catplot(data=filtered_df,
            x='label_region',
            y='count',
            kind='bar',
            )
plt.xticks(rotation=90)


plt.savefig('static/imgGraficas/BIODIVERSIDAD EN DIFERENTES1.jpg')

plt.show()