"""arr=[1,2,3,4,5,6,7]
k=3
lis=[]
for i in range(k,len(arr)):
    lis.append(arr[i])
for i in range(k):
    lis.append(arr[i])
print(lis)"""


arr=[1,2,3,4,5,6,7]
k=3
lis=arr[:k+1]
del arr[:k+1]
for i in lis:
    arr.append(i)
print(arr)


"""
arr=[2,3,4,5,6]
k=3
for i in range(k):
    arr.insert(0,arr.pop())
print(arr)"""
"""
nums=[2,3,4,5,6]
k=3
n=len(nums)
for i in range(k-1):
    temp=nums[-1]
    for j in range(n-1,0,-1):
        nums[j]=nums[j-1]
    nums[0]=temp
print(nums)"""



    


    