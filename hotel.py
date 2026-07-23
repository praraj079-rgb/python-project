while True:
    print("\n===== HOTEL MANAGEMENT SYSTEM =====")

    customer = input("Enter Customer Name: ")

    room_no = int(input("Enter Room Number: "))
    days = int(input("Enter Number of Days: "))

    print("\n=========Room Types=========")
    print("1. Standard Room - ₹1000/day")
    print("2. Deluxe Room   - ₹2000/day")
    print("3. Suite Room    - ₹3500/day")
    print("-----------------------------")

    choice = int(input("Enter Room Type: "))

    if choice == 1:
        room_type = "Standard Room"
        rent = 1000
    elif choice == 2:
        room_type = "Deluxe Room"
        rent = 2000
    elif choice == 3:
        room_type = "Suite Room"
        rent = 3500
    else:
        print("Invalid Room Type")
        continue

    room_bill = rent * days

    print("\n==========Food Types==========")
    print("1. Fine Dining       - ₹1500/day")
    print("2. Casual Dining     - ₹2500/day")
    print("3. Fast Food Service - ₹4500/day")
    print("4. Buffet Service    - ₹6000/day")
    print("5. Cafeteria Service - ₹7500/day")
    print("--------------------------------")

    choice = int(input("Enter Food Type: "))

    if choice == 1:
        food_type = "Fine Dining"
        fd_amt = 1500
    elif choice == 2:
        food_type = "Casual Dining"
        fd_amt = 2500
    elif choice == 3:
        food_type = "Fast Food Service"
        fd_amt = 4500
    elif choice == 4:
        food_type = "Buffet Service"
        fd_amt = 6000
    elif choice == 5:
        food_type = "Cafeteria Service"
        fd_amt = 7500
    else:
        print("Invalid Food Type")
        continue

    food_bill = fd_amt * days
    total = room_bill + food_bill

    print("\n========== HOTEL BILL ==========")
    print("Customer Name :", customer)
    print("Room Number   :", room_no)
    print("Room Type     :", room_type)
    print("Food Type     :", food_type)
    print("Days Stayed   :", days)
    print("Room Rent     : ₹", room_bill)
    print("Food Charges  : ₹", food_bill)
    print("-------------------------------")
    print("Total Bill    : ₹", total)
    print("===============================")

    ch = input("\nDo you want to book another room? (yes/no): ")

    if ch.lower() != "yes":
        print("\nThank you for visiting our hotel!")
        break