class User:
    #Define the attributes of the class
    name = "Sally"
    email = ""
    password = "1234abcd"
    account = 0

    #methods of the class
    def login(self):
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}".format(self.name))
        else:
            print("You are not authorized for this page.")

    #Instance of the user class
    new_user = User()
    #Call the login method using the new object
    new_user.login()
    
