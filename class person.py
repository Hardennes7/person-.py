
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello! My name is {self.name}, I am {self.age} years old and my gender is a {self.gender}.")

# Create an instance of the Person class
person1 = Person("Hargreaves", 20, "male")

# Call the introduce method
person1.introduce()
