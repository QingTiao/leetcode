class Solution:
    def missingNumber(self, nums: [int]) -> int:
        nums.sort()
        nums.append(0)
        ls=len(nums)
        for i in range(ls):
            if i!=nums[i]:
                return i

if __name__ == '__main__':
                    s = Solution()
                    print(s.missingNumber([0,1]))