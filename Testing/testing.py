import unittest

from App import App
from Exception.exceptions import CustomerNotFoundException, InvalidAccountException
from dao.customer import Customer


class testcases(unittest.Testing):
    def setUp(self):
        self.customer = Customer()
        self.App = App(Customer(0,"","","","","",""))


    def test_create_customer(self):
        temp_cust = self.customer.create_customer(Customer(0, first_name="someone", last_name="newone", dob="1968-02-04", email="someone@example.com", phone_number = "2898512618", address = "Nanded"))

        self.assertNotEqual(temp_cust,None)

    def test_get_customer(self):
        with self.assertRaises(CustomerNotFoundException):
            temp_cust = self.customer.get_customer(customer_id=20)


    def test_get_transactions(self):
        with self.assertRaises(InvalidAccountException):
            self.App.set_current_account()
            transactions = self.App.getTransactions()
