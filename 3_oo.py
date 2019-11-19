class Person:

    def __init__(self, n, h, w):
        self.name = n
        self.height = h
        self.weight = w

    def getbmi(self):
        return self.weight / (self.height / 100) ** 2

    def __str__(self):
        return self.name

    def __repr__(self):
        return "/" + self.name + "/"

    def __int__(self):
        return 0

class Student(Person):

    def __init__(self, n, h, w, a):
        Person.__init__(self, n, h, w)
        self.age = a

    def __int__(self):
        return self.age

p1 = Person("Elwing", 175, 75)
print(p1.getbmi())
print(p1)
p2 = Person("Bob", 180, 80)
print(p2.getbmi())
print([p1, p2])
print(int(p1))
s1 = Student("Carol", 170, 50, 25)
print(int(s1))
print(s1)