class Solution(object):
    def rotate(self, nums, k):
        def rotate_aux(nums, start, end):
            i,j = start, end
            while i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i, j = i + 1, j - 1
        k = k % len(nums) 
        rotate_aux(nums, len(nums)-k, len(nums)-1)
        rotate_aux(nums, 0, len(nums)-k-1)
        rotate_aux(nums, 0, len(nums)-1)
        