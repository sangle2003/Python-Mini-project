class company:
    def c(self):
        self.name=input("Enter Company Name :: ")
        
class HR(company):
    def hr(self):
        self.id=input("hires :: ")
        
class Tech(company):
    def tech(self):
        self.id=input("Tech :: ")
        
class Manager(HR,Tech):
    def man(self):
        print("company name is :: ",self.name)
        print("Hires :: ",self.id)
        print("Tech :: ",self.tech)
        
bj = Manager()
bj.c()
bj.hr()
bj.tech()
bj.man()
