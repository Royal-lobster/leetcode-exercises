class Solution(object):
    def search(self, nums, target):
        for i,x in enumerate(nums):
            if x == target:
                return i
        else:
            return -1