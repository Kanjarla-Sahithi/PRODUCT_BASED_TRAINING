#Multiple inheritance
class one:
    def funone(self):
        print("1fun1")
    def fun1(self):
        print("1fun2")
class two:
    def funtwo(self):
        print("2fun1")
    def fun2(self):
        print("2fun2")
class three(one,two): #In multi inheritance the class which is called first that is going to access means here one is going to access
    def funthree(self):
        print("Three")
        
obj1=one()
obj2=two()
obj3=three()
obj3.funone()
obj3.funtwo()
obj3.funthree()