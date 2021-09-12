# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while True:
            mid = int(start + (end - start) / 2)
            if isBadVersion(mid):
                end = mid
                if not isBadVersion(mid-1):
                    return mid;
            else:
                start = mid + 1
                
                