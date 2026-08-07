#side=5
#area=side**2
#print("area of square=",area)

#balance=500
#amount_added=200
#balance += amount_added
#print("current_balance=",balance)

#game_points=100
#gains = 50
#loses =20
#game_points += gains
#game_points -= loses
#print("final_points =",game_points) 

#student_score=65
#pass_mark=40
#if(student_score>=pass_mark):
#    print("passed")
#else:
#    print("failed")

#password="Key"
#newpassword=input("enter the new password:")
#if newpassword == password:
 #   print("match found")
#else
#    print("no match found")

#stock_availability=int(input("enter the stock:"))
#if stock_availability != 0:
#    print("stock available")
#else:
#    print("stock not available")

#age = int(input("enter your age:"))
#test = input("enter your test result:")
#if age>=18 and test=="pass":
#   print("eligible for driving licence")
#else:
#   print("not eligible")

#day=input("Enter the day:")
#if day=="Saturday" or day=="Sunday":
#    print("It's a Weekend")
#else:
#    print("Not a weekend")

#order = int(input("Enter the order amount:"))
#customer = input("Are you are a premium member:")
#if order>=1000 or customer == "Yes":
#    print("Gets a free delivery")
#else:
#    print("No free delivery")

#block=input("is account blocked:")
#if not(block=="yes"):
#    print("access granted")
#else:
#   print("access denied") 

#age=int(input("enter your age:"))
#graduation=input("are you graduated:")
#banned=input("are you baned:")
#if age>=21 and graduation =="yes" and banned == "NO":
#    print("eligible")
#else:
#    print("not eligible")

#products = ["Laptop", "Mobile", "Tablet", "Headphones"]
#if "Laptop" in products:
 #   print("Available")
#else:
 #   print("not available")


#blocked_names = ["admin", "root", "system"]
#username="lucky"
#if username not in blocked_names:
 #   print("username accepted")
#else:
#    print("username not accepted")

Product_price = 1200
Quantity = 3
Discount = 500
product=["laptop","tablet","iphone"]
total_price=Product_price*Quantity
final_price=total_price-Discount
print("final amount =",final_price)
if final_price>= 2000:
    print("free delivery")
else:
    print("no free deliver")
if "laptop" in product:
    print("laptop is available")
else:
    print("laptop is not present")
