class Solution:
    def arrayRankTransform(self, arr: [int]) -> [int]:
        arr2=[]
        res=[]
        for ch in arr:
            arr2.append(ch)
        arr2=list(set(arr2))
        arr2.sort()
        for ch in arr:
            res.append(arr2.index(ch)+1)
        return res
if __name__ == '__main__':
        s = Solution()
        print(s.arrayRankTransform([8,3,1,4]))
