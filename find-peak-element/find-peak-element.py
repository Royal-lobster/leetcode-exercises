class Solution(object):
    def findPeakElement(self, nums):
        
        # IF ONLY ONE ELEMENT IN ARRAY
        if len(nums) == 1: return 0
        
        # IF FIRST ELEMENT IS GREATER THAN ITS RIGHT
        if nums[0] > nums[1]:
            return 0
        
        # IF LAST ELEMENT IS GREATER THAN ITS LEFT
        if nums[-2] < nums[-1]:
            return len(nums)-1
        
        # IF PEAK ELEMENT IS NOT FOUND YET, SEARCH IN REST
        i = 1
        while i < len(nums):
            if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
                return i
            i += 1
            
           
        