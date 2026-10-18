class father:
    def fatherskill(self):
        print("he drive so well")
        
class mother:
    def motherskill(self):
        print("she cookc so well")
        
class child(father,mother):
    def childskill(self):
        print("child can study ")
        
obj = child()
obj.fatherskill()
obj.motherskill()
obj.childskill()