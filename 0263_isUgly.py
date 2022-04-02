class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0:return False
        a=[2,3,5]
        for i in a:
            while n%i==0:
                n=n//i
        return n==1
if __name__ == '__main__':
            s = Solution()
            print(s.isUgly(21))