m = 0
A = list(map(int,input().split()))

if len(A)%2!=0: m = 1

for i in range(0, len(A)-m, 2):
	A[i], A[i+1] = A[i+1], A[i]

print(*A)
