from Entity.entity import Account


class SavingAccount(Account):
    def __init__(self, account_id, customer, balance):
        super().__init__(account_id = account_id,customer= customer, account_type="savings",balance= balance)

    def calculate_interest(self):
        return self.__balance + self.__balance * 0.05


class CurrentAccount(Account):
    def __init__(self, account_id, customer, balance):
        super().__init__(account_id = account_id, customer=customer,account_type= "current", balance=balance)

    def calculate_interest(self):
        return self.__balance
