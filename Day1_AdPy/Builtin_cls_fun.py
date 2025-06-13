#Built-in Class Functions
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an instance of Person
person = Person("Alice", 30)

# Use getattr to get the value of an attribute
name = getattr(person, "name")
print(f"Name: {name}") # Output: Name: Alice

# Use setattr to set the value of an attribute
setattr(person, "age", 31)
print(f"Updated Age: {person.age}") # Output: Updated Age: 31

# Use hasattr to check if an attribute exists
has_name = hasattr(person, "name")
print(f"Has attribute 'name': {has_name}") # Output: Has attribute 'name': True

# Use delattr to delete an attribute
delattr(person, "age")

# Check if the attribute 'age' still exists after deletion
has_age = hasattr(person, "age")
print(f"Has attribute 'age' after deletion: {has_age}")
# Output: Has attribute 'age' after deletion: False