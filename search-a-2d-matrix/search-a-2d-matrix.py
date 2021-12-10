class Solution(object):
    def searchMatrix(self, matrix, target):
        # GET THE ROW IN WHICH TARGET LIES
        row_of_target = None
        for i, r in enumerate(matrix):
            if target < r[0]:
                break
            if target <= r[::-1]:
                row_of_target = r
            
        print(row_of_target)
        # IF NO ROW FOUND
        if row_of_target == None:
            return False
    
        # BINARY SEARCH THE FOUND ROW
        l, r = 0, len(row_of_target)-1
        while(l <= r):
            m = (l + r)//2
            if(row_of_target[m] == target):
                return True
            elif(target < row_of_target[m]):
                r = m - 1
            elif row_of_target[m] < target:
                l = m + 1
        else:
            return False
            
        