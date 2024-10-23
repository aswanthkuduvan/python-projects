def addition():
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    result = num1 + num2
    print(f'Result is {result}')

def subtraction():
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    result = num1 - num2
    print(f'Result is {result}')

def multiplication():
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    result = num1 * num2
    print(f'Result is {result}')

def division():
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    result = num1 / num2
    print(f'Result is {round(result,2)}')

while True:
    print('🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸')
    print("1 - for Addition ➕\n2 - for subtraction ➖\n3 - for Multiplication ✖️\n4 - for Division ➗\n5 - for Exit 🚶")
    option = input('Enter your option: ')
    print('🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸')
    if option == "1":
        addition()
    elif option == "2":
        subtraction()
    elif option == "3":
        multiplication()
    elif option == "4":
        division()
    elif option == "5":
        print('You have selected Exit, Thank you 😊')
        break
    else:
        print('Wrong option 🫤')
