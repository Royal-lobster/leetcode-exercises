class Solution(object):
    def backspaceCompare(self, s, t):
        
        # PARSE WORDS WITHOUT BACKSPACES
        def parse(w):
            temp = []
            for l in w:
                if l != "#":
                    temp.append(l)
                elif temp:
                    temp.pop()
            return temp
        
        # RETURN IF WORDS ARE SAME OR NOT
        return parse(s) == parse(t)