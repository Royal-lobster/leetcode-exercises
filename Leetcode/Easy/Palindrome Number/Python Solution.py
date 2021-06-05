class Solution(object):
    def isPalindrome(self, x):
       return True if(str(x) == str(x)[::-1]) else False