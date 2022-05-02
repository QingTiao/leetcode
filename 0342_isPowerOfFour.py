class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:return True
        if n==4:return True
        if n<=0:return False
        if n<1:n=1/n
        if n>1:
            while n>4:
                n=n/4
            if n==4:
                return True
            else:return False




if __name__ == '__main__':
            s = Solution()
            print(s.isPowerOfFour(17))