A = list(map(int, input().split()))
a = A[0]
b = A[1]
flag = 0
x = 0
while flag != 1:
    if (a + x)%b == 0 and (b + x)%a == 0:
        print(x)
        flag = 1
    x += 1


