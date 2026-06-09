#OOPS BASICS-Class and objects
class A:
    c=100
    def __init__(self,u=1000,v=2000):
        self.u=u
        self.v=v
    def display(self):
        print("HI",self.u,a.v)
        return A.c+self.u
    
class B:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def displ(self):
        print("hi",self.a)
        return 20

a=A(100,50)
b=B(50,200)
print(a.display()+b.displ())

#Inheritance
class A:
    def __init__(self,a):
        self.u=a
    def asd(self):
        print("Hi")
    def dwer(self):
        print("Hello")
class B(A):
    def __init__(self, a,b):
        super().__init__(a)
        self.v=b
    def displ(self):
        print("Hey ",self.u,self.v)
b=B(10,20)
print(b.displ())

        
