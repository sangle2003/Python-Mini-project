class Demo:
    def dispaly(self,a=None,b = None):
        if b:
            print(a,b)
        else:
            print(a)
            
d = Demo()
d.dispaly("Hello")
d.dispaly("Hello","world")