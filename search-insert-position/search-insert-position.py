class Solution(object):
    def searchInsert(self, nums, target):
        start, end = 0 , len(nums) - 1
        while end >= start:
            mid = start + int((end - start)/2)
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                end = mid - 1
            if nums[mid] < target:
                start = mid + 1
        else:
            if target < nums[mid]:
                return mid
            return mid + 1
        