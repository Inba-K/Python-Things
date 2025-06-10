class calculator:
    def __init__(self,num1,num2,num3):
        self.num1=num1
        self.num2=num2
        self.num3=num3
    def add(self):
        print("The sum of all 3 numbers is",self.num1+self.num2+self.num3)
Thing=calculator(5,8,9)
Thing.add()
