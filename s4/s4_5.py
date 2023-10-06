import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


tab = pd.read_csv('BTC_data.csv')

y = list(map(float, list(tab["close"])))
x = list(tab['time'])
for i in range(len(((tab)))):
    x[i] = f'{x[i][8:10]} - {x[i][5:7]} - {x[i][:4]}'
    print(x[i])
fig = plt.figure()
ax1 = plt.subplot(111)
xtab = list(range(len(y)))
ax1.plot(x, y, color = 'b')

ax1.grid()
plt.show()
