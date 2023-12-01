A = list(map(int, input().split()))
n = A[0]
m = A[1]
center = 0

while m > 0 and n > 0:
    if (n+1) % 2 == 0 and (m+1) % 2 == 0:
        center += 1
    n = (n-1)/2
    m = (m-1)/2

k = int((4**center-1)/3)
print(k)
