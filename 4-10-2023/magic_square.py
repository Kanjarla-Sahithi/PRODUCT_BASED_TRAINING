#before running the code memory is allocated is known as static memory alocation
n=int(input())
sq=[[0]*n for i in range(n)]
num=1
i=n//2
j=n-1
while(num<=(n*n)):
    if i<0 and j==n:
        i=0
        j=n-2
    else:
        if i<0:
            i=n-1
        if j==n:
            j=0
    if sq[i][j]: #means already number is present
        i=i+1
        j=j-2
        continue
    sq[i][j]=num
    num+=1
    i=i-1
    j=j+1
for i in sq:
    print(*i) #To remove the brackets and commas we use '*'

