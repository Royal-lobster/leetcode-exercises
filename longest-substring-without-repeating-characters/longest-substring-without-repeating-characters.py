class Solution(object):
    def lengthOfLongestSubstring(self, s):
        sub = []
        output = 0
        for x in s:
            if x not in sub:
               sub.append(x)
            else:
                sub = sub[sub.index(x)+1:] + [x]
            if output < len(sub): 
                    output = len(sub)
        return output
                
            
                