class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n=str(n)
        n=list(n)
        ji=1
        he=0
        for ch in n:
            ji*=int(ch)
            he+=int(ch)
        return ji-he

if __name__ == '__main__':
            s = Solution()
            print(s.subtractProductAndSum(123))
