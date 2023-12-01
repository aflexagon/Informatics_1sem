class Vector:
	def __init__(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z
	def __abs__(self):
		return(self.x**2 + self.y**2 + self.z**2)**0,5
	def __radd__(self,other):
		if isinstance(other,Vector):
			return Vector(self.x+other.x,self.y+other.y,self.z+other.z)
		elif isinstance(other,int) or isinstance(other, float):
			return Vector(self.x+other,self.y+other,self.z+other)
A = list(map(int, input().split()))
B = []
for  i in range(1,i//3):
	B.append(Vector(A[i],A[i+1],A[i+2]))
for i in range(1,len(B)):
	print(isinstance(B[i],Vector))
