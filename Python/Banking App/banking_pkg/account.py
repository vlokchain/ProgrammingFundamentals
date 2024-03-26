def show_balance(balance):
    print("Current balance: $",float(balance))

def deposit(balance):
    amount = float(input("Enter amount to deposit: $"))
    balance =+ amount
    return balance

def withdraw(balance):
    withdraw = float(input("Enter amount to withdraw: $"))
    balance =- withdraw
    return balance

def logout(name):
    print(f"Goodbye{name}")
    exit()