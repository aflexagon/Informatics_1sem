A = list(map(int,input().split()))
for i in range(len(A)-1):
	A[i], A[i+1] = A[i+1], A[i]
	if A[i] == A[len(A)-1]:
		A[i] == A[0]
print(*A)
