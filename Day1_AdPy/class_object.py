#P1-Create class and object

class Greeting:
    message = "Hello, World!"

    def say_hello(self):
        print(self.message)

# Create an object
greet = Greeting()
greet.say_hello()