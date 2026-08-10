#def total(*numbers):
#   result = 0
#    for n in numbers:
#       result += n
#   return result 
#print(total(10,20))
#print(total(10,20,30,40))


# **kwargs
#def Student_info(**data):
#    for key,value in data.items():
#        print(key,':',value)
#Student_info(name="Ravi",age=18,marks=85)

#def demo(*args,**kwargs):
#A    print(args)
 #   print(kwargs)
#demo(10,20,name="achu",age=25)

#def show():
#    x=10
#    print(x)
#show()
 
#x = 10
#def show():
#     print(x)
#show()
#print(x)


#num=int(input("enter the number:"))
#def factorial(n):
#    if n==1 or n==0:
#        return 1
#    else:
#        return n*factorial(n-1)
#print("Factorail of",num,"is  =",factorial(num))


#num=int(input("enter the 1st number:"))
#num2=int(input("enter the 2nd number:"))
#print("the sum is :",num+num2)

#x="10"
#print(type(x))
#print(isinstance(x,float))
#print(id(x))

#age=20
#has_id=True
#if age>18 and has_id:
#    print("elligible to vote")

#day="sunday"
#if day=="sunday" or day=="saturday":
#    print("its a weekend")

#age=20
#has_id=True
#is_banned=False
#if age>18 and has_id:
#    print("You can vote")
#if age<18 or not has_id:
#    print("you are not elligible")
#if not is_banned:
#    print("you are not allowed to enter")

#membership operator
#products=["laptop","mobile","tab"]
#if "laptop" in products:
#    print("available")
#else:
#    print("not available")

#identity operator
#x=[10,20]
#y=[10,20]
#print(x is  y )

#available_balance=500
#credit=int(input("Enter the amount you want to add to uour account:"))
#new_balance=available_balance+credit
#print("your current balance is",new_balance)

#password="key"
#new_password=input("Enter your new password:")
#if password == new_password:
#    print("password match")
#else:
#    print("no match")

#for i in range(1,11):
#    print(i)

#for i in range(5):
#    print("Hello!")

#fruits=["banana","mango","orange"]
#for fruit in fruits:
#    print(fruit)

#for i in range(2,11,3):
#    print(i)

#num=int(input("enter the number:"))
#for i in range(1,11):
#   print(i,"*",num ," = " ,i*num)

#for i in range(5,0,-1):
#    print(i)

#for i in range(3):
#    for j in range(2):
#        print(i,j)

#i=1
#while i<=5:
#    print(i)
#    i+=1

#for i in range(3):
#    print(i)
#else:
#    print("completed")

#for i in range(5):
#    if i==3:
#        break
#    print(i)
#else:
#    print("completed")

#def welcome():
#    password="key"
#    new_password=input("Enter your new password:")
#    if password == new_password:
#        print("password match")
#    else:
#        print("no match")
#welcome()

#def hey(name):
#    print("My name is "+name)
#hey("Anjana")
# num=int(input("enter your number:"))
# sum=0
# sum+=num
# if sum==0:
#     # break

# print("sum =",sum)
