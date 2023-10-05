import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

A,B,C = [], [], []
df = pd.read_csv('iris_data.csv')

X = list(map(float, list(df['PetalLengthCm'])))

for i in X:
	if i < 1.2:
		A.append(i)
	elif i >= 1.2 and i < 1.5:
		B.append(i)
	else:
		C.append(i)

fig = plt.figure(figsize = (16,9))
plt1 = fig.add_subplot(211)
plt2 = fig.add_subplot(212)

plt1.pie([len(A),len(B),len(C)], labels = ['<1.2cm','1,2< and <=1.5cm','>1.5cm'])

plt.show()		 
