def max_element(l,low,high):
    if low==high:
        return l[low]
    mid=(low+high)//2   
    return max(max_element(l,low,mid),max_element(l,mid+1,high))

l=[240,37,490,59,900]
m=max_element(l,0,len(l)-1)
print(m)
