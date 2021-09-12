class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged_list = nums1 + nums2
        merged_list.sort()
        length_of_list = len(merged_list)
        mid_number = int(length_of_list/2)
        if (length_of_list % 2 != 0):
             return merged_list[mid_number]
        else:
             return float(merged_list[mid_number]+merged_list[mid_number-1])/2

            