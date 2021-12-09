def binarySearch(arr, target):
    n = len(arr)
    left = 0
    right = n-1

    while(left<=right):
        mid = (left+right)//2
        if arr[mid]== target:
            return mid

        if arr[mid] > target:
            right = mid

        else:
            arr[mid] < target
            left = mid+1


arr = [1, 2, 3, 4, 5, 6]
target = 1

result = binarySearch(arr, target)
print("index : ", result)

