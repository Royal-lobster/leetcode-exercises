class Solution(object): 
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if(numRows == 1):
            return s
        inter_arr = []
        flag = False;
        count = 0
        temp = []
        for i in range(len(s)):
            if(not flag):
                temp.append(s[i])
                count = count + 1
                if(count == numRows or i == len(s)-1):
                    if(i == len(s)-1):
                        for x in range(numRows - len(temp)):
                            temp.append(None)
                    inter_arr.append(temp)
                    if(numRows != 2):
                        flag = True
                    temp = []
                    count = 0
            else:
                if(count != 0 and i == len(s)-1):
                    temp.insert(0, s[i])
                    temp.insert(0, None)
                    count = count + 2
                    for x in range(numRows-count):
                        temp.insert(0, None)
                        count = count + 1
                if(count == 0 and i == len(s)-1):
                    temp.insert(0, None)
                    temp.insert(0, s[i])
                    count = count + 2
                    for x in range(numRows-count):
                        temp.insert(0, None)
                        count = count + 1
                    
                elif(count == 0 and numRows > 3):
                    temp.insert(0, None)
                    temp.insert(0, s[i])
                    count = count + 2
                elif(count==numRows-2 and numRows > 3):
                    temp.insert(0, s[i])
                    temp.insert(0, None)
                    count = count + 2
                elif(numRows == 3):
                    temp.insert(0, None)
                    temp.insert(0, s[i])
                    temp.insert(0, None)
                    count = count + 3
                elif(count<numRows-1):
                    temp.insert(0, s[i])
                    count = count + 1
                if(count>numRows-1):
                    inter_arr.append(temp)
                    flag = False
                    temp = []
                    count = 0
        print(inter_arr)
        final_arr = []
        for x in range(numRows):
            for y in range(len(inter_arr)):
                if inter_arr[y][x] != None:
                    final_arr.append(inter_arr[y][x])
        return "".join(final_arr)