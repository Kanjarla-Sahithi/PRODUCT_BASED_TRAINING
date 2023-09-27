def prime(n):
    for i in range(2,n):
        if n%i==0:
            return True
        else:
            return False
num=input("enter a number")
rev=num[::-1]
num1=int(num)
rev1=int(rev)

flag1=prime(num1)
flag2=prime(rev1)

if flag1==False and flag2==False:
    print(num,"is a magic prime number")
else:
    print(num,"is not a magic prime number")
