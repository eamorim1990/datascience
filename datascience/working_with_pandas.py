import numpy as np 
import pandas as pd 
from pandas import Series, DataFrame

obj = Series([3,6,9,12])


print(obj.values)
print(obj.index)

ww2_cas = Series([8700000,4300000,2100000,400000], index=['URSS','Germany','Japan','EUA'])
print(ww2_cas['EUA'])

print(ww2_cas[ww2_cas > 4000000])

print('URSS' in ww2_cas)

ww2_dict = ww2_cas.to_dict()
print(ww2_dict)

ww2_series = Series(ww2_dict)
print(ww2_series)

countries = ['China','Germany','Japan','EUA','URSS','Argentina']

obj2 = pd.Series(ww2_dict, index=countries)
print(obj2)

print(pd.isnull(obj2))
print(pd.notnull(obj2))

print(ww2_series+obj2)

obj2.name = 'Vítimas 2ª Guerra Mundial'
obj2.index.name= 'Países'

print(obj2)