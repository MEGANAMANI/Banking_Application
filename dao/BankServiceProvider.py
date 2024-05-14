from abc import ABC,abstractmethod

from Entity.entity import Customer


class BankServiceProvider(ABC):
    @abstractmethod
    def create_account(customer: Customer, accNo,accType,balance):
        pass

    @abstractmethod
    def listAccounts(self):
        pass

    @abstractmethod
    def calculateInterest(self):
        pass