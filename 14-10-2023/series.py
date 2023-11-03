l=[2,3,0,4,6,3,2,1]
j=1
for i in l:
    print(j,"|","  x   "*i)
    j+=1
print("-----------------------------------------")
print("0 |   0     1     2     3     4     5 ")
print( )
print( )
for i in range (max(l),-1,-1):
    print(i+1,"|","  ",end="")
    for j in l:
        if j>i:
            print("x",end=" ")
        else:
            print(" ",end=" ")
    print()
print("----------------------------")
print("0 |   0 1 2 3 4 5 6 7 ")