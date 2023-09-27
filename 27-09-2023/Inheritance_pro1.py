#inheritance- To transfer the data from one class to another class
#Hierachial inheritance-
"""     program2
        /      \
    pro2a       pro2b """
class Program2:
    def gold(warangal):
        print("Parent class-Price 5L")
    def car(warangal):
        print("Parent class-price 3L")
class Pro2a(Program2):
    def bank(warangal):
        print("pro2a-deposited 2L")
class Pro2b(Program2):
    def jewels(warangal):
        print("Pro2b-price 10L")

obj1=Pro2a()
obj1.bank()
obj1.gold()
obj1.car()

obj2=Pro2b()
obj2.jewels()
obj2.gold()
obj2.car()


