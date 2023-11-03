"""x=4
def binarysearch(x):
    if x==0:
        return 0
    first=1
    last=x
    while first<=last:
        mid=first+(last-first)//2
        if mid==x//mid:
            return mid
        elif mid>x//mid:
            last=mid-1
        else:
            first=mid+1
    return last
print(binarysearch(x))"""

"""
n=int(input())
si=0
li=n//2
floor=-1
while si<=li:
    mid=(si+li)//2
    sq=mid*mid
    if sq==n:
        floor=mid
        break
    elif sq<n:
        floor=mid
        si=mid+1
    else:
        li=mid-1
print(floor)
"""


        
        
        
