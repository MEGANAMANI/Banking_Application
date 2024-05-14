import datetime
from Exception.exceptions import InvalidAccountException, InsufficientFundException
from Entity.entity import Customer, Account, Transaction
#from Util.Utilproperty import DBConnUtil
from dao.AccountType import SavingAccount, CurrentAccount
from dao.CustomerService import CustomerService


class CustomerServiceImpl(CustomerService):

    def __init__(self, connection):
        self.__conn = connection

    def create_account(self, customer: Customer, acc_no, accType, balance):
        customer_info = customer.get_customer_info()
        customer_id = customer_info["customer_id"]

        with self.__conn.cursor() as stmt:
            if accType == "savings":
                stmt.execute(
                    "INSERT INTO accounts (customer_id, account_type, balance) VALUES (%s, 'savings', %s);",
                    (customer_id, balance)
                )
            else:
                stmt.execute(
                    "INSERT INTO accounts (customer_id, account_type, balance) VALUES (%s, 'current', %s);",
                    (customer_id, balance)
                )
            self.__conn.commit()
            stmt.execute("SELECT account_id FROM accounts ORDER BY account_id DESC LIMIT 1;")
            account_id = stmt.fetchone()[0]
            print(account_id)

        if accType == "savings":
            return SavingAccount(account_id, customer, balance)
        elif accType == "current":
            return CurrentAccount(account_id, customer, balance)

    def get_account_balance(self, account_number):
        with self.__conn.cursor() as stmt:
            stmt.execute("SELECT balance, account_type FROM accounts WHERE account_id = %s;", (account_number,))
            row = stmt.fetchone()
            if row is None:
                raise InvalidAccountException()
            return {"balance": row[0], "account_type": row[1]}

    def deposit(self, account: Account, amount):
        account_info = account.get_account_info()
        account_id = account_info["account_id"]
        transaction_date = datetime.date.today()

        with self.__conn.cursor() as stmt:
            stmt.execute(
                "INSERT INTO transactions (account_id, transaction_type, amount, transaction_date) VALUES (%s, 'deposit', %s, %s);",
                (account_id, amount, transaction_date)
            )
            stmt.execute(
                "UPDATE accounts SET balance = balance + %s WHERE account_id = %s;",
                (amount, account_id)
            )
            self.__conn.commit()
            print(self.get_account_balance(account_id))

    def withdraw(self, account: Account, amount):
        account_info = account.get_account_info()
        account_id = account_info["account_id"]
        balance = self.get_account_balance(account_id)["balance"]

        if amount > balance:
            raise InsufficientFundException()

        transaction_date = datetime.date.today()

        with self.__conn.cursor() as stmt:
            stmt.execute(
                "INSERT INTO transactions (account_id, transaction_type, amount, transaction_date) VALUES (%s, 'withdrawal', %s, %s);",
                (account_id, amount, transaction_date)
            )
            stmt.execute(
                "UPDATE accounts SET balance = balance - %s WHERE account_id = %s;",
                (amount, account_id)
            )
            self.__conn.commit()
            print(self.get_account_balance(account_id))

    def transfer(self, from_account: Account, to_account_number, amount):
        from_account_info = from_account.get_account_info()
        from_account_id = from_account_info["account_id"]
        balance = self.get_account_balance(from_account_id)["balance"]

        if amount > balance:
            raise InsufficientFundException()

        transaction_date = datetime.date.today()

        with self.__conn.cursor() as stmt:
            stmt.execute(
                "INSERT INTO transactions (account_id, transaction_type, amount, transaction_date) VALUES (%s, 'transfer', %s, %s);",
                (from_account_id, amount, transaction_date)
            )
            stmt.execute(
                "UPDATE accounts SET balance = balance + %s WHERE account_id = %s;",
                (amount, to_account_number)
            )
            stmt.execute(
                "UPDATE accounts SET balance = balance - %s WHERE account_id = %s;",
                (amount, from_account_id)
            )
            self.__conn.commit()

    def get_account_details(self, account_number):
        with self.__conn.cursor() as stmt:
            stmt.execute("SELECT * FROM accounts WHERE account_id = %s;", (account_number,))
            account = stmt.fetchone()
            if account is None:
                raise InvalidAccountException()

            stmt.execute(
                "SELECT * FROM customers WHERE customer_id = (SELECT customer_id FROM accounts WHERE account_id = %s);",
                (account_number,))
            customer_row = stmt.fetchone()
            customer = Customer(customer_row[0], customer_row[1], customer_row[2], customer_row[3], customer_row[4],
                                customer_row[5], customer_row[6])
            print("Customer information:")
            print(customer.get_customer_info())

            if account[2] == "savings":
                account_obj = SavingAccount(account_id=account[0], customer=customer, balance=account[3])
            else:
                account_obj = CurrentAccount(account_id=account[0], customer=customer, balance=account[3])
            print("Account information:")
            print(account_obj.get_account_info())

        return account_obj

    def get_transactions(self, account: Account):
        account_info = account.get_account_info()
        account_id = account_info["account_id"]

        with self.__conn.cursor() as stmt:
            stmt.execute("SELECT * FROM transactions WHERE account_id = %s;", (account_id,))
            transactions = stmt.fetchall()
            tran_arr = [Transaction(transaction_id=tran[0], account=account, transaction_type=tran[2], amount=tran[3],
                                    transaction_date=tran[4]) for tran in transactions]

        return tran_arr

