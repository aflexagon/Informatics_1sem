import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

A,B,C = [], [], []
df = pd.read_csv('iris_data.csv')

X = list(map(float, list(df['PetalLengthCm'])))
Y = list(map(str, list(df['Species'])))

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

A, B, C = [], [], []

a = 0
b = 0
c = 0
for i in Y:
	if  i == 'Iris-setosa':
		A.append(i)
		a+=1
	if i == 'Iris-versicolor':
		B.append(i)
		b+=1
	if i == 'Iris-virginica':
		C.append(i)
		c+=1
print(f'{a} {b} {c}')
plt2.pie([a,b,c], labels = ['Iris-setosa','Iris-versicolor','Iris-virginica'])

plt.show()

