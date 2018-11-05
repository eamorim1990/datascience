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