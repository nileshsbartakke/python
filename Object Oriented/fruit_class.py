class fruit:
    def __init__(self,color,size):
        self.color=color
        self.size=size
    def sayhi(self):
         print(f"Hi.\nI am {self.color} and {self.size}") 
apple=fruit('red','round')
apple.sayhi()

dragon=fruit('Red','ellips')
dragon.sayhi()