def tri(N,x):
	x = o
	for i in range(1,N):
		print(f'{x}'*i)
	for i in range(N,0,-1):
		print(f'{x}'*i)

N,o = input().split()

tri(int(N),o)
