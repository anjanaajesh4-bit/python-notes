print("ONLINE BANKING SYSTEM")
def create_account(account_type="Savings"):
    print("Create Account:")
    name=input("Enter your name:")
    age=int(input("Enter your age:"))
    phone=input("Enter your phone number:")
    print("ACCOUNT CREATED")
    print("Name:",name)
    print("Age:",age)
    print("Phone Number:",phone)
    print("Account Type:", account_type)
# create_account()
balance=10000
def deposit(balance,amount):
    """This function adds amount to the balance"""
    balance+=amount
    print("Amount deposited successfully")
    print("New Balance:",balance)
    return balance
# balance = deposit(balance=balance, amount=50000)
def withdraw(balance,amount):
    """This function subtracts the withdrawal amount from the balance"""
    if amount > balance:
        print("Insufficient Balance")
        return balance
    balance-=amount
    print("Withdrawal Successfull!")
    print("New Balance:",balance)
    return balance
# withdraw(balance,30000)
def check_balance(balance):
    """This checks the balance"""
    print("Current Balance:",balance)
    return balance
# check_balance(balance)
def transaction_history(*transaction):
    """This gives the transaction history"""
    if len(transaction) == 0:
        print("No transactions yet")
        return
    print("Transaction History:",transaction)
    print("Number of Transactions:",len(transaction))
    print("Total Transactions:",sum(transaction))
    print("Largest Transaction:",max(transaction))
    print("Smallest Transaction:",min(transaction))
# transaction_history(40000,434,2432,43)
def loan_eligibility(balance):
    """Checks whether the customer is eligible for a loan"""
    if balance>10000:
        result="Eligible for loan"
    else:
        result="Not Eligible for loan"
    print(result)
    return result
# loan_eligibility(balance)
def customer_details(**data):
    print(data)
customer_details(name="Anjana",age=22,phone=974525353)
def display_message():
    print("Welcome to online banking")
result = display_message()
print(result)
def show_account():
    account_number=5635611
    print(account_number)
show_account()
bank_name="adfc"
def bank():
    print(bank_name)
bank()
service_charge=500
def update_charge():
    global service_charge
    service_charge=400
update_charge()
print("Service Charge:",service_charge)
def bank_service():
    charge=300
    def bank_service1():
        nonlocal charge
        charge=450
        print("Charge:",charge)
    bank_service1()
bank_service()
name="Global Name"
def outer():
    name="Bank Name"
    def inner():
        name="Customer Name"
        print(name)
    inner()
outer()
interest=lambda amount:amount*0.05
print(interest(100000))
gst=lambda amount:amount*0.08
print(gst(10000))
accounts={
    "Anu":25000,
    "Manu":30000,
    "Kiran":4000
}
sorted_accounts=sorted(accounts.items(),key=lambda account:account[1])
print(sorted_accounts)
interest_values=list(map(interest,accounts.values()))
print("Interest of all values:",interest_values)
high_balance=list(filter(lambda balance:balance>10000,accounts.values()))
print("Accounts with Balance > 10000:",high_balance)
def verify_pin(attempt):
    """PIN verification"""
    print(f"PIN verification attempt:{attempt}")
    pin=input("Enter your PIN: ")

    if pin == "1234":
        print("PIN Verified")
        return
    
    if attempt == 3:
        print("Maximum Attempts Reached")
    else:
        verify_pin(attempt+1)

# verify_pin(1)
import sys
print(sys.getrecursionlimit())
transactions = []
while True:
    print("---------------ONLINE BANKING SYSTEM------------------")
    print("1.Create Account")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Check Balance")
    print("5.Transaction History")
    print("6.Loan Eligibility")
    print("7.PIN Verification")
    print("8.EXIT")

    choice=int(input("Enter your choice:"))
    # print("DEBUG:", choice)
    if choice == 1:
        create_account()
    elif choice == 2:
        amount=int(input("Enter the Amount you want to deposit:"))
        balance=deposit(balance,amount)
        transactions.append(amount)
    elif choice == 3:
        amount = int(input("Enter the amount you want to Withdraw:"))
        if amount > balance:
            print("Insufficient Balance")
        else:
            balance = withdraw(balance, amount)
            transactions.append(amount)
    elif choice == 4:
        check_balance(balance)
    elif choice == 5:
        transaction_history(*transactions)
    elif choice == 6:
        loan_eligibility(balance)
    elif choice == 7:
        verify_pin(1)
    elif choice == 8:
        print("Thanks for using online banking system")
        break
    else:
        print("Invalid Choice")
