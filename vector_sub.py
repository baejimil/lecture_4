class Vector2D :
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return '({}, {}, {})'.format(self.x , self.y, self.z) 

    def sub(self, other):
        return Vector2D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Vector2D(self.x * other.x, self.y * other.y, self.z * other.z)

v1 = Vector2D(10,20,30)
v2 = Vector2D(30,40,50)
v3 = v1.sub(v2)
v4 = v1 - v2 
v5 = v1 * v2
print(v5)
print(v4)
print(v3)
