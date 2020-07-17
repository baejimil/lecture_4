class Circle:
    def __init__(self, name, radius, PI):
        self.name = name
        self.radius = radius
        self.PI = PI

    def area(self):
        return self.PI * self.radius **2

c1 = Circle("c1", 4 , 3.14)
print('c1의 면적:', c1.area())
c2 = Circle("c1", 6 , 3.141)
print('c2의 면적:', c2.area())
c3 = Circle("c1", 5 , 3.1415)
print('c3의 면적:', c3.area())

print(c1.__dict__)