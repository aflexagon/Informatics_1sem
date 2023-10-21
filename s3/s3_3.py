a, b = list(map(int,input().split()))
def NOD (a, b):
        if a==0 or b==0:
                return(a+b)
        if a>b:
                return NOD(a-b, b)
        else:
                return NOD(a, b-a)
d = NOD(a,b)
for y in range (1,10000):
	x = int((d-b*y)/a)
	if x == int((d-b*y)/a):
		break
	else:
		y+=1
print(f'{x} {y} {d}')
