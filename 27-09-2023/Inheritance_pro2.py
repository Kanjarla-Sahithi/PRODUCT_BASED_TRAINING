#this is the combination of both hierachial and multi inheritance
"""           Program2
             /       \
        pro2a        pro2b
          |
        pro22a
"""
class Program2:
    def gold(warangal):
        print("Parent class-Price 5L")
    def car(warangal):
        print("Parent class-price 3L")
class Pro2a(Program2):
    def bank(warangal):
        print("pro2a-deposited 2L")
class Pro22a(Pro2a):
    def credit(warangal):
        print("pro22a-credited 1L")
class Pro2b(Program2):
    def jewels(warangal):
        print("\nPro2b-price 10L")
        
obj1=Pro22a()
obj1.gold()
obj1.car()
obj1.bank()
obj1.credit()

obj2=Pro2b()
obj2.jewels()
obj2.gold()
obj2.car()


    
