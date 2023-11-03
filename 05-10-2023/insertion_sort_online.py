def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j] < arr[j-1] and j > 0:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j = j-1
            return arr

arr = [7,-1,0,5,2]

ans = insertion_sort(arr)

print(ans)