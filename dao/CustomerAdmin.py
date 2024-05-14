from abc import ABC,abstractmethod

from Entity.entity import Customer


class CustomerAdmin(ABC):
    @abstractmethod
    def create_customer(self, customer: Customer):
        pass

    @abstractmethod
    def get_customer(self,customer_id):
        pass