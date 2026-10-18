class Email:
    def send(self):
        print("send Email")
        
class SMS:
    def send(self):
        print("semd SMS")
        
def notify(service):
    service.send()
    
notify(Email())
notify(SMS())