class Emplyee:
    def __init__(self):
        self.__rating=0
        
    def evaluate(self,work_hours):
        if work_hours>8:
            self.__rating=5
        else:
            self.__rating
            
    def show_rating(self):
        print("Rating is :: ",self.__rating)
        
e = Emplyee()
e.evaluate(int(input("Enter work hourse :: ")))
e.show_rating()