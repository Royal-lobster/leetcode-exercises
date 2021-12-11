class Solution(object):
    def findMin(self, nums):
        
        # INITIALIZE l, r FOR POINTERS AND res TO STORE MINIMUM VALUE 
        l,r,res = 0, len(nums)-1, nums[0]
        
        # START BINARY SEARCH 
        while l <= r:
            m = l + (r-l)//2
            
            # IF m IS IN LEFT SIDE OF PIVOT
            if nums[m] > nums[r]:
                l = m+1 # move to right towards pivot
            
            # IF m IS IN RIGHT SIDE OF PIVOT
            else:
                r = m-1 # move to left towards pivot
            
            # THE m WILL CONVERGE TO SOLUTION SINCE WE ARE GOING TOWARDS IT
            res = min(res, nums[m])  
        return res
