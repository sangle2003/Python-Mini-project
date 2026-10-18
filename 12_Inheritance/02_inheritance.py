class Employee:
    def get_Emp(self):
        self.name = input("Enter Employee Name :: ")
        
class Developer(Employee):
    def get_Dev(self):
        self.language= input("Enter Developer language :: ")
        print(self.name,"code in ",self.language)
        
d = Developer()
d.get_Emp()
d.get_Dev()