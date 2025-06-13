#In the following program we are altering the __str__() method.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):  # This will get called when we print the object
        return f"The name is {self.name} and age is {self.age}"

p = Person("Amit", 35)
print(p)

#Instance Method Example
class Employee:
    # __init__ method to initialize the object attributes
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    # Instance method to display employee details
    def display_details(self):
        print(f"Employee Details:\nName: {self.name}\nPosition: {self.position}\nSalary: {self.salary}")

    # Instance method to give a raise to the employee
    def give_raise(self, amount):
        self.salary += amount
        print(f"{self.name} received a raise of {amount}. New salary is {self.salary}")

    # Instance method to update the employee's position
    def update_position(self, new_position):
        self.position = new_position
        print(f"{self.name}'s new position is {self.position}")
        # Creating an instance of Employee
employee_1 = Employee("Alice", "Software Engineer", 70000)
# Displaying employee details using an instance method
employee_1.display_details()
# Giving a raise to the employee using an instance method
employee_1.give_raise(5000)
# Updating the employee's position using an instance method
employee_1.update_position("Senior Software Engineer")
# Displaying updated employee details
employee_1.display_details()

#Write a program to count how many objects of a class are created.
class Student:
    counter = 0

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        Student.counter = Student.counter + 1

    def msg(self):
        print("Hello " + self.name + " you got ", self.marks, "% marks")

    @classmethod
    def object_count(cls):
        return cls.counter

s1 = Student("Abhishek", 65)
s2 = Student("Amit", 89)
print(Student.object_count())
print(s1.object_count())

#Static Method Example
class MathOperations:
    @staticmethod
    def add_numbers(a, b):
        return a + b

    @staticmethod
    def subtract_numbers(a, b):
        return a - b

obj = MathOperations()
result_add = MathOperations.add_numbers(10, 5) #called by className
result_subtract = obj.subtract_numbers(10, 5) #called by objectName

print(f"Addition: {result_add}")
print(f"Subtraction: {result_subtract}")