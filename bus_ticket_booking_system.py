print("Welcome to Bus Ticket Booking!")
Name=input("Enter your Name:")
Age=int(input("Enter your age:"))
Phone_number=input("Enter your phone number:")
Gender=input("Enter your gender:")
no_of_passengers=int(input("Enter the number of passengers:"))
print("==========AVAILABLE BUSES==========")
BUS1={
    "BUS_NUMBER":"B101",
    "From":"Trivandrum",
    "To":"Kochi",
    "Departure":"09:00 AM",
    "Arrival":"02:30 PM",
    "Ticket_price":550,
    "Total_Seats":40,
    "Available_seats":30
}
for key, values in BUS1.items():
    print(key, ":", values)

print("---------------------------------------")
BUS2={
    "BUS_NUMBER":"B102",
    "From":"Banglore",
    "To":"Kochi",
    "Departure":"09:00 AM",
    "Arrival":"09:00 PM",
    "Ticket_price":1500,
    "Total_Seats":40,
    "Available_seats":30
}
for key, values in BUS2.items():
    print(key, ":", values)

print("---------------------------------------")
BUS3={
    "BUS_NUMBER":"B103",
    "From":"Trivandrum",
    "To":"Chennai",
    "Departure":"09:00 AM",
    "Arrival":"09:00 PM",
    "Ticket_price":1500,
    "Total_Seats":40,
    "Available_seats":30
}

for key, values in BUS3.items():
    print(key, ":", values)

print("---------------------------------------")
booking=input("Enter the Bus you want to book:")
if booking == "B101":
    print("Your selected Bus number is B101 from TVM to KOCHI")
    for key, values in BUS1.items():
        print(key, ":", values)
elif booking == "B102":
    print("Your selected Bus number is B102 from BANGLORE to KOCHI")
    for key, values in BUS2.items():
        print(key, ":", values)
elif booking == "B103":
    print("Your selected Bus number is B103 from TVM to CHENNAI")
    for key, values in BUS3.items():
        print(key, ":", values)
else:
    print("Invalid Bus Number")

seats=list(range(1,41))
booked_seats=[1,3,5,10,12,13,20,25,29,35]

for seat in seats:
    if seat in booked_seats:
        print(seat,"X",end="   ")
    else:
        print(seat,"A",end="   ")
print("------------------------------------------------------")
selected_seats=[]
for i in range(no_of_passengers):
    while True:
        selected_seat=int(input("Enter the seat number:"))
        if selected_seat not in seats:
            print("Invalid seat number .Please select seat number between 1 and 40")
        elif selected_seat in booked_seats:
            print("Seat already booked.Choose another seat.")
        elif selected_seat in selected_seats:
            print("You have already selected this seat.Please select another seat.")
        else:
            selected_seats.append(selected_seat)
            break
print("Selected Seats are:",selected_seats)
print("------------BOOKING SUMMARY-------------------")
print("Passenger Name:",Name)
print("Age:",Age)
print("Phone Number:",Phone_number)
print("Gender:",Gender)
print("Number of Passengers:",no_of_passengers)

print("Bus Number:",booking)
if booking == "B101":
    ticket_price = BUS1["Ticket_price"]
elif booking == "B102":
    ticket_price = BUS2["Ticket_price"]
elif booking == "B103":
    ticket_price = BUS3["Ticket_price"]

total_fare = ticket_price * no_of_passengers
print("Total Fare:",total_fare)
print("Seat Booked Successfully!")
print("----------------------------------------------")


