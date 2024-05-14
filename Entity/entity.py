class Customer():
    def __init__(self, customer_id, first_name, last_name, dob, email, phone_number, address):
        self.__customer_id = customer_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__dob = dob
        self.__email = email
        self.__phone_number = phone_number
        self.__address = address

    def get_customer_info(self):
        return {
            "customer_id": self.__customer_id,
            "first_name": self.__first_name,
            "last_name": self.__last_name,
            "dob": self.__dob,
            "email": self.__email,
            "phone_number": self.__phone_number,
            "address": self.__address
        }


class Account():
    def __init__(self, account_id, account_type, balance, customer: Customer):
        self.__account_id = account_id,
        self.__customer:Customer = customer
        self.__account_type = account_type
        self.__balance = balance

    def get_account_info(self):
        return {
            "account_id": self.__account_id,
            # "customer": self.__customer.get_customer_info(),
            "account_type": self.__account_type,
            "balance": self.__balance
        }

    def deposit(self, amount):
        #increase balance
        pass

    def withdraw(self, amount):
        if self.__balance > amount:
            pass
            #Withdraw

    def calculate_interest(self):
        return self.__balance + self.__balance * 0.045


class Transaction():
    def __init__(self, transaction_id, account:Account, transaction_type, amount, transaction_date):
        self.__transactions_id = transaction_id
        self.__account = account
        self.__transactions_type = transaction_type
        self.__amount = amount
        self.__transaction_date = transaction_date

    def get_transaction_info(self):
        return {
            "transactions_id":self.__transactions_id,
            # "account":self.__account,
            "transactions_type":self.__transactions_type,
            "amount":self.__amount,
            "transaction_date":self.__transaction_date
        }
