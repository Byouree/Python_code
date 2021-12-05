def maximum_num(arr):
    n = len(arr)
    max_num=arr[0]

    for i in range(1,n):
        if arr[i] > max_num:
            max_num= arr[i]
    return max_num

def minimum_num(arr):

    return min(arr)

arr = [63,54,98,34,89,42,18]
print(maximum_num(arr))
print(minimum_num(arr))
