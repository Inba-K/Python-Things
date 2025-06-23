class shape:
    def __init__(self,length,width):
        self.length=length
        self.width=width
class square(shape):
    def __init__(self,length,width):
        super().__init__(length,width)
    def area(self):
        print("The area of this square is",self.length**2)
    def perimeter(self):
        print("The perimeter of the square is",self.length*4)
class rectangle(shape):
    def __init__(self,length,width):
        super().__init__(length,width)
    def area(self):
        print("The area of the rectangle is",self.length*self.width)
    def perimeter(self):
        print("The perimeter of the rectangle is",2*self.length+2*self.width)
class circle(shape):
    def __init__(self,length,width):
        super().__init__(length,width)
        self.__radius=0.5*length
    def area(self):
        print("The area of the circle is",3.14*self.__radius**2)
    def circumference(self):
        print("The circumference of the circle is",2*3.14*self.__radius)
a=square(5,5)
b=rectangle(7,5)
c=circle(6,6)
a.area()
b.area()
c.area()
a.perimeter()
b.perimeter()
c.circumference()
