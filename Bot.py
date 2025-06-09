class robot:
    def __init__(self, name, liking):
        self.name=name
        self.liking=liking
    def intro(self):
        print("Hello there! My name is",self.name,"and I like",self.liking)
bot1=robot("Shravan","basketball")
bot1.intro()
bot2=robot("Sriram","video games")
bot2.intro()
