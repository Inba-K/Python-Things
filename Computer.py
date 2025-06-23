class computer:
    def __init__(self):
        self.__max_price=100
    def sell(self):
        print("The selling price is",self.__max_price)
    def changemaxprice(self):
        print("The max price was changed to",self.__max_price-15)
sale=computer()
sale.sell()
sale.changemaxprice()
