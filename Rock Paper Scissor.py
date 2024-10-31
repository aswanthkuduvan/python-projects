import random

choices = ('r','p','s')
emoji = {'r':'🪨', 'p':'📰', 's':'✂️'}
computer = random.choice(choices)

while True:
    user = input('Rock, Paper or Scissor? (r/p/s): ').lower()
    if user not in choices:
        print('Wrong input 🫤')
        continue

    print(f'You choose {emoji[user]}')
    print(f'Computer choose {emoji[computer]}')

    if computer == user:
        print('Its a tie 🫰')
    elif (computer == "r" and user == "s") or (computer =="p" and user == "r") or (computer =="s" and user == "p"):
        print('You lose 😔')
    else:
        print('you Win 😀')

    repeatGame = input('Do you want to continue? (y/n): ').lower()
    if repeatGame == "y":
        continue
    else:
        print('You choose Exit, Thank you 😊')
        break