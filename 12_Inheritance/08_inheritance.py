class Camera:
    def cam(self):
        self.mp = input("Enter MP :: ")
        
class Brand:
    def ph(self):
        self.brand = input("Enter Brand :: ")
        
class SmartPhone(Camera,Brand):
    def disp(self):
        print("smartphone has camera of ",self.mp,"and is is of ",self.brand,"brand")
        
s = SmartPhone()
s.cam()
s.ph()
s.disp()