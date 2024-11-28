class circle:
  def __init__(self,r):
    self.r=r
  
  def area(self):
    a= 3.14*(self.r**2)
    return a
  def pere(self):
    p= 2*3.14*self.r
    return p
    
r= int(input("Enter radious of circle: "))
c1=circle(r)
print(c1.area())
print(c1.pere())