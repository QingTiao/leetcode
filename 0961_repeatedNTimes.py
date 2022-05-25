class Solution:
    def repeatedNTimes(self, nums:[int]) -> int:
        ls=len(nums)
        n=ls/2
        for ch in nums:
            if nums.count(ch)==n:
                return ch


if __name__ == '__main__':
            s = Solution()
            print(s.repeatedNTimes())