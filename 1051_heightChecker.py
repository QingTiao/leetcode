class Solution:
    def heightChecker(self, heights: [int]) -> int:
        a=[]
        res=0
        for ch in heights:
            a.append(ch)
        heights.sort()
        for i in range(len(a)):
            if a[i]!=heights[i]:
                res+=1
        return res



if __name__ == '__main__':
            s = Solution()
            print(s.heightChecker())