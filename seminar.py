import random
import pandas as pd
import csv
import matplotlib.pyplot as plt

from pandas import read_csv
from seaborn import scatterplot, relplot, histplot,load_dataset, PairGrid, heatmap
from matplotlib.pyplot import show
from sklearn.preprocessing import OneHotEncoder
from os.path import exists


data1 = read_csv('california_housing_test.csv')
# scatterplot(data1, x = 'households', y = 'population')

# relplot(data1, x = 'median_house_value', y = 'longitude', kind='line')

# histplot(data1, x = 'housing_median_age')

# histplot(data1, x = 'median_house_value', hue='housing_median_age')
# show()


# penguins = load_dataset('penguins')
# scatterplot(penguins, x ='flipper_length_mm', y = 'body_mass_g', hue='sex', size='island', style='island')
# pg = PairGrid(penguins, x_vars=["body_mass_g", "bill_length_mm", "bill_depth_mm","flipper_length_mm"], y_vars=["sex"], hue='species')
# pg.map(scatterplot)
# show()
# penguins = penguins.pivot_table(columns='island', values='body_mass_g', index='species')
# heatmap(penguins)
# plt.xlabel('остров', size = 14)
# plt.ylabel('вид пигвина', size = 14)
# penguins['bill_depth_mm'].hist(bins=10)
# show()

# Для кодировки категориальных данных можно использовать метод pandas get_dummies
# pd.get_dummies(df['Type 1'])

# data = read_csv('penguins.csv')
# data.loc[data['bill_length_mm'] < 35, 'heigth_group'] = 'low'
# data.loc[(data['bill_length_mm'] >=35) & (data['bill_length_mm'] <= 42 ), 'heigth_group'] = 'medium'
# data.loc[data['bill_length_mm'] > 42, 'heigth_group'] = 'high'
# print(data)
# data.to_csv('penguins.csv', index=False)


lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
print(data)
data = pd.DataFrame({'whoAmI':lst})
# Создаем экземпляр класса OneHotEncoder
onehotencoder = OneHotEncoder()
data_new = onehotencoder.fit_transform(data.values)
print(pd.DataFrame(data_new.toarray(), columns=onehotencoder.categories_))

