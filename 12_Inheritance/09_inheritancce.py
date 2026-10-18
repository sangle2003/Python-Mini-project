class song:
    def s(self):
        self.song = input("Enter song name :: ")
        
class Dancer:
    def d(self):
        self.style = input("Enter style of Dance :: ")
        
class Perfomance(song,Dancer):
    def show(self):
        print("Perfomance is performing on ",self.song,"with dance style ",self.style)
        
p = Perfomance()
p.s()
p.d()
p.show()