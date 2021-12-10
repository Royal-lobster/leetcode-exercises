class Solution(object):
    def search(self, nums, target):
        
        # INITALIZE LEFT RIGHT POINTERS
        l, r = 0, len(nums)-1
        
        # START BINARY SEARCH
        while l <= r: 
            
            # FIND MIDDLE INDEX
            m = l + (r-l)// 2
            
            # TARGET IS THE MID ELEMENT
            if nums[m] == target:
                return m
            
            # IF MID IS IN LEFT PORTION OF PIVOT
            if nums[l] <= nums[m]:
                if target < nums[m] and nums[l] <= target:
                    r = m - 1 # search right side of mid
                else:
                    l = m + 1 # search left side of mid
                
            # IF MID IS IN RIGHT PORTION OF PIVOT
            else:
                if nums[m] < target and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        
        # IF NO ELMENT FOUND
        return -1                