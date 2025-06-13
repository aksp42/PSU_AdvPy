# Class and Instance Variable
#P3
class Car:
    wheel = 4  # <- Class variable
    def __init__(self, name):
        self.name = name  # <- Instance variable
mercedes = Car("mercedes")
print(mercedes.wheel)  # Access of class variable through object
print(Car.wheel)  # Access of class variable through class
print(mercedes.name)  # Access of instance variable through object

#P4
'''Create a class name Employee with
i. a class variable office_name, and
ii. instance variables name and designation.
iii. Create a show_detail() method.
Difference'''
class Employee:
    office_name = "ABC Corporation"  # Class variable

    def __init__(self, name, designation):
        self.name = name
        self.designation = designation

    def show_details(self):
        print(f"Company Name: {Employee.office_name}\n Name: {self.name} \n Designation: {self.designation}")

emp1 = Employee("Mohit", 35)
emp1.show_details()
