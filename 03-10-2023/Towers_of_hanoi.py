#Tower of Hanoi
def toh(n,source,auxilary,destination):
    count=1
    if n==1:
        print(source,"to",destination)
        return 1
    if n>0:
        count+=toh(n-1,source,destination,auxilary)#source to aux with the help of dest      
        print(source,"to",destination)
        count+=toh(n-1,auxilary,source,destination)#aux to dest with the help of source      
    return count
n=int(input())
print(toh(n,'A','B','C'))

        
