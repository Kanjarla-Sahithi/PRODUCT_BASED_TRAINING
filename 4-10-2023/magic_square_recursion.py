def magic_square(n):
    sq=[[0]*n for i in range(n)]
    def fill(i,j,num):
        if num>(n*n):
            return sq
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
            return fill(i,j,num)
        sq[i][j]=num
        return fill(i-1, j+1, num+1)
    return fill(n//2, n-1, 1)

n=int(input())
while(n%2==0):
    print("Give an odd number only")
    n=int(input())
for i in magic_square(n):
    print(*i)
    