n = int(input())
A = list(map(int, input().split()))
b = n*(n+1)//2 - sum(A)
print(b)
