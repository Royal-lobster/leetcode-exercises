class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        ans = []
        for i, x in enumerate(nums):
            if i > 0 and x == nums[i-1]:
                continue
            l,r = i+1, len(nums)-1
            while l < r:
                threeSum = x + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    ans.append([x, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return ans
                        