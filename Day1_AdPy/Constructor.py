#Example of Default Constructor.
class Student:
    # Default Constructor
    def __init__(self):
        print("This is a default constructor")

    def show(self, name):
        print("Hello!", name)

student = Student()
student.show("Shivansh")

#Parameterised Constructor Example
class Addition:
    first = 0
    second = 0
    answer = 0

    def __init__(self, f, s):  # parameterized constructor
        self.first = f
        self.second = s

    def display(self):
        print("First number = ", self.first)
        print("Second number = ", self.second)
        print("Addition of two numbers = ", self.answer)

    def calculate(self):
        self.answer = self.first + self.second

obj = Addition(1000, 2000)
obj.calculate()
obj.display()

#More than One Constructor in Class
class Student:
    def __init__(self):
        print("The First Constructor")

    def __init__(self):
        print("The second Constructor")
st = Student()