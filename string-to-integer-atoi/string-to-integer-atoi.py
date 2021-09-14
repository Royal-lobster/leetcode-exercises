class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        if(s == "" or s[0].isalpha()):return 0
        try:
            arr = []
            isNumFound = False
            for x in s:
                if not x.isnumeric() and isNumFound : break
                if x in [".", "+", "-"] or x.isnumeric() : 
                    arr.append(x)
                    isNumFound = True
            parsedNum = int(float("".join(arr)))
        except:
            return 0
        return max(-2**31, min(parsedNum,2**31-1))