class Solution:
    def getRow(self, rowIndex: int) -> [int]:
        if rowIndex==0:return [1]
        if rowIndex==1:return [1,1]
        res=[0]*(rowIndex+1)
        res[0]=[1]
        res[1]=[1,1]
        for i in range(2,rowIndex+1):
            res[i]=[0]*(i+1)
            res[i][0]=res[i][-1]=1
            for j in range(1,i):
                res[i][j]=res[i-1][j-1]+res[i-1][j]
        return res[-1]
if __name__ == '__main__':
        s = Solution()
        print(s.getRow(3))