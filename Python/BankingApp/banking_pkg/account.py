def show_balance(balance):
    print(f"\nCurrent balance: ${balance:.2f}")

def deposit(balance):
    while True:
        try:
            amount = float(input("\nEnter amount to deposit: $"))
            if amount <=0:
                print("\nPlease eneter a positive amount.")
                continue
            break
        except ValueError:
            print("\nInvalid input. Please enter a number.")
    
    balance += amount
    print(f"Deposit successful. Your new balance is: ${balance:.2f}")
    return balance


def withdraw(balance):
    while True:
        try:
            amount = float(input("\nEnter amount to withdraw: $"))
            if amount <= 0:
                print("\nPlease enter a positive amount.")
                continue
            elif amount > balance:
                print("\nWithdrawal amount exceeds the current balance.")
                continue
            break
        except ValueError:
            print("\nInvalid input. Please enter a number.")
    
    balance -= amount
    print(f"Deposit successful. Your new balance is: ${balance:.2f}")
    return balance

def logout(name):
    print(f"\nGoodbye, {name}!")