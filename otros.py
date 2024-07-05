import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
plt.show()