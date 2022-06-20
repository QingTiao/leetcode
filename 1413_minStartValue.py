class Solution:
    def minStartValue(self, nums:[int]) -> int:
        for i in range(1,len(nums)):

            if 0<i<len(nums):
                nums[i]=nums[i-1]+nums[i]
            elif i==len(nums):
                nums[i]=sum(nums)
        if min(nums)>=1:
            return 1
        return abs(min(nums))+1
        # for a in range(1,100000):
        #     if all((a+num)>=1 for num in nums):
        #         return a

if __name__ == '__main__':
            s = Solution()
            print(s.minStartValue(nums = [-3,2,-3,4,2]))