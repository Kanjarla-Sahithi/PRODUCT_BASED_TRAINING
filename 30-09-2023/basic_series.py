"""ip: 4
ot: *
    * *
    * * *
    * * * *"""
n=int(input())
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end=" ")
    print(" ")
#using single loop
for i in range(0,n):
    print("*" * (i+1))
    

    

