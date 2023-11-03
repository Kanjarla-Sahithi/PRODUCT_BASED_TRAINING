def binarysearch(arr,low,high,target):
    mid=(low+high)//2
    if low>high:
        return
    if arr[mid]>arr[low]:
        for i in range(low,mid+1):
            if arr[i]==target:
                return i
    else:
        for i in range(mid+1,high):
            if arr[i]==target:
                return i 
    
arr=[4,5,6,7,1,2,3]
target=2
low=0
high=len(arr)
print(binarysearch(arr,low,high,target))


        
        
            
        
        
        
    