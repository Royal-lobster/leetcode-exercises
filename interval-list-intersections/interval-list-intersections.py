class Solution(object):
    
    def intervalIntersection(self, firstList, secondList):
        if not firstList or not secondList:
            return []
        l = r = 0
        result = []
        while l < len(firstList) and r < len(secondList):
            if firstList[l][0] > secondList[r][1]:
                r += 1
            elif firstList[l][1] < secondList[r][0]:
                l += 1
            else:
                result.append([max(firstList[l][0], secondList[r][0]),
                               min(firstList[l][1], secondList[r][1])])
                if firstList[l][1] > secondList[r][1]:
                    r += 1
                else:
                    l += 1
        return result
                
                
                
                
                
                         