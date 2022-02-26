class Solution:
    def arrangeCoins(self, n: int) -> int:
        l=1
        r=n
        if n==1:return 1
        while l<=r:
            mid=(l+r)//2
            if n-mid-1<(mid+1)/2*mid<=n:
                return mid
            elif (mid+1)/2*mid<=n-mid-1:
                l=mid+1
            else:
                r=mid-1



if __name__ == '__main__':
            s = Solution()
            print(s.arrangeCoins(10))