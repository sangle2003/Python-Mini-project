class Tax:
    def Calculate_tax(self,amount):
        return amount * 0.1
    

class IndiaTax(Tax):
    def calculate_tax(self, amount):
        return amount*0.18

class USATax(Tax):
    def calculate_tax(self,amount):
        return amount*0.07

class UKTax(Tax):
    def calculate_tax(self,amount):
        return amount*0.20

taxes=[IndiaTax(),USATax(),UKTax()]

for t in taxes:
    print(t.calculate_tax(20000))