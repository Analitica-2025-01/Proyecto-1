import pandas as pd
# Cargar datos
file_path = 'df_william.csv'
df = pd.read_csv(file_path, encoding='cp1252', sep=',')


print(df['has_photo'].unique())




