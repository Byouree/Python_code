def find_pairs(arr, target):
    n = len(arr)
    arr = sorted(arr)
    print(arr)
    left = 0
    right = n-1
    while(left<=right):
        if arr[left]+arr[right] > target:
            right -= 1

        elif arr[left]+arr[right] < target:
            left += 1
        elif arr[left]+arr[right] == target:
            left +=1
            right -=1
            print(arr[left], arr[right])


arr = [5,7,4,3,9,8,19,21]
sum = 17
find_pairs(arr, sum)
