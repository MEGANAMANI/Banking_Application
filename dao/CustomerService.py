from abc import ABC,abstractmethod

from Entity.entity import Customer, Account


class CustomerService(ABC):
    @abstractmethod
    def create_account(self, customer: Customer, acc_no, accType, balance):
        pass

    @abstractmethod
    def get_account_balance(self, account_number):
        pass

    @abstractmethod
    def deposit(self, account: Account, amount):
        pass

    @abstractmethod
    def withdraw(self, account: Account, amount):
        pass

    @abstractmethod
    def transfer(self, from_account: Account, to_account: Account, amount):
        pass

    @abstractmethod
    def get_account_details(self, account_number):
        pass

    @abstractmethod
    def get_transactions(self,account_number):
        pass