""" output:
    1
    2 2
    3 3 3
    4 4 4 4 """
n=int(input())
"""for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print(" ")
    
for i in range(0,n):
    print(str(i+1)*(i+1))"""

for i in range(1,n+1):
    print(((10**i)//9)*i)

    

