class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n = len(arr)
        if n < 3:
            return 0
        
        index = 0
        
        maxnum = arr[0]
        for i in range(1,n):
            if arr[i] >maxnum:
                maxnum=arr[i]
                index = i
        print(index)
        
        left = 0
        right = n-1
        
        if index == left or index == right:
            return 0
        
        while left < index:
            if arr[left] >= arr[left+1]:
                return 0
            left +=1
        
        while index < right:
            if arr[index] <= arr[index+1]:
                return 0
            index +=1
            
        return 1
    
  #######################################      
        
        class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n = len(arr)
        i = 1
        while i < n and arr[i] > arr[i-1]:
            i+=1
        if i == 1 or i == n:
            return False
        
        while i < n and arr[i] < arr[i-1]:
            i+=1
        
        return i==n
            
            
# T = O(N)
# S = O(1)
            
        
