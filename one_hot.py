import random
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

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

