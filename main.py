import datetime

from App import App
from Entity.entity import Customer
from Util.Utilproperty import DBConnUtil
from dao.AccountType import SavingAccount, CurrentAccount
from dao.BankServiceProviderImpl import BankServiceProviderImpl
from dao.customer import customer
from dao.CustomerServiceImpl import CustomerServiceImpl


def customer_eligible_for_loan(credit_score, annual_income):
    if credit_score > 700:
        if annual_income > 50000:
            return True
        else:
            return False
    else:
        return False


def future_balance_for_compound_interest(initial_balance, annual_interest_rate, years):
    future_balance = initial_balance * (1 + annual_interest_rate / 100) ** years
    return future_balance


def check_balance(account_id):
    #get balance from account
    pass


def password_validation(password):
    if len(password) < 8:
        return False

    flag1 = False
    flag2 = False
    for char in password:
        if not char.isupper():
            flag1 = True
        elif not char.isdigit():
            flag2 = True

    return flag1 and flag2


def transactions():
    #implement the transaction
    pass

def Admin_options():
    while True:
        print("Choose option from below")
        print("1) Create customer ")
        print("2) List Customer")
        print("3) Update Customer")
        print("4) Delete Customer")
        print("5) List Accounts")
        print("6) Find Account")
        print("7) Update Account")
        print("8) Detele Account")
        print("9) Exit")

        option = int(input("Option : "))

        if option ==1:
            print("Give following information")
            first_name = input("First Name : ")
            last_name = input("Last Name : ")
            dob = input("Date of birth(yyyy-mm-dd) : ")
            email = input("Email : ")
            phone_number = input("phone_number : ")
            address = input("address : ")
            try:
                temp_cust = customer.create_customer(Customer(0, first_name, last_name, dob, email, phone_number, address))
                print("Customer created successfully ")
                # current_customer = temp_cust
                print(temp_cust.get_customer_info())
            except Exception as e:
                print(f"Error occurred : {e}")

        elif option == 2:
            try:
                customers = customer.list_customer()
                for cust in customers:
                    print(cust.get_customer_info())
            except Exception as e:
                print(f"Error occurred : {e}")
        elif option == 3:
            custID = int(input("Customer ID to update : "))
            try:
                customer.update_customer(customer_id=custID)
            except Exception as e:
                print(f"Error occurred : {e}")
        elif option == 4:
            custID = int(input("Customer ID to delete : "))
            try:
                customer.delete_customer(customer_id=custID)
            except Exception as e:
                print(f"Error occurred : {e}")

        elif option == 5:
            try:
                accounts = customer.list_accounts()
                for acc in accounts:
                    print(acc.get_account_info())
            except Exception as e:
                print(f"Error occurred : {e}")

        elif option == 6:
            accId = int(input("Account Id : "))
            try:
                account = customer.get_account(accId)
                print(account.get_account_info())
            except Exception as e:
                print(f"Error occurred : {e}")

        elif option == 7:
            accID = int(input("Account ID to update : "))
            try:
                customer.update_account(accID)
            except Exception as e:
                print(f"Error occurred : {e}")

        elif option == 8:
            accID = int(input("Account ID to update : "))
            try:
                customer.delete_account(accID)
            except Exception as e:
                print(f"Error occurred : {e}")

        elif option ==9 :
            break


if __name__ == "__main__":

    customer= Customer()
    current_customer = None

    while True:
        print("Choose option to use")
        print("1) Admin")
        print("2) Customer")
        option = int( input("Option : "))

        if option == 1:
            Admin_options()
            break
        elif option == 2:
            break
        else: print("Choose correct option")


    while True:
        customer_id = int(input("Give your customer Id : "))
        try:
            temp_cust = customer.get_customer(customer_id=customer_id)
            print("Customer details fetched successfully")
            current_customer=temp_cust
            print(current_customer.get_customer_info())
            break
        except Exception as e:
            print(f"Error occurred : {e}")



    Banking = App(customer=current_customer)

    while True:
        print("Choose operation:")
        print("1) create account")
        print("2) Open Existing Account")

        option = int(input("Option : "))

        if option == 1:
            try:
                Banking.create_account()
                break
            except Exception as e:
                print(f"Error occurred : {e}")
        elif option == 2:
            try:
                print(f"Valid account Ids = {Banking.accounts}")
                Banking.set_current_account()
                break
            except Exception as e:
                print(f"Error occurred : {e}")
        else:
            print("invalid option please retry")

    while True:

        print("Options")
        print("1) Check Balance")
        print("2) Withdraw")
        print("3) Deposit")
        print("4) Transfer")
        print("5) Get all transactions")
        print("6) Exit")

        selected = int(input("Option : "))

        if selected == 1:
            print("Checking Balance")
            Banking.get_balance()
        elif selected == 2:
            print("Withdrawing")
            Banking.withdraw()

        elif selected == 3:
            print("Depositing")
            Banking.deposit()

        elif selected == 4:
            print("Transfering")
            Banking.transfer()

        elif selected == 5:
            print("Getting all transactions")
            transactions = Banking.getTransactions()
            for transaction in transactions:
                print(transaction.get_transaction_info())

        elif selected == 6:
            print("Visit again!!")
            Banking.exit()
            break

        else:
            print("Enter valid input")
