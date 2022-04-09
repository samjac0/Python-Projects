# Author Jacob Flaherty
#
# Python 3.10.4
#
# This is my first ever program in Python; demonstrating the passing of variable from function to function to creat a game.
#
#
#
#
#
#




def start():
    print("Hello {}!".format(get_name()))

    
def get_name():
    name = input("What is your name? ")
    return name

def start():
    fName = "Sarah"
    lName = "Connor"
    age = 28
    gender = "Female"
    getInfo(fName,lName,age,gender)

def getInfo(fName,lName,age,gender):
    print("My name is {} {}. I am a {} year-old {}.".format(fName,lName,age,gender))
        






if __name__ == "__main__":
    start()
