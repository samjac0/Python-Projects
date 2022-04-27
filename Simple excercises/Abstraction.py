#This is a brief excersise showing familiarity in class abstraction.
from abc import ABC, abstractmethod
class laptop(ABC):
    def paySlip(self, amount):
        print("Your payment amount: ",amount)
    @abstractmethod
    def payment(self, amount):
        pass

class DebitCardPayment(laptop):
    def payment(self, amount):
        print('Your purchase amount of {} meets and exceeds the minimum interest payment. No interest for you! '.format(amount))

obj = DebitCardPayment()
obj.paySlip("$350")
obj.payment("$350")
