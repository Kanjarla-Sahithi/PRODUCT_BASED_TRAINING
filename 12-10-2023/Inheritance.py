"""class one:
    def fun1(self):
        print("1fun1")
    def fun2(self):
        print("1fun2")
class two:
    def fun1(self):
        one.fun1(self)
        print("2fun1")
    def fun2(self):
        print("2fun2")
obj1=one()
obj2=two()
obj2.fun1()"""

class one:
    def fun11(self):
        print("1fun1")
    def fun21(self):
        print("1fun2")
class two(one): #when we call other class then those methods can call through this class object
    def fun12(self):
        one.fun11(self)
        print("2fun1")
    def fun22(self):
        print("2fun2")
obj1=one()
obj2=two()
obj2.fun21()
obj2.fun12()


