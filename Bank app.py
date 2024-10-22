balance = 0 # Define a variable with zero

# Define a deposit function
def deposit():
    print('🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸')
    addAmount = int(input('Enter the amount: '))
    print(f'{addAmount} added to your account 💸')
    return addAmount

def display():
    print('🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸')
    print(f'Your balance is {balance} 💰')

# Define a withdrawal function
def withdrawal():
    print('🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸')
    print(f'{balance} Amount in your account ')
    withdrawAmount = int(input('Enter the amount to withdraw: '))
    if balance >= withdrawAmount:
        print(f'{withdrawAmount} is deducted from your account 💸')
        return withdrawAmount
    else:
        print('Sorry there is no much amount in your account 🫤')

# Define a while loop
while True:
    print('🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸')
    print('Welcome to the Bank program 🏦')
    print('''1 - for Deposit Amount\n2 - for Check balance\n3 - for Withdraw amount\n4 - for Exit''')
    print('🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸')
    option = input('Enter your option: ')
    if option == "1":
        balance += deposit() # Call the deposit function and add the deposit amount in the balance
    elif option == "2":
        display() # Call the amount checking
    elif option == "3":
        balance -= withdrawal() # call the withdrawal function and deduct the withdrawal amount
    elif option == "4":
        print('You press Exit,Thank you 😊')
        break
    else:
        print('Wrong option selected 🫤')