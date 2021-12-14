class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        n=len(people)
        people = sorted(people)
        left = 0
        right = n-1        
        boat = 0
        while left <= right:
            if left == right:
                boat+=1
                break
            if people[left]+people[right] <= limit:
                boat += 1
                left += 1
                right -= 1
            else:
                boat += 1
                right -= 1
        
        return boat
    
                
                
