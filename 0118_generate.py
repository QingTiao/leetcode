class Solution:
    def generate(self, numRows: int) -> [[int]]:
        if numRows==1:return [[1]]
        if numRows==2:return [[1],[1,1]]
        res=[0]*numRows
        res[0]=[1]
        res[1]=[1,1]
        for i in range(2,numRows):
            res[i]=[0]*(i+1)
            res[i][0]=res[i][-1]=1
            for j in range(1,i):
                res[i][j]=res[i-1][j-1]+res[i-1][j]
        return res
if __name__ == '__main__':
        s = Solution()
        print(s.generate(3))


