import pandas as pd
from pandas import read_csv

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import seaborn as sns
import numpy as np

data = pd.read_csv('C:/Users/Park Subin/Desktop/gitproj-main/bitt.csv', encoding='cp949')
data_x1 = data.loc[:,"고가"]
data_x2 = np.array(data.loc[:,'저가'])
a = data_x1.tolist()
b = data_x2.tolist()
print(a)
print(b)

x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
y1=a
y2=b
plt.figure(figsize=(30, 30))
plt.plot(x,y1,y2,'g')
plt.xlabel('date')
plt.ylabel('price')
plt.title('Bitcoin Comparison')
plt.show()