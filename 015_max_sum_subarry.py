def max_sum_subarray(arr):
    n = len(arr)
    curr_sum = 0
    max_so_far = arr[0]

    for i in range(n):
        curr_sum+= arr[i]
        if max_so_far < curr_sum:
            max_so_far = curr_sum

        if curr_sum < 0:
            curr_sum = 0
    return max_so_far


arr = [4,-3,-2,2,3,1,-2,-3,6,-6,-4,2,1]
print(max_sum_subarray(arr))


def max_sum_subarray(arr):
    n = len(arr)
    curr_sum = 0
    max_so_far = arr[0]
    st, en, poi=0,0,0

    for i in range(n):
        curr_sum+= arr[i]
        if max_so_far < curr_sum:
            st=poi
            en=i
            max_so_far = curr_sum

        if curr_sum < 0:
            curr_sum = 0
            poi=i+1
    print("st :", st)
    print("end : ", en)
    0
    return max_so_far


arr = [4,-3,-2,2,3,1,-2,-3,6,-6,-4,2,1]
print(max_sum_subarray(arr))
