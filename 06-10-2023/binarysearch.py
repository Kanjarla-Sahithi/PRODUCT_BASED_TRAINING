def binarysearch(l,si,li,se):
    mid=(si+li)//2
    if si>li:
        return l[mid]
    if se<l[0]:
        return False
    if l[mid]==se:
        return True
    if l[mid]<se:
        return binarysearch(l,mid+1,li,se)
    return binarysearch(l,si,mid-1,se)
    
l=[24,37,49,59,90]
print(binarysearch(l,0,len(l)-1,23))
