print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child ticket is $5.")
    elif age <= 18:
        bill = 7
        print("Youth ticket is $7.")
    else:
        bill = 12
        print("Adult Ticket is $12.")
    wants_photo = input("Do you want to have a photo? Type y for yes and n for no")
    if wants_photo == "y":
        bill += 3
    print(f"your final bill is $", {bill})
else:
    print("Sorry you have to grow taller before you can ride.")
