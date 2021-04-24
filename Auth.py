# registration - first name, last name, email and password

# login - account number and password

# Generate Account Number

# Bank Operations - withdrawal and deposit


import random


database = []

def init():
    print("you are welcome to BankJBL")

    have_an_account = int(input("do you have an account with us: 1 (no) 2 (yes) \n"))

    if have_an_account == 1:
        register()

    elif have_an_account == 2:
        login()

    else:
        print("you selected an invalid option")
        init()
            

def register():
    print("------ Register an account with us ------")

    first_name = input("what's your first name? \n")
    last_name = input("what's your last name? \n")
    email = input("what's your email address? \n")
    password = input("create a password \n")
    
    account_number = GenerateAccountNumber()

    new_user_created = { account_number, first_name, last_name, email, password }

    if new_user_created:

        print("your account has been created")
        print("*****************************")
        print("*****************************")
        print("your account number is: %d" % account_number)
        print("*****************************")
        print("*****************************")
        
        login()

    else:
        print(" Error, please try again")
        register()

def login():
    print("-----login your account details------")

    user_account_number = input("what's your account number?: \n")

    registered_account = ['1234567890', '9800808658', '9076138810', '3725202186']
    registered_password = ['passjubril', 'asdzxc', 'qwerty', 'qweasd']

    if (user_account_number in registered_account):
        password = input("what's your password?: \n")
        userId = registered_account.index(user_account_number)

        if (password == registered_password[userId]):
            bank_operations(user_account_number)

        else:
            print("------ inavlid password ------")
            init()

    else:
        print("your account number is inavlid")
        init()


def GenerateAccountNumber():
    return random.randrange(111111111,9999999999)  
# to generate account number:
# - import random
# - range numbers between 1 and 10, count < 10


def bank_operations(user_account_number):
    print(" welcome to BankJBL ")

    options_selected = int(input(" what would you like to do? (1) deposit (2) withdraw (3) exit (4) logout \n"))
    
    if options_selected == 1:
        deposit()

    elif options_selected == 2:
        withdraw()

    elif options_selected == 3:
        exit()

    elif options_selected == 4:
        logout()

    else:
        print(" you have selected an invalid option")
        bank_operations(user)    



def deposit():
    print("deposit operation")
    deposit_amount = int(input("how much woukd you like to deposit? \n"))
    init()
# still need to get current balance
# amount remaining after deposit
# to display the balance aftermath

def withdraw():
    print(" withdrawal operation")
    withdrawal_amount = int(input(" how muc would you like to withdraw? \n"))
    init()
# still need to get current balance before withdrawing
# amount remaining after withdraw
# to display the balance aftermath

def exit():
    print("*******thank you for banking with us******")
    logout()

def logout():
    init()


init()    