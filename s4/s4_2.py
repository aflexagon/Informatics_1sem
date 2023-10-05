import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure(figsize = (16,9))
ax2 = fig.add_subplot(211)
ax1 = fig.add_subplot(212)

values1 = np.random.normal(0, 10, 10000000)
values2 = np.random.normal(0, 10, 10000) 
ax1.hist(values1, 1000)
ax1.grid()

x = [i for i in range(50)]
y = [j for j in range(50)]


ax2.hist(values2, 1000)
ax2.grid()

plt.show()
