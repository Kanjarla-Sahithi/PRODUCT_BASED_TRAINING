#bubble sort
#bestcase timecomplexity O(n)
#avgcase timecomplexity and worst case time complexity is O(n^2)
l=list(map(int,input().split()))
for i in range(1,len(l)):
    for j in range(len(l)-i):
        if(l[j]>l[j+1]):
            l[j],l[j+1]=l[j+1],l[j]
print(l)
            

            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
