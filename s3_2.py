import numpy as np
d=[]
N = int(input())
sqr = np.sqrt(N)
for i in range(2,int(sqr)):
	if N % i == 0:
		d.append(i)
print(d)	
