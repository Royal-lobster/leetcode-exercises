class Solution(object):
    def lengthOfLongestSubstring(self, s):
        sub = ''
        output = 0
        for i in s:
            if i in sub:
                sub = sub[sub.index(i) + 1:]
            sub += i
            if len(sub) > output:
                output = len(sub)
        return output