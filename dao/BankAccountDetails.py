from abc import ABC, abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def __init__(self, account_number, customer_name, balance):
        pass

    @abstractmethod
    def get_information(self):
        pass

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass