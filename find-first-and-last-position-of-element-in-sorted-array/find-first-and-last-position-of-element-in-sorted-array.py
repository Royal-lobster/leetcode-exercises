class Solution(object):
    def searchRange(self, nums, target):
       
        # initalize finnal result array and two pointers
        result = []
        start, end = 0, len(nums)-1
        
        # loop over the nums array using binary search approch
        while(start <= end):
            
            # find the mid element of current context 
            mid = start +  (end - start) / 2
            print([start, mid, end])
            
            # found the target area
            if nums[mid] == target:
                
                #find the first occurence
                i = mid - 1
                while(i >= 0 and nums[i] == target):
                    i -= 1
                i += 1
                result.append(i)
                
                # find the last occurence
                while(i <= len(nums)-1 and nums[i] == target):
                    i += 1
                i -= 1
                result.append(i)
                break;
                    
            # the target is right part of the array
            elif nums[mid] < target:
                start = mid + 1
                
            # the target is left part of the array
            elif target < nums[mid]:
                end = mid - 1
                
        # return the result
        if len(result) == 0:
            return [-1, -1]
        return result
            
            