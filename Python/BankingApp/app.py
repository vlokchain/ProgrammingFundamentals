from banking_pkg import account

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

print("\n=== Automated Teller Machine ===\n=== REGISTRATION: PLEASE ENTER YOUR DESIRED USERNAME AND PIN ===")

while True:
    name = input("\nEnter username to register: ").strip()
    if 0 < len(name) <= 10:
        break
    print("\nUsername must be between 1 and 10 characters.")

while True:
    pin = input("Enter PIN: ").strip()
    if len(pin) == 4 and pin.isdigit():
        break
    print("\nPIN must be exactly 4 digits.")

balance = 0.0

print(f"\n'{name}' has been registered with a starting balance of ${balance:.2f}")

# Login process

while True:
    print("\n=== Automated Teller Machine ===\n=== LOG IN: PLEASE LOGIN WITH YOUR REGISTERED USERNAME AND PIN ===")
    username = input("\nUsername: ").strip()
    password = input("PIN: ").strip()

    if username == name and password == pin:
        print("Login succesful!")
        break
    else:
        print("Invalid credentials. Please try again.")

# Main ATM loop

while True:
    atm_menu(name)
    option = input("Choose an option: ").strip()

    if option == "1":
        account.show_balance(balance)

    elif option == "2":
        balance = account.deposit(balance)

    elif option == "3":
        balance = account.withdraw(balance)

    elif option == "4":
        account.logout(name)
        break

    else:
        print("Invalid option, please try again.")