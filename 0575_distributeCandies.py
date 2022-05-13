class Solution:
    def distributeCandies(self, candyType:[int]) -> int:
        ls1=len(candyType)
        candyType=list(set(candyType))
        ls2=len(candyType)
        ls3=ls1//2
        if ls3>=ls2:return ls2
        elif ls3<ls2:return ls3


if __name__ == '__main__':
            s = Solution()
            print(s.distributeCandies([1,1,1,1,1,2,3]))