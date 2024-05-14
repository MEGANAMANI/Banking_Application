from Entity.entity import Customer
from Util.Utilproperty import DBConnUtil
from dao.AccountType import SavingAccount, CurrentAccount
from dao.CustomerServiceImpl import CustomerServiceImpl
from dao.BankServiceProvider import BankServiceProvider

conn = DBConnUtil().makeConnection()
class BankServiceProviderImpl(CustomerServiceImpl, BankServiceProvider):

    def __init__(self, accounts, branch_name, brance_address, connection):
        super().__init__(connection)
        self.__accounts = accounts
        self.__branch_address = brance_address
        self.__branch_name = branch_name
        self.__conn = connection

    def create_account(self, customer: Customer, acc_no, accType, balance):
        # self.__customer = customer
        stmt = self.__conn.cursor()
        customer_id = customer.get_customer_info()["customer_id"]
        stmt.execute(
            f"INSERT INTO accounts (customer_id, account_type, balance) VALUES ({customer_id}, '{accType}', {balance})")

        stmt.execute("SELECT * FROM accounts ORDER BY account_id DESC LIMIT 1")
        account = stmt.fetchone()

        if account[2] == "savings":
            account = SavingAccount(account_id=account[0], customer=customer, balance=account[3])
        else:
            account = CurrentAccount(account_id=account[0], customer=customer, balance=account[3])
        print(f"Account information : ")
        print(account.get_account_info())

        stmt.close()
        return account

    def listAccounts(self):
        stmt = self.__conn.cursor()
        stmt.execute("select * from accounts;")
        accounts = stmt.fetchall()
        accounts_arr = []
        for account in accounts:
            if(account[2] == "savings"):
                accounts_arr.append(SavingAccount(account_id= account[0], customer=Customer(account[1],"","","","",0,""), balance=account[3]))
            else:
                accounts_arr.append(CurrentAccount(account_id= account[0], customer=Customer(account[1],"","","","",0,""), balance=account[3]))
        self.__accounts=accounts_arr
        return accounts_arr

    def calculateInterest(self):
        pass