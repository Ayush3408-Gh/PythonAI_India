import random

accounts = {}

def find_account(account_number):
    if account_number in accounts:
        return accounts[account_number]
    else:
        return None

def verify_pin(account, pin):
    if account['pin'] == pin:
        return True
    else:
        return False

def create_account():
    print("\n=== Create New Account ===")
    name = input("Enter your name: ")
    mobile = input("Enter your mobile number: ")
    pin = input("Enter a 4-digit PIN: ")
    initial_deposit = float(input("Enter initial deposit amount: "))

    account_number = random.randint(1000, 9999)

    accounts[account_number] = {
        'account_number': account_number,
        'name': name,
        'mobile': mobile,
        'pin': pin,
        'balance': initial_deposit
    }

    print("Account created successfully!")
    print("Your Account Number:", account_number)

def deposit_money():
    print("\n=== Deposit Money ===")
    account_number = int(input("Enter your account number: "))
    account = find_account(account_number)

    if account == None:
        print("Account not found.")
    else:
        pin = input("Enter your 4-digit PIN: ")
        if verify_pin(account, pin) == False:
            print("Incorrect PIN.")
        else:
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                print("Invalid amount.")
            else:
                account['balance'] = account['balance'] + amount
                print("Deposit successful! New Balance:", account['balance'])

def withdraw_money():
    print("\n=== Withdraw Money ===")
    account_number = int(input("Enter your account number: "))
    account = find_account(account_number)

    if account == None:
        print("Account not found.")
    else:
        pin = input("Enter your 4-digit PIN: ")
        if verify_pin(account, pin) == False:
            print("Incorrect PIN.")
        else:
            amount = float(input("Enter amount to withdraw: "))
            if amount > account['balance']:
                print("Insufficient balance.")
            elif amount <= 0:
                print("Invalid amount.")
            else:
                account['balance'] = account['balance'] - amount
                print("Withdrawal successful! New Balance:", account['balance'])

def check_balance():
    print("\n=== Check Balance ===")
    account_number = int(input("Enter your account number: "))
    account = find_account(account_number)

    if account == None:
        print("Account not found.")
    else:
        pin = input("Enter your 4-digit PIN: ")
        if verify_pin(account, pin) == False:
            print("Incorrect PIN.")
        else:
            print("Account Number:", account['account_number'])
            print("Account Holder:", account['name'])
            print("Current Balance:", account['balance'])

def main():
    print("Welcome to Simple Banking System")

    while True:
        print("\n1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            create_account()
        elif choice == '2':
            deposit_money()
        elif choice == '3':
            withdraw_money()
        elif choice == '4':
            check_balance()
        elif choice == '5':
            print("Thank you for using Simple Banking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
