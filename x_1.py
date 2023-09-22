x, y = list(map(int,input().split()))
def NOD (a, b):
	if a==0 or b==0:
		return(a+b)
	if a>b:
		return NOD(a-b, b)
	else:
		return NOD(a, b-a)
print(NOD(x,y))	
