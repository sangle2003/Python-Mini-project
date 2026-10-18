class Animal:
    def an(self):
        self.type=input("Enter type of animal :: ")

class Cat(Animal):
    def cat(self):
        self.breed=input("Enter Breed :: ")

class Kitten(Cat):
    def kit(self):
        print("Kitten is of type : ", self.type ," and of breed ", self.breed)

k=Kitten()
k.an()
k.cat()
k.kit()