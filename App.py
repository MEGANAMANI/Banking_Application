from Entity.entity import Customer
from Exception.exceptions import InvalidAccountException
from Util.Utilproperty import DBConnUtil
from dao.BankServiceProviderImpl import BankServiceProviderImpl
from dao.CustomerServiceImpl import CustomerServiceImpl


class App():

    def __init__(self, customer:Customer):
        self.accounts = []
        self.conn = DBConnUtil.makeConnection()
        self.__customer= customer
        self.__BankService = BankServiceProviderImpl(accounts = [],branch_name="HMBank", brance_address="Pune", connection=self.conn)
        self.__CustomerService = CustomerServiceImpl(connection= self.conn)

        stmt = self.conn.cursor()
        customer_info = customer.get_customer_info()
        stmt.execute(f"select account_id from accounts where customer_id = {customer_info['customer_id']};")
        accounts = stmt.fetchall()
        for account in accounts:
            self.accounts.append(account[0])
        stmt.close()

    def create_account(self):
        print("Enter following information : ")
        accnType = input("Account Type (savings,current) : ")
        balance = input("Balance : ")

        account = self.__BankService.create_account(customer=self.__customer,acc_no=0, accType=accnType, balance= balance)
        print("Successfully Created the account")
        self.current_account = account
        self.conn.commit()
        return account


    def set_current_account(self):
        accNo = int(input("Enter enter account number : "))
        if not accNo in self.accounts:
            raise InvalidAccountException()
        account = self.__CustomerService.get_account_details(accNo)
        self.current_account = account
        return account
    def deposit(self):
        amount = int(input("Amount for deposit for current account : "))
        try:
            self.__CustomerService.deposit(account=self.current_account, amount=amount)
            self.conn.commit()
            print("Deposit successful")
        except Exception as e:
            print(f"Error occurred : {e}")

    def withdraw(self):
        amount = int(input("Amount for withdraw for current account : "))
        try:
            self.__CustomerService.withdraw(account=self.current_account, amount=amount)
            self.conn.commit()
            print("Withdrawal successful")
        except Exception as e:
            print(f"Error occurred : {e}")

    def get_balance(self):
        try:
            balance = self.__CustomerService.get_account_balance(account_number=self.current_account.get_account_info()["account_id"][0])
            print(balance)
        except Exception as e:
            print(f"Error occurred : {e}")

    def transfer(self):
        print("Enter following information")
        to_account_number =  int( input("Enter the account number to transfer to : "))
        amount = int(input("Enter amount to transfer : "))
        try:
            self.__CustomerService.transfer(from_account=self.current_account,to_account_number=to_account_number,amount=amount)
            self.conn.commit()
            print("Transfer Successful")
        except Exception as e:
            print(f"Error occurred : {e}")

    def getAccountDetails(self):
        print("Your current account details are :")
        print(self.__CustomerService.get_account_details(account_number=self.current_account["account_id"][0]))

    def getTransactions(self):
        print("Your transactions for current account are:")
        try:
            return self.__CustomerService.get_transactions(account=self.current_account)
        except Exception as e:
            print(f"Error occurred : {e}")



    def exit(self):
        self.conn.commit()
        self.conn.close()


