class Speaker:
    def play(self):
        print("playing on speaker")
        
class Phone:
    def play(self):
        print("playing on phone ")
        
def start_music (device):
    device.play()
    
start_music(Speaker())
start_music(Phone())