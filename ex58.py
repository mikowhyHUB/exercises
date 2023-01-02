'''
Create a Python class Person with attributes: name and age of type string.
Create a display() method that displays the name and age of an object created via the Person class.
Create a child class Student  which inherits from the Person class and which also has a section attribute.
Create a method displayStudent() that displays the name, age and section of an object created via the Student class.
Create a student object via an instantiation on the Student class and then test the displayStudent method.
'''


from unicodedata import name


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f'Person name:{self.name}, Person age:{self.age}')


class Student(Person):
    def __init__(self, name, age, section):
        Person.__init__(self, name, age)
        self.section = section

    def display_student(self):
        print(f'Name:{self.name}, Age:{self.age}, Section:{self.section}')


user_p = Person('Jacob', 22)
user_p.display()

user_s = Student('Alex', 19, 'Math')
user_s.display_student()
