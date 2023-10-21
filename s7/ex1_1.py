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
                return Vector(self.x*other,self.y*other,self.z*other)
        elif isinstance(other, int) or isinstance(other, float):
                return Vector(self.x*other, self.y*other, self.z*other)
class Dot:
    def __init__(self,m,Vector):


