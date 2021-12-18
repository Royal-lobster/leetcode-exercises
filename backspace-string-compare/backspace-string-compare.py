class Solution(object):
    def backspaceCompare(self, s, t):
        
        # INITALIZE PARSED ARRAY
        parsed_s, parsed_t = [],[]
        
        # PARSE WORD S WITHOUT BACKSPACES
        for i,letter in enumerate(s):
            if letter == "#" and len(parsed_s) != 0:
                parsed_s.pop()
            elif letter != "#":
                parsed_s.append(letter)
        
        # PARSE WORD T WITHOUT BACKSPACES
        for i,letter in enumerate(t):
            if letter == "#" and len(parsed_t) != 0:
                parsed_t.pop()
            elif letter != "#":
                parsed_t.append(letter)
        
        # RETURN IF WORDS ARE SAME OR NOT
        return parsed_s == parsed_t