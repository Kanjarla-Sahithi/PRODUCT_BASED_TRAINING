#Overriding or polymorphism
"""overriding means if one class contain a method with some name and same method with same
same name is present in other class then if we call that function then this process is known as overiding """ 
class one:
    def fun1(self):
        print("1fun1")
class two(one):
    def fun1(self):
        print("2fun1")
    def fun2(self):
        print("2fun2")
obj1=one()
obj2=two()
obj2.fun1()


