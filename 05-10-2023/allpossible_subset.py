def check(arr, target,n,lis):
    if target==0:
        print(lis)
        return
    if n==0 or target<0:
        return
    '''if arr[n-1]>target:
        check(arr, target, n-1,lis)'''
    lis.append(arr[n-1])
    check(arr, target-arr[n-1],n-1,lis)
    lis.pop()
    check(arr, target, n-1,lis)

arr=[3,12,5,4,24,2]
target=9

res=check(arr, target, len(arr),[])

