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
	def __rsub__(self,other):
                if isinstance(other,Vector):
                        return Vector(self.x-other.x,self.y-other.y,self.z-other.z)
                elif isinstance(other, int) or isinstance(other, float):
                        return Vector(self.x-other, self.y-other, self.z-other)
	def __repr__(self):
		return f'x = {self.x} y = {self.y} z = {self.z}'
	def __mul__(self,other):
                if isinstance(other,Vector):
                        return Vector(self.x*other.x,self.y*other.y,self.z*other.z)
                elif isinstance(other, int) or isinstance(other, float):
                        return Vector(self.x*other, self.y*other, self.z*other)
v1 = Vector(1,2,3)
print(isinstance(v1,Vector))
print(v1.x-v1.y)
v2 = Vector(2,3,4)
v3 = 1 + v1
v4 = 1 - v1
R = v3 * v4
print(v3)
print(v4)
print(R)

