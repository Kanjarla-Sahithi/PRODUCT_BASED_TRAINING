nums=[2,5,8,10]
nums.sort()
target=15
flag=False
for i in range(len(nums)):
    k=len(nums)-1
    j=i+1
    while j<k:
        if nums[i]+nums[j]+nums[k]==target:
            flag=True
            break
        elif nums[i]+nums[j]+nums[k]<target:
            j+=1
        elif nums[i]+nums[j]+nums[k]>target:
            k-=1
if flag:
    print("True")
else:
    print("False")
    