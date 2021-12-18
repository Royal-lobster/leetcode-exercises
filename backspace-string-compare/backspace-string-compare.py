class Solution(object):
    def backspaceCompare(self, s, t):
        
        # INITALIZE PARSED ARRAY
        parsed = [[],[]]
        
        # PARSE WORDS WITHOUT BACKSPACES
        for i,w in enumerate([s, t]):
            for l in w:
                if l != "#":
                    parsed[i].append(l)
                elif parsed[i]:
                    parsed[i].pop()
        
        # RETURN IF WORDS ARE SAME OR NOT
        return parsed[0] == parsed[1]