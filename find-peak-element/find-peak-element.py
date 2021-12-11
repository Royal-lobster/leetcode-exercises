class Solution(object):
    def findPeakElement(self, nums):
        
        # INITIALIZE LEFT RIGHT POINTERS
        l, r = 0, len(nums)-1
        
        # START BINARY SEARCH
        while l < r:
            m = l + (r-l)//2
            
            # IF THE MID IS LOWER THAN ITS RIGHT ELEMENT
            if(nums[m] < nums[m+1]):
                l = m + 1 # search for the peak at right
            
            # IF THE MID IS GREATER THAN ITS RIGHT ELEMENT
            else:
                r = m # search for the peak at left
        
        # EVENTUALLY l == m == r
        return l
                
        