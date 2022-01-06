def min_diff_ele(arr):
    arr=sorted(arr)
    size = len(arr)
    min_diff = 9999*999

    for i in range(size-1):
        if arr[i+1]-arr[i] < min_diff:
            min_diff = arr[i+1] - arr[i]

    return min_diff


arr=[5,32,45,3,12,18,25]
print(min_diff_ele(arr))

#######################################################
def min_diff(arr):
    arr = sorted(arr)
    min_diff = arr[1]-arr[0]
    for i in range(1, len(arr)-1):
        if arr[i+1]-arr[i] < min_diff:
            min_diff = arr[i+1]-arr[i]
    return min_diff


arr=[9,32,45,4,12,18,25]
print(min_diff(arr))
