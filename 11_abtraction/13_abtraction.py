from abc import ABC, abstractmethod


# Abstract Class
class Payment(ABC):

    def __init__(self, amount):
        self.amount = amount

    # Concrete Method
    def show_amount(self):
        print("Payment Amount:", self.amount)

    # Abstract Method
    @abstractmethod
    def make_payment(self):
        pass


# Single Inheritance
class UPI(Payment):

    def make_payment(self):
        print("Payment completed using UPI")


# Hierarchical Inheritance
class CreditCard(Payment):

    def make_payment(self):
        print("Payment completed using Credit Card")


class DebitCard(Payment):

    def make_payment(self):
        print("Payment completed using Debit Card")


# Multilevel Inheritance
class Wallet(Payment):

    def make_payment(self):
        print("Payment completed using Wallet")


class PayWallet(Wallet):

    def wallet_offer(self):
        print("Paytm wallet cashback applied")


# Creating UPI Object
upi = UPI(1500)
upi.show_amount()
upi.make_payment()

print("-------")


# Creating Credit Card Object
card = CreditCard(2500)
card.show_amount()
card.make_payment()

print("-------")


# Creating Debit Card Object
debit = DebitCard(1200)
debit.show_amount()
debit.make_payment()

print("-------")


# Creating PayWallet Object
wallet = PayWallet(1000)
wallet.show_amount()
wallet.make_payment()
wallet.wallet_offer()