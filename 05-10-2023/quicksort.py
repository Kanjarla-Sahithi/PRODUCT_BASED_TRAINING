"""Complexity of function qsorting is n
=> Complexity of function quick depends on the depth of recursion tree
=> The worsr=t case scenario, depth goes till n so O(n^2)
=> Best,Avg -> depth -> logn->O(nlogn)"""
def qsorting(l,start,end):
    pi=l[end]                                                                                                         
    i=start-1 
    for j in range(start,end):
        if l[j]<pi:
            i=i+1
            l[i],l[j]=l[j],l[i]
    l[i+1],l[end]=l[end],l[i+1]
    return i+1
def quick(l,start,end):
    if start<end:
        pi=qsorting(l,start,end)
        quick(l,start,pi-1)
        quick(l,pi+1,end)
        
l=list(map(int,input().split()))
quick(l,0,len(l)-1)
print(l)
