class Solution(object):
    def search(self, nums, target):
        def binarysearch(nums, start, end, target):
            # enter if base condition statisfies
            if end >= start:   
                # caluculate mid value 
                mid = int(start + (end - start) / 2)
                
                # if mid is target return
                if nums[mid] == target :
                    return mid
                
                # if target is less than mid
                if target < nums[mid] :
                    return binarysearch(nums, start, mid - 1, target)
                    
                # if target is more than mid
                if nums[mid] < target :
                    return binarysearch(nums, mid + 1, end, target)
                    
            # if base condition fails return not found
            else:
                return -1
        index = binarysearch(nums, 0, len(nums) - 1, target)
        return index