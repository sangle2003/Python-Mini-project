class Teacher:
    def teach(self):
        print("Teaching in classroom")
        
class Youtube:
    def teach(self):
        print("Teaching online")
        
def learn(source):
    source.teach()

learn(Teacher())
learn(Youtube())