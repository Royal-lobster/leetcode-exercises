class Solution(object):
    def reverseWords(self, s):
        reversed_list = []
        for word in s.split(" "):
            left, right = 0, len(word)-1
            s = [x for x in word]
            while left <= right:
                s[left], s[right] = s[right], s[left]
                left, right = left+1, right-1
            reversed_list.append("".join(s))
        return " ".join(reversed_list)
            