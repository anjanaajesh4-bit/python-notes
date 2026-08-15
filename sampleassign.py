print("            ONLINE BANKING SYSTEM")
balance=10000
transactions=[]
def create_account(account_type="savings"):
    print("        Create Account ")
    name=input("Enter your name: ")
    age=int(input("Enter your age: "))
    phone=input("Enter your phone number: ")
    print("      Account Created")
    print("Name: ",name)
    print("Age: ",age)
    print("Phone number: ",phone)
    print("Account type: ",account_type)
    return name,age,phone,account_type
def deposit(balance,amount):
    balance+=amount
    print("Amount deposited")
    print("Updated Balance= ",balance)
    return balance
def withdraw(balance,amount):
    balance-=amount
    print("Amount withdrawn: ")
    print("Update balance= ",balance)
    return balance
def check_balance(balance):
    print("Current balance= ",balance)
    return balance
def transaction_history(*transactions):
    print("         Transaction history")
    for i in transactions:
        print(i)
    return transactions
def loan_eligibility(balance):
    if balance>=10000:
        print("Costumer is eligible for loan")
        return "eligible"
    else:
        print("Costumer not eligible for loan")
        return "not eligible"
def pin(attempt):
    if attempt>3:
        print("Maximum attempts reached")
        return
    print("PIN Verification attempt: ",attempt)
    userpin=input("Enter pin: ")
    if userpin=="1234":
        print("PIN Verified")
        return
    print("INCORRECT PIN")
    pin(attempt+1)
while True:
    print("1. Create Account")
    print("2. Deposite")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Loan Eligibility")
    print("7. Calculate ineterest")
    print("8. Multiple Balance interest")
    print("9. Accounts above 10000")
    print("10. Sorted costumer names")
    print("11. PIN Verification")
    print("12. EXIT")
    choice=int(input("Enter option Number: "))
    if choice==12:
        print("THANK YOU")
        break
    if choice==1:
        name,age,phone,account_type=create_account()
    if choice==2:
        
        amount=(int(input("Enter Amount to be deposted: ")))
        balance=deposit(balance,amount)
        transactions.append(amount)
    if choice==3:
        
        amount = int(input("Enter Amount to be withdrawn: "))
        balance = withdraw(balance, amount)
        transactions.append(-amount)
    if choice==4:
        
        balance=check_balance(balance)
    if choice==5:
        transaction_history(*transactions)
    if choice==6:
        
        loan_eligibility(balance)
    if choice==7:
        interest_amount=int(input("enter principle amount: "))
        interest_rate=int(input("enter interest rate: "))
        interest=lambda interest_amount,interest_rate:interest_amount*interest_rate/100
        result=interest(interest_amount,interest_rate)
        print("Interest amount is: ",result)
    if choice==8:
        number=int(input("Enter number of balances: "))
        balances=[]
        for i in range(number):
            amount=int(input("Enter balance : "))
            balances.append(amount)
        interest_rate=float(input("Enter interest rate: "))
        interest=lambda balance:balance*interest_rate/100
        interest_results=list(map(interest,balances))
        print("Interest for multiple users: ",interest_results)
    if choice==9:
        balances=[5000,10000,15000,2000,25000,8000]
        eligible=list(filter(lambda balance:balance>10000,balances))
        print("Accounts with balance more than 10000: ")
        print(eligible)
    if choice==10:
        names=[]
        num=int(input("Enter number of costumers: "))
        for i in range(num):
            name=input("Enter Costumer name: ")
            names.append(name)
        sorted_names=sorted(names)
        print("Sorted Costumer Names:")
        print(sorted_names)
    if choice==11:
        pin(1)
