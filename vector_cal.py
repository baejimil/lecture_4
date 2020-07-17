class Vector2D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add(self, other):
        return Vector2D(self.x + other.x, self.y + other.y,self.z + other.z)

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y,self.z + other.z)

    def eq(self, other):
        return Vector2D(self.x == other.x, self.y == other.y, self.z == other.z)
    def __eq__(self, other):
        return Vector2D(self.x == other.x, self.y == other.y, self.z == other.z)

    def __str__(self):
        return '({}, {}, {})'.format(self.x , self.y, self.z) 

    def sub(self, other):
        return Vector2D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Vector2D(self.x * other.x, self.y * other.y, self.z * other.z)
