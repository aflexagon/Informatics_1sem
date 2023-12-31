import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


tmp = pd.read_csv('BTC_data.csv')

y = list(map(float, list(tmp["close"])))
x = list(tmp['time'])
for i in range(len(((tmp)))):
    x[i] = f'{x[i][8:10]} - {x[i][5:7]} - {x[i][:4]}'

fig = plt.figure()
ax1 = plt.subplot(111)
xtmp = list(range(len(y)))
ax1.plot(x, y, color = 'b')

ax1.grid()
plt.show()
