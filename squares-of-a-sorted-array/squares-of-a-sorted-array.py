class Solution(object):
    def sortedSquares(self, nums):
        squares = [x**2 for x in nums]
        squares.sort()
        return squares