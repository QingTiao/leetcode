class Solution:
    def arrayPairSum(self, nums: [int]) -> int:
        ls=len(nums)
        nums.sort()
        a=0
        for i in range(0,ls,2):
            a+=nums[i]
        return a





if __name__ == '__main__':
            s = Solution()
            print(s.arrayPairSum([0, 0, 1, 0, 0, 1]))