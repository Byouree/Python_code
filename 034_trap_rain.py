def rain_trap(arr):
    size=len(arr)
    left = [0]*size
    right = [0]*size
    left[0]=arr[0]
    water = 0
    max_so_far_left=arr[0]
    for i in range(size):
        if arr[i]>max_so_far_left:
            max_so_far_left=arr[i]
            left[i] = max_so_far_left
        else:
            left[i] = max_so_far_left

    max_so_far_right=arr[-1]
    for i in range(size-1,-1,-1):
        if arr[i]>max_so_far_right:
            max_so_far_right=arr[i]
            right[i]=max_so_far_right
        else:
            right[i] = max_so_far_right

    for i in range(size):
        water += min(left[i], right[i])-arr[i]


    return water



arr=[1,0,2,0,1,0,3,1,0,2]
print(rain_trap(arr))
