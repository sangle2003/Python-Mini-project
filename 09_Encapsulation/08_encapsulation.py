class ATM:
    def __init__(self,pin,balance):
        self.__pin=pin
        self.__balance=balance
        
    def check_balance(self,entered_pin):
        if entered_pin==self.__pin:
            print("Balance is :: ",self.__balance)
        else:
            print("Ivalid pin")
            
atm = ATM(1234,5000)

        
        