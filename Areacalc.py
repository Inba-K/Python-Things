class shape:
    def __init__(self,length,width):
        self.length=length
        self.width=width

class square(shape):
    def __init__(self,length,width):
        super().__init__(length,width)
    def area(self):
        print("The area of a square is",self.length**2)
    def perimeter(self):
        print("The perimeter of a square is",self.length*4)


class rectangle(shape):
    def __init__(self,length,width):
        super().__init__(length,width)
    def area(self):
        print("The area of a rectangle is", self.length*self.width)
    def perimeter(self):
        print("The perimeter of a rectangle is",2*self.length+2*self.width)

class triangle(shape):
    def __init__(self,length,width,a,b):
        self.a=a
        self.b=b
        super().__init__(length,width)
    def area(self):
        print("The area of this triangle is",0.5*self.length*self.width)
    def perimeter(self):
        print("The perimeter of a triangle is",self.length+self.a+self.b)
c=square(5,5)
c.area()
c.perimeter()
d=rectangle(12,7)
d.area()
d.perimeter()
e=triangle(8,5,8,8)
e.area()
e.perimeter()
