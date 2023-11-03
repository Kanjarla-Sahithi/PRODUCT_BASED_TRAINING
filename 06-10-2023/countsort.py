l=[5,4,3,5,7,9,2,4,1,8]
count=[0 for i in range(max(l)+1)]
for i in range(len(l)):
    count[l[i]]+=1
for i in range(1,len(count)):
    count[i]+=count[i-1]
#print(count)
res=[0]*len(l)
for i in range(len(l)):
    count[l[i]]-=1
    res[count[l[i]]]=l[i]
    
print(res)
               