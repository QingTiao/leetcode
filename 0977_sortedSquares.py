class Solution:
    def sortedSquares(self, nums:[int]) -> [int]:
        res=[]
        for ch in nums:
            res.append(ch*ch)
        res.sort()
        return res

if __name__ == '__main__':
            s = Solution()
            print(s.sortedSquares())