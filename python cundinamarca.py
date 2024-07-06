import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

cundi = pd.read_csv('CUNDINAMARCA.csv')

df3 = pd.DataFrame(cundi)
print(df3.head())

filtrado = df3[df3['label_region'].isin(['Agua de Dios',
                                  'Albán','Bojacá',
                                  'Cajicá','Carmen de Carupa','Chía','Sibaté','Soacha',
                                  'subachoque','Susa','Tocancipá','Zipaquirá','Yacopí','viota','villapinzon','vergara',
                                  'tocaima','pacho','madrid','silvania'])]

sns.pairplot(data= df3,
             hue='indicador',)
plt.plot(filtrado['count'],
         filtrado['label_region'],)
sns.catplot(data=filtrado,
              x='label_region',
              y='count',
              kind='bar',
              )
plt.xticks(rotation=90)

plt.savefig('static/imgGraficas/biocund2')
plt.show()