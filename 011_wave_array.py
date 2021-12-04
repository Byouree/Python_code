def wave_arr(arr):
    size = len(arr)
    for i in range(0, size, 2):
        if i > 0 and arr[i-1] > arr[i] :
            arr[i-1], arr[i] = arr[i], arr[i-1]

        if i < size-1 and arr[i] < arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr



arr = [3,5,12,2,6,10,7,9,8]
print(wave_arr(arr))
