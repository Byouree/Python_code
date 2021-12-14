def moveZeroes(nums):
    n = len(nums)
    prev = 0
    for i in range(n):
        if nums[i] != 0:
            nums[prev] = nums[i]
            prev += 1
    for i in range(prev,n):
        nums[i] = 0
    
    print(nums)



nums = [0,1,0,3,12]
moveZeroes(nums)
