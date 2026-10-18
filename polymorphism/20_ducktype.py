class Robot:
    def clean(self):
        print("Robot cleaning ")
        
class Human:
    def clean(self):
        print("Human cleaning ")
        
def clean_room(helper):
    helper.clean()
    
clean_room(Robot())
clean_room(Human())