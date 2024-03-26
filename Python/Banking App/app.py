from banking_pkg import account

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

print("          === REGISTER: Automated Teller Machine ===          ")
name = input("Enter name to register: ")
pin = input("Enter PIN: ")
balance = (float(0))

print(f"{name} has been registered with a starting balance of ${balance}")

while True:
    print("          === LOGIN: Automated Teller Machine ===          ")
    username = input("Username: ")
    password = input("Password: ")

    if username == name and password == pin:
        print("Login successful!")
        break
    else:
        print("Invalid credentials.")

while True:
    atm_menu(name)
    option = input("Choose an option:")

    if option == "1":
        account.show_balance(balance)

    elif option == "2":
        account.deposit(balance)
        balance = account.deposit(balance)
        print(account.show_balance(balance))

    elif option == "3":
        account.withdraw(balance)
        balance = account.withdraw(balance)
        print(account.show_balance(balance))

    elif option == "4":
        account.logout(name)
        break