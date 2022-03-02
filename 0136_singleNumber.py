# class Solution:
#     def singleNumber(self, nums:[int]) -> int:
#         ls=len(nums)
#         fast=1
#         nums.sort()
#         if ls==1:return nums[0]
#         if nums[0]!=nums[1]:return nums[0]
#         if nums[-1]!=nums[-2]:return nums[-1]
#
#         while fast<ls:
#             if nums[fast]!=nums[fast-1] and nums[fast]!=nums[fast+1]:
#                 return nums[fast]
#             fast+=1
#         return nums[-1]
from functools import reduce
class Solution:
    def singleNumber(self, nums: [int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)







if __name__ == '__main__':
            s = Solution()
            print(s.singleNumber([2,2,1]))
