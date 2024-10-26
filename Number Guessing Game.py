import random

number = random.randint(1,100)

while True:
    try:
        userGuess = int(input('Guess a number between 1 and 100: '))
        if userGuess > number:
            print('Too high 😮')
        elif userGuess < number:
            print('Too low 🙁')
        elif userGuess == number:
            print('Correct guess 😀')
            break
    except ValueError:
        print('Wrong input 🤔')
