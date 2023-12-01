A = list(map(int, input().split()))
B = list(map(int, input().split()))
n = A[0]
k = A[1]
S=[]
j=0

for i in range(0,2**n):
    j = i ^ k
    S.append(B[i]+B[j])
print(max(S))
