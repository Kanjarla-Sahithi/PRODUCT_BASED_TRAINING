#sliding window Algorithm            
"""arr=[1,6,4,11]
target=10
i=0
j=0
currsum=arr[0]
while(j<len(arr)):
    if currsum==target:
        print(range(i,j))
        break
    elif currsum>target:
        currsum-=arr[i]
        i+=1
    else:
        j+=1
        currsum+=arr[j]"""
def count_distinct_elements(nums, k):
    distinct_counts = []
    window = {}
    
    for i in range(len(nums)):
        if nums[i] not in window:
            window[nums[i]] = 0
        window[nums[i]] += 1
        
        if i >= k:
            if window[nums[i - k]] == 1:
                del window[nums[i - k]]
            else:
                window[nums[i - k]] -= 1
        
        if i >= k - 1:
            distinct_counts.append(len(window))
    
    return distinct_counts

# Sample Input
nums = list(map(int,input().split(",")))
k = int(input())

# Sample Output
result = count_distinct_elements(nums, k)
s=""
for i in result:
    s+=str(i)
print(",".join(s))
    

        
    
        