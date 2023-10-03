#OOPS Concepts
"""
=>This concepts are used for the huge and large amount of data.
=>A class contain object and every object contain data and methods.
=>In class ot oops concepts everything is packed clearly and we can also retrive the data easily.
=>static data can be used by the class but the non static data will not use by the class 
=>Using def keyword inside the class it is method, outside the class it is called as function.
=>for static method no need of object,and we wont use self argument in method.
This is the static method
class cse:
    def meth():
        print("hi")        
cse.meth()

=>Non static variables require objects but static doesnot require the objects
"""

"""
class cse:
    def meth(self):
        print("hi")        
obj=cse()
obj.meth()     #calling only with object and method
cse.meth(obj)  #calling with class,method and object also

#print(obj) # It gives the refernce of the object."""

"""
class cse:
    x=10 #static variable
    def __init__(self):
        self.y=30 #non static variable
    def meth(self):     #Here the use of self is the obj goes to self so we use self.variable so obj.variable it means
        print("Hi",self.y) 
obj=cse()
obj.meth()
print(cse.x,obj.y)"""


class cse:
    x=10 #static variable
    def __init__(self,k):
        self.y=k #non static variable
    def meth(self):     #Here the use of self is the obj goes to self so we use self.variable so obj.variable it means
        print("Hi",self.y) 
obj=cse(80)
obj1=cse(12)
obj.meth()
obj1.meth()






