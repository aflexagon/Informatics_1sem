import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure(figsize = (16,9))
ax1 = fig.add_subplot(111)

x_measured = [62.32, 92.78, 127.64, 166.13, 170.39, 198.93, 225.22, 256.58, 299.64, 306.65,
             236.82, 230.17, 220.16, 212.33, 205.28, 197.43, 187.28, 174.92, 164.68, 155.14,
	     146.81, 140.92, 133.53, 125.86, 115.56, 111.72, 103.62, 91,87, 85.83, 82.72]

y_measured = [130, 195, 265, 345, 355, 415, 470, 535, 625, 640,
	     730, 710, 680, 655, 635, 610, 580, 540, 510, 480,
	     735, 705, 670, 630, 580, 560, 520, 460, 430, 415]

for i in range (0,3):
	x1 = x_measured[10*i:10*(i+1)]
	y1 = y_measured[10*i:10*(i+1)]
	x = np.array(x1)
	y = np.array(y1)

	x_mean = np.mean(x)
	y_mean = np.mean(y)

	numerator = (x - x_mean)*y
	denominator = (x - x_mean)**2
	k = np.sum(numerator)/np.sum(denominator)

	print(k)

	b = y_mean - k*x_mean

	print(b)

	plt.axline((0,b),(1,k+b))
	
	ax1.scatter(x1, y1, marker='x')
	
	ax1.errorbar(y1, x1, yerr=0.2, xerr = 0.1, color = 'k', linestyle = 'None')
#plt.ylim(50, 800)

ax1.grid() 
plt.xlabel('I,мА')
plt.ylabel('V, мВ')

plt.show()
