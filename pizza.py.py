print("🍕 Welcome to Python Pizza Deliveries 🍕")


pizza_size = input("What size pizza do you want? (S, M OR L):\n").upper()
pepperoni = input("Do you want pepperoni? (Y or N):\n").upper()
extra_cheese = input("Do you want extra cheese? (Y or N):\n").upper()

if pizza_size == "S":
    bill = 15
    if pepperoni == "Y":
        bill = bill + 2
    if extra_cheese == "Y":
        bill = bill + 1
    print(f"Your final bill is : ${bill}")
    
elif pizza_size == "M":
    bill = 20
    if pepperoni == "Y":
        bill = bill + 3
    if extra_cheese == "Y":
        bill = bill + 1
    print(f"Your final bill is : ${bill}")
elif pizza_size == "L":
    bill = 25
    if pepperoni == "Y":
        bill = bill + 3
    if extra_cheese == "Y":
        bill = bill + 1
    print(f"Your final bill is : ${bill}")
else:
    print("Make sure you taped the right input")



