# class Dog:
#     # name="rex"

#     def bark(self):
#         print(f"{self.name} says woof ")

#     def __init__(self,name):
#         self.name=name
# d=Dog("rex")
# print(d.name)
# d.bark()
# d=Dog("jimmy")
# d.bark()
# d1=Dog("jim")
# d1.bark()


# 1. Student Class
# Create a class Student with a method study() that prints:

# Student is studying

# Create an object and call the method.



# class student:
#     def study(self):
#         print("Student is studying")
# d=student()
# d.study()


# 2. Car Class
# Create a class Car with a method drive() that prints:
# Car is moving
# Create an object and call drive().

# class Car:
#     def drive(self):
#         print("Car is moving")
# c=Car()
# c.drive()

# class student:
#     name="Rahul"
#     def display(self):
#         print(f"{self.name} is studying")
# d=student()
# d.display()

# class dog:
#     name="Bobby"
#     def bark(self):
#         print(f"{self.name} is barking")
# d=dog()
# d.bark()

# class student:

#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print(f"Name:{self.name},Age:{self.age}")
# d=student("Anu","10")
# d.display()

# class car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
        
#     def display(self):
#         print(f"{self.brand},{self.model}")
# d=car("Toyota","Innova")
# d.display()

class student:
    def __init__(self,name):
          self.name=name
    def introduce(self):
        print("My name is",self.name)
s1=student("Anu")
s2=student("Rahul")
s1.introduce()
s2.introduce()