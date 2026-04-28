import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Carregando os dados que geraamos no passo anterior
df = pd.read_csv('tax_data.csv')

#Visualizar as primeiras 5 linhas para garantir que tudo subiu certo
print(df.head())

#Resumo estatística das colunas numéricas
print(df.describe())

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='invoice_value', y='calculated_icms', alpha=0.5)
plt.title('Invoice Values vs ICMS Tax')
plt.show()