class Solution(object):
    def dominantIndex(self, nums):
        
        # check if nums has less than 1 element
        if len(nums) == 1:
            return 0
        
        # make new sorted array
        sorted = [x for x in nums]
        sorted.sort(reverse=True)
        
        # check if 1st largest element is greater 
        # than twice of 2nd largest element
        if sorted[0] >= 2 * sorted[1]:
            return nums.index(sorted[0])
        else:
            return -1
        