class Dog:
    
    def __init__(self) -> None:
        self.temperament = "Loyal"

    def bark(self):
        print("Woof! Woof!")

class Labrador(Dog):

    def __init__(self) -> None:
        super().__init__()
        self.temperament = "Gentle"

    def bark(self):
        super().bark()        
        print("Greetings, Good Sir!")

roge = Dog()
roge.bark()


doge = Labrador()
doge.bark()