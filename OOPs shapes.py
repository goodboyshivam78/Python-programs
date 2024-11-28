class shape:
  def area(self):
    pass
  
  def pere(self):
    pass
  
  
class triangle(shape):
  
    
  def __init__(self,a,b,c):
    self.a=a
    self.b=b
    self.c=c
    
  def area(self):
    s= (self.a+self.b+self.c)/2
    a= pow(s*(s-self.a)*(s-self.b)*(s-self.c),0.5)
    print(a)
  def pere(self):
    p = self.a+self.b+self.c
    print(p)
    
class rectangle(shape):
  
      
  def __init__(self,l,b):
    
    self.l=l
    self.b=b
        
  def area(self):
    a=self.l*self.b
    print(a)
        
  def pere(self):
    p=(2*self.l)+(2*self.b)
    print(p)
        
class circle(shape):
      
  def __init__(self,r):
    self.r=r
        
  def area(self):
    a = 3.14*(self.r**2)
    print(a)
        
  def pere(self):
    p=2*3.14*self.r
    print(p)
        
c1=circle(7)
c1.area()
c1.pere()
t1=triangle(3,4,5)
t1.area()
t1.pere()
r1=rectangle(5,4)
r1.area()
r1.pere()
      