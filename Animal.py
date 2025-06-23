class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print("This cat's name is",self.name,"and is a",self.age,"year old")
    def make_sound(self):
        print("Cats meow")
class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print("This dog's name is",self.name,"and is a",self.age,"year old")
    def make_sound(self):
        print("Dogs bark")
a=cat("Garfield",4)
b=dog("Gerald",5)
a.info()
a.make_sound()
b.info()
b.make_sound()
