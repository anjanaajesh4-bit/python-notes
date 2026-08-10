fare1=0
fare2=0
fare3=0
passenger1=0
passenger2=0
passenger3=0
bus1 = {
    "name": "KSRTC",
    "From": "TVM",
    "To": "Ernakulam",
    "Amount": 700,
    "booked": []
}
bus2 = {
    "name": "KSRTC",
    "From": "TVM",
    "To": "Banglore",
    "Amount": 1400,
    "booked": []
}
bus3 = {
    "name": "kallada",
    "From": "TVM",
    "To": "Hydrebad",
    "Amount": 2000,
    "booked": []
}
buses = [bus1, bus2, bus3]
def viewbus():
    print("           Available bus")

    index = 1

    for bus in buses:
        print(index, bus["name"])
        print("  From = ", bus["From"])
        print("  TO = ", bus["To"])
        print("  Amount =", bus["Amount"])
        index += 1
while True:  
    viewbus()
    choice = int(input("Select Bus Number: "))
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    phone = input("Enter mobile number: ")
    seat = int(input("Select seat number (1-10): "))
    if choice == 1:
        while seat in bus1["booked"]:
            print("Seat no.", seat, "is already booked")
            seat = int(input("Select another seat: "))
        bus1["booked"].append(seat)
        print("Seat booked")
        passenger1+=1
        fare1+=bus1["Amount"]
        print("")
    elif choice == 2:
        while seat in bus2["booked"]:
            print("Seat no.", seat, "is already booked")
            seat = int(input("Select another seat: "))
        bus2["booked"].append(seat)
        print("Seat booked")
        passenger2+=1
        fare2+=bus2["Amount"]
    else:
        while seat in bus3["booked"]:
            print("Seat no.", seat, "is already booked")
            seat = int(input("Select another seat: "))
        bus3["booked"].append(seat)
        print("Seat booked")
        passenger3+=1
        fare3+=bus3["Amount"]
        print(bus1["From"]," to ",bus1["To"],passenger1)
        print(bus2["From"]," to ",bus2["To"],passenger2)
        print(bus3["From"]," to ",bus3["To"],passenger3)
    again=input("Book for another passanger(yes/no): ")
    if again=="no":
        break
print("Number of passengers= ",passenger1+passenger2+passenger3)
print("Total payable amount= ",fare1+fare2+fare3)