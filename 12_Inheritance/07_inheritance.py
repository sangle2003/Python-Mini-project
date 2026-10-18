class Teachar:
    def t(self):
        self.subject = input("Enter subject :: ")
        
class Writer:
    def w(self):
        self.book = input("Enter book name :: ")
        
class student(Teachar,Writer):
    def show(self):
        print(self.subject,"is taught from a book ",self.book)
        
s = student()
s.t()
s.w()
s.show()