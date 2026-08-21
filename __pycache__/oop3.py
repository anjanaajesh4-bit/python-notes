# class Dog:
#     def speak(self):
#               print("Woof")
# class Cat:
#        def speak(self):
#               print("Meow")
# animals=[Dog(),Cat()]
# for a in animals:
#        a.speak()

# class Car:
#     def move(self):
#         print("car is moving")
# class Boat:
#     def move(self):
#         print("Boat is sailing")
# class Plane:
#    def move(self):
#        print("plane is flying")
# vehicles=[Car(),Boat(),Plane()]
# for v in vehicles:
#     v.move() 

# class File:
#     def read(self):
#         print("Reading file")
# class Socket:
#     def read(self):
#         print("Reading Socket")
# def fetch_data(source):
#     source.read()
# fetch_data(File())
# fetch_data(Socket())

# class Point:
#     def __init__(self,x):
#         self.x=x
#     def __add__(self,other):
#         return self.x + other.x
# p1=Point(10)
# p2=Point(20)
# print(p1+p2)

# class Student:
#     def __init__(self):
#         self.mark = 0
#     @property
#     def marks(self):
#         return self._marks
#     @marks.setter
#     def marks(self,value):
#         if value < 0:
#             print("Invalid marks")
#         else:
#             self._marks=value
# s=Student()
# s.marks = 80
# print(s.marks)


# class Student:
#     def __init__(self):
#         self.__marks = 80
#     def show_marks(self):
#         print(self.__marks)
# s=Student()
# s.show_marks()

class Student:
    def __init__(self):
        self.__marks = 80
    def get_marks(self):
        return self.__marks
    def set_marks(self,value):
        self.__marks=value
s=Student()
print(s.get_marks())
s.set_marks(100)
print(s.get_marks())