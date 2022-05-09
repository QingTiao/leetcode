class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==0:return False
        if n==-1:return False
        if n==-2:return False
        if n==2:return False
        if n==1:return True
        while n>=3 or n<=-3:
            n=n/3
        if n==1:
            return True
        else:return False



if __name__ == '__main__':
            s = Solution()
            print(s.isPowerOfThree(45))
