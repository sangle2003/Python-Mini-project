class Pen:
    def write(self):
        print("Writing with pen")
        
class Keyboard:
    def write(self):
        print("Typing with keyboard")
        
def write_somthing(tool):
    tool.write()
    
write_somthing(Pen())
write_somthing(Keyboard())