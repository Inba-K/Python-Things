class calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        print("The sum of both numbers is",self.num1+self.num2)
Thing=calculator(5,8)
Thing.add()
