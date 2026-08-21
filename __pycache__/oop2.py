# class student:
#     name="anjana"
# s=student()
# print(s.name)

# class example:
#     __private = 3
# e= example()
# # print(e.__private)
# print(e._example__private)

#name mangling-python changes __private to _example__private


# class account:
#     _balance = 1000
# class savingsaccount(account):
#     def show_balance(self):
#         print(self._balance)
# acc = savingsaccount()
# acc.show_balance()
# print(acc._balance)

# #Single Inheritance
# class animal:
#     def speak(self):
#         print("animal makes a sound")
# class dog(animal):
#     def bark(self):
#         print("dog barks")
# d=dog()
# d.speak()
# d.bark()

# #Multilevel Inheritance
# class Animal:
#     def speak(self):
#         print("Animal makes a sound")
# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")
# class Puppy(Dog):
#     def cry(self):
#         print("Puppy cries")
# p=Puppy()
# p.speak()
# p.bark()
# p.cry()

# #Hierarchical Inheritance
# class Animal:
#     def speak(self):
#         print("animal makes a sound")
# class Cat(Animal):
#     def meow(self):
#         print("cat meows")
# class dog(Animal):
#     def bark(self):
#         print("dog barks")
# c=Cat()
# d=dog()
# c.speak()
# c.meow()
# d.bark()

# #multiple Inheritance
# class Father:
#     def driving(self):
#         print("Ftaher can drive")
# class Mother:
#     def cooking(self):
#         print("Mother can cook")
# class Child(Father,Mother):
#     pass
# f=Child()
# f.cooking()
# f.driving()


# class Animal:
#     def speak(self):
#         print("Animal sound")
# class Dog(Animal):
#     def speak(self):
#         super().speak()
#         print("Woof")
# d=Dog()
# d.speak()

# class BankAccount:
#     account_holder="Anjana"
#     _balance=10000
#     __pin=1234
# d=BankAccount()
# print(d.account_holder)
# print(d._balance)
# print(d._BankAccount__pin)

class Person():
    name="Rex"
    age=21
class Teacher(Person):
    subject="maths"
t=Teacher()
print(t.subject)
print(t.name)
print(t.age)