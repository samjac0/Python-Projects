
#Parent User Class
class User:
    name = "Mark"
    email = "mark@gmail.com"
    password = "1234abcd"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")

#Child Class Employee
class Employee(User):
    base_pay = 11.00
    department = "General"
    pin_number = "3980"

# This is the same method in the parent class "User"
# Alows use of pin instead of password

    def getLoginInfo(self):
            entry_name = input("Enter your name: ")
            entry_email = input("Enter your email: ")
            entry_pin = input("Enter your pin: ")
            if (entry_email == self.email and entry_pin == self.pin_number):
                print("Welcome back, {}!".format(entry_name))
            else:
                print("The password or email is incorrect.")

#Supplier Portal
class Supplier(User):
        company_freight_routing = "1123564789"
        password = "47586345"
        supplier_type = "Consumer Electronics"

# This is the same method in the parent class "User"
# Alows use of supplier routing # instead of password

    def getLoginInfo(self):
            company_freight_routing = input("Enter your freight routing number: ")
            entry_name = input("Enter your name: ")
            entry_password = input("Enter your password: ")
            if (company_freight_routing == self.company_freight_routing and entry_password == self.password):
                print("Welcome back, {}!".format(entry_name))
            else:
                print("The password or email is incorrect.")
                


# The following code invokes the methods inside each class for User and Employee and Supplier
customer = User()
customer.getLoginInfo()

manager = Employee()
manager.getLoginInfo()

company = Supplier()
company.getLoginInfo()

