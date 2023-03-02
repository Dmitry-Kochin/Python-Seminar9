import pandas as pd
df=pd.read_csv('california_housing_train.csv')
print(df.head())
min_population = df.population.min()
print(df[
    df['population'] == min_population
].households.max())