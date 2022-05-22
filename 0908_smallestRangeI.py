class Solution:
    def smallestRangeI(self, nums:[int], k: int) -> int:
        l=min(nums)
        r=max(nums)
        if r-l<=2*k:
            return 0
        else:return r-l-2*k







if __name__ == '__main__':
            s = Solution()
            print(s.smallestRangeI(nums = [0,10], k = 2))