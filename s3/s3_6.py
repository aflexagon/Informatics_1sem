import numpy as np
x = np.array(list(map(float,input().split())))
y = np.array(list(map(float,input().split())))

xsr = np.mean(x)
ysr = np.mean(y)

n = (x - xsr)*y
d = (x - xsr)**2
a = np.sum(n)/np.sum(d)
b = ysr - a*xsr

print(f'a={a},b={b}')
