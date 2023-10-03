"""1-Water 0-Land Tell How many Iland count is present?
If a 1(water) is surrounded by 0(land) in all directions then we say it as Iland."""

l=[[0,1,0,1],[1,1,0,1],[0,0,1,1],[1,0,1,0]]
n=len(l)
"""
for i range(n):
    l.append(list(map(int,input().spilt)))"""
count=0
def fun(l,i,j,n):
    if l[i][j]==0:
        return
    
    if l[i][j]==1:
        l[i][j]=0    
    
    if i>0:
        fun(l,i-1,j,n) #Top
    if i<n-1:
        fun(l,i+1,j,n) #Bottom  
    if j>0:
        fun(l,i,j-1,n) #left
    if j<n-1:
        fun(l,i,j+1,n) #right
        
    
for i in range(n):
    for j in range(n):
        if l[i][j]==1:
            count=count+1
            fun(l,i,j,n)
print(count)
            