from Exception.exceptions import CustomerNotFoundException, InvalidAccountException
from Entity.entity import Customer, Account
from Util.Utilproperty import DBConnUtil
from dao.CustomerAdmin import CustomerAdmin


class CustomerAdmin(CustomerAdmin):

    def __init__(self):
        pass

    def create_customer(self, customer: Customer):
        conn = DBConnUtil.makeConnection()
        stmt = conn.cursor()
        customer_info = customer.get_customer_info()

        stmt.execute(
            f"""INSERT INTO customers 
                (first_name, last_name, dob, email, phone_number, address) 
                VALUES 
                ('{customer_info["first_name"]}', '{customer_info["last_name"]}', '{customer_info["dob"]}', 
                 '{customer_info["email"]}', '{customer_info["phone_number"]}', '{customer_info["address"]}');
            """)

        conn.commit()

        stmt.execute("SELECT customer_id FROM customers ORDER BY customer_id DESC LIMIT 1;")
        customer_id = stmt.fetchone()[0]

        conn.commit()
        stmt.close()
        conn.close()

        return Customer(customer_id=customer_id, first_name=customer.get_customer_info()["first_name"],
                        last_name=customer.get_customer_info()["last_name"], dob=customer.get_customer_info()["dob"],
                        email=customer.get_customer_info()["email"],
                        phone_number=customer.get_customer_info()["phone_number"],
                        address=customer.get_customer_info()["address"])

    def get_customer(self, customer_id):
        conn = DBConnUtil.makeConnection()
        stmt = conn.cursor()
        stmt.execute(f"select * from customers where customer_id = {customer_id};")
        customer = stmt.fetchall()
        if len(customer) == 0: raise CustomerNotFoundException()
        customer = customer[0]
        conn.commit()
        conn.close()
        return Customer(customer[0], customer[1], customer[2], customer[3], customer[4], customer[5], customer[6])

    def update_customer(self, customer_id):
        conn = DBConnUtil.makeConnection()
        stmt = conn.cursor()
        self.get_customer(customer_id)
        print("Select value to update ")
        print("1) First name")
        print("2) Last name")
        print("3) dob")
        print("4) Email")
        print("5) Phone Number")
        print("6) Address")
        val_change = "not selected "
        option = int(input("Option : "))
        if option == 1:
            val_change = "first_name"
        elif option == 2:
            val_change = "last_name"
        elif option == 3:
            val_change = "dob"
        elif option == 4:
            val_change = "email"
        elif option == 5:
            val_change = "phone_number"
        elif option == 6:
            val_change = "address"

        value = input(f"New Value for the {val_change} : ")
        stmt = conn.cursor()

        stmt.execute(f"update customers set {val_change} = '{value}' where customer_id = {customer_id};")
        conn.commit()
        conn.close()
        print("Value updated successfully")

    def list_customer(self):
        conn = DBConnUtil.makeConnection()
        stmt = conn.cursor()
        stmt.execute("select * from customers")
        customers = stmt.fetchall()
        cust_arr = []
        if len(customers) == 0: raise CustomerNotFoundException()

        for customer in customers:
            cust_arr.append(
                Customer(customer[0], customer[1], customer[2], customer[3], customer[4], customer[5], customer[6]))

        conn.close()
        return cust_arr

    def delete_customer(self, customer_id):
        self.get_customer(customer_id)
        conn = DBConnUtil.makeConnection()
        stmt = conn.cursor()
        stmt.execute(f"delete from customers where customer_id = {customer_id};")
        print("Deleted Successfully")

        conn.commit()
        conn.close()

    def list_accounts(self):
        conn = DBConnUtil.makeConnection()
        stmt = conn.cursor()
        stmt.execute("select * from accounts")
        accounts = stmt.fetchall()
        acc_arr = []
        if len(accounts) == 0: raise InvalidAccountException()

        for acc in accounts:
            acc_arr.append(
                Account(acc[0], acc[1], acc[2], acc[3])
            )

        conn.close()
        return acc_arr

    def get_account(self,account_id):
        conn = DBConnUtil.makeConnection()
        stmt = conn.cursor()
        stmt.execute(f"select * from accounts where account_id ={account_id};")
        accounts = stmt.fetchall()
        if len(accounts) == 0: raise CustomerNotFoundException()
        accoun = accounts[0]
        conn.commit()
        conn.close()
        return Account(accoun[0],accoun[1],accoun[2],accoun[3])

    def delete_account(self,account_id):
        self.get_account(account_id)
        conn = DBConnUtil.makeConnection()
        stmt = conn.cursor()
        stmt.execute(f"delete from accounts where account_id = {account_id};")
        print("Deleted Successfully")

        conn.commit()
        conn.close()

    def update_account(self,account_id):
        conn = DBConnUtil.makeConnection()
        stmt = conn.cursor()
        self.get_account(account_id)
        print("Select value to update ")
        print("1) Account Type")
        print("2) Balance")
        val_change = "not selected "
        option = int(input("Option : "))
        if option == 1:
            val_change = "account_type"
        elif option == 2:
            val_change = "balance"

        value = input(f"New Value for the {val_change} : ")
        stmt = conn.cursor()

        stmt.execute(f"update accounts set {val_change} = '{value}' where account_id = {account_id}")
        conn.commit()
        conn.close()
        print("Value updated successfully")

