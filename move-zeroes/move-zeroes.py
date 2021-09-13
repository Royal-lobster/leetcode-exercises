class Solution(object):
    def moveZeroes(self, nums):
        zeros = []
        for i,x in enumerate(nums):
            if x == 0:
                zeros.append(i)
        zeros.sort(reverse=True)
        for x in zeros:
            nums.pop(x)
            nums.append(0)
                
                