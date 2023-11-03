def sum_of_ele(l,low,high):
    if low==high:
        return l[low]
    if low>high:
        return -1
    mid=(low+high)//2
    return sum_of_ele(l,low,mid)+sum_of_ele(l,mid+1,high)

l=[4,7,2,9,7,0]
s=sum_of_ele(l,0,len(l)-1)
print(s)