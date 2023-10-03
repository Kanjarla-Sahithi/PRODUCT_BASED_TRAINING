"""ip:4
op:    *
     *   *
    *  *  *
   *  *  *  * 
n=int(input())
for i in range(0,n):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    print()"""
n=int(input())   
for i in range(0,n):
    print(" "*(n-i) + "* " *(i+1))

    

