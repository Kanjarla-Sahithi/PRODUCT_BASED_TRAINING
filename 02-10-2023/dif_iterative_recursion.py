"""n=int(input())
for i in range(1,n):
    print(i)
for i in range(n,1):
    print(i)"""

#The above program is using a for loop i.e iterative and the below one is using recursive
#This is 1 to n
def fun(n):
    if(n<=0):
        return
    fun(n-1)
    print(n)
    
n=int(input())
fun(n)
#This is n to 1
def fun1(n1):
    if(n1<=0):
        return
    print(n1)
    fun1(n1-1)
n1=int(input())
fun1(n1)
