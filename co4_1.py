class rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        return (self.length*self.breadth)
    def perimeter(self):
        return 2*(self.length+self.breadth)
rectangle1=rectangle(10,20)
rectangle2=rectangle(30,40)
print("area of first rectangle=",rectangle1.area())
print("area of second rectangle=",rectangle2.area())

print("perimeter of first rectangle=",rectangle1.perimeter())
print("perimeter of second rectangle=",rectangle2.perimeter())
