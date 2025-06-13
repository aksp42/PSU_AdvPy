#P2-Create a class named person with some attributes and properties.

class Person:
    def __init__(self, name, age, gender):  # __init__ is constructors.
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print('The name is {}, age is {} and gender is {}'.format(self.name, self.age, self.gender))

# Create an object of Person class
p1 = Person('Aditya', 28, 'Male')
p1.show_details()