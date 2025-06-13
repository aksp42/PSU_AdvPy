#In the following program we are using default and abc in place of self.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello! My name is " + self.name)

p1 = Person("Amrit", 36)
p1.myfunc()

#Program modifying mutable type attributes.
class Number:
    evens = []
    odds = []

    def __init__(self, num):
        self.num = num
        if num % 2 == 0:
            Number.evens.append(num)
        else:
            Number.odds.append(num)
N1 = Number(21)
N2 = Number(32)
N3 = Number(43)
N4 = Number(54)
N5 = Number(65)
print("Even Numbers are:", Number.evens)
print("Odd Numbers are:", Number.odds)