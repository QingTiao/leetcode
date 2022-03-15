class Solution:
    def largestPerimeter(self, nums: [int]) -> int:
        ls=len(nums)
        nums.sort(reverse=True)
        for i in range(ls-2):
            if nums[i]<nums[i+1]+nums[i+2]:
                return nums[i]+nums[i+1]+nums[i+2]
        return 0

if __name__ == '__main__':
            s = Solution()
            print(s.largestPerimeter([2,3,3]))



