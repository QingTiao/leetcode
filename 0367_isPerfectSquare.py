class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l=1
        r=num
        if num==1:return True
        while l<=r:
            mid=(l+r)//2
            if mid*mid==num:
                return True
            elif mid*mid<num:
                l=mid+1
            else:
                r=mid-1
        return False




if __name__ == '__main__':
            s = Solution()
            print(s.isPerfectSquare(104976))