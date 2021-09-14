class Solution(object):
    def reverseWords(self, s):
        return " ".join(i[::-1] for i in s.split())
            