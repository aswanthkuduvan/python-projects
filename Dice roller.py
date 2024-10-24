import random

while True:
    print('Welcome to Dice roller game 🎲')
    option = input('Do you want to roll dice(Y/N): ').lower()
    if option == "y":
        print(f'{random.randint(1,9),random.randint(1,9)}')
    elif option== "n":
        print('You press Exit, Thank you 😊')
        break
    else:
        print('Invalid option 🫤')