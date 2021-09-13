class Solution(object):
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers)-1
        for x in numbers:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left+1, right+1]
            if sum < target:
                left += 1
            if target < sum:
                right -= 1