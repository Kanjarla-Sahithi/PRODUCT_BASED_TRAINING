"""class n:
    pass
obj=n()
print(obj)"""

"""class n:
    def fun(self): #method
        print("hello")
obj=n() 
obj.fun()"""

"""class n:
    def __init__(self): #constructor
        print("const")
obj=n()"""

"""
class n:
    def fun(self,a): #method
        print("hello ",a)
obj=n() 
obj.fun(4)"""
"""
class n:
    def __init__(self,a): #constructor
        print("const",a)
    def fun(self,a):
        print("hello ",a)
obj=n(3)
#obj.__init__(4)  #if we want to call the constructor
obj.fun(8)"""

class n:
    def __init__(self,a):#constructor
        print("(:")
        self.a=a
    def fun(s,b):
        s.b=b
        print("hello ",s.b)
obj=n(3)
obj.fun(5)



