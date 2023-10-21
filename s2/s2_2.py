A = []
B = []
s = input().split()
G = int(s[0])
st = s[1]
L = len(st)
n = L//G
for i in range(n):
	A.append(st[i*G:(i+1)*G])
for k in range(len(A)):
	B.append(A[k][::-1])
R = ''.join(B)
print(R)
