#Using three pointer alogorithm
def sort(nums):
    l=0
    i=0
    r=len(nums)-1
    while(i<=r):
        if nums[i]==0:
            nums[i],nums[l]=nums[l],nums[i]
            l+=1
            i+=1
        elif nums[i]==1:
            i+=1
        elif nums[i]==2:
            nums[i],nums[r]=nums[r],nums[i]
            r-=1
    return nums
nums=[2,0,1,0,1,2]
sorted_array=sort(nums)
print(sorted_array)

"""
#using count sort
l=[2,0,1,0,1,2]
count=[0 for i in range(max(l)+1)]
#print(count)
for i in range(len(l)):
    count[l[i]]+=1
#print(count)
for i in range(1,len(count)):
    count[i]+=count[i-1]
#print(count)
res=[0]*len(l)
for i in range(len(l)):
    count[l[i]]-=1
    res[count[l[i]]]=l[i]   
print(res)"""



        