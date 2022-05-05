class Solution:
    def thirdMax(self, nums: [int]) -> int:
        nums = list(set(nums))
        nums.sort()
        ls=len(nums)
        if ls<3:return nums[-1]
        else:return nums[-3]

if __name__ == '__main__':
            s = Solution()
            print(s.thirdMax([-1,2,3]))