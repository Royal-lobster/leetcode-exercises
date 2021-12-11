class Solution(object):
    def findMin(self, nums):
        l, r = 0, len(nums)-1
        
        # IF THE ARRAY IS NOT ROTATED
        if nums[l] <= nums[r]:
            return nums[0]
        
        # IF THE ARRAY IS ROTATED FIND THE PIVOT
        while l <= r:
            m = l + (r-l)//2
            print(nums[m])
            
            # IF WE FOUND PIVOT
            if nums[m] < nums[m-1]:
                return nums[m]
            if l == m:
                return nums[m+1]
            
            # IF m IS IN LEFT PORTION
            if nums[l] < nums[m]:
                l = m
                
            # IF m IS IN RIGHT PORTION
            else:
                r = m
            
        