class NeonNum:
    def neon(self,num):
        sq=num*num
        s=0
        while sq>0:
            s=s+sq%10
            sq=sq//10
        if(num==s):
            print("Neon Number")
        else:
            print("Not a Neon Number")
            
num = int(input("Enter a number:"))
obj=NeonNum()
obj.neon(num)
