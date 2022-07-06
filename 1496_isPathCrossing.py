class Solution:
    def isPathCrossing(self, path: str) -> bool:
        path=list(path)
        res=[0]*(len(path)+1)
        res[0]=[0,0]
        for i in range(len(path)):
            if path[i]=='N':
                res[i+1]=[res[i][0],res[i][1]+1]
            elif path[i]=='S':
                res[i+1]=[res[i][0],res[i][1]-1]
            elif path[i]=='E':
                res[i+1]=[res[i][0]+1,res[i][1]]
            elif path[i]=='W':
                res[i+1]=[res[i][0]-1,res[i][1]]
            if res[i+1] in res[:i+1]:
                return True
        return False




if __name__ == '__main__':
            s = Solution()
            print(s.isPathCrossing())