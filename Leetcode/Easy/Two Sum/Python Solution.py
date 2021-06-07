class Solution(object):
    def twoSum(self, nums, target):
        dic = {}
        for i, num in enumerate(nums): 
            if num in dic : return [dic[num], i] 
            dic[target - num] = i
​
        