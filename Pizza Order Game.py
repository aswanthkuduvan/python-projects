print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

#checking the size of the pizza

if size == "s":
    bill = 15
elif size == "m":
    bill = 20
elif size == "l":
    bill = 25
else:
    print('wrong input')

#checking if customer want pepperoni

if pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3

#checking if customer want extra cheese

if extra_cheese == "y":
    bill += 1

#print the final bill

print(f'final bill is {bill}')