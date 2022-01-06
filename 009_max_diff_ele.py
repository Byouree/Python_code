def max_diff_ele(arr):
    arr = sorted(arr)
    size = len(arr)
    max_diff = -999*999

    for i in range(size-1):
        if arr[i+1]-arr[i] > max_diff:
            max_diff = arr[i+1]-arr[i]
        print(max_diff)
    return max_diff


arr=[5,32,45,4,12,18,25]
print(max_diff_ele(arr))


######################################
def max_diff(arr):
    arr = sorted(arr)
    max_diff = arr[1]-arr[0]
    for i in range(1, len(arr)-1):
        if arr[i+1]-arr[i] > max_diff:
            max_diff = arr[i+1]-arr[i]
    return max_diff


arr=[5,40,45,4,12,18,25]
print(max_diff(arr))
