# 一开始的错误代码
# class Solution:
#     def removeDuplicates(self, nums:[int]) -> int:
#         ls=len(nums)
#         for i in range(ls):
#             if i<ls-1 and nums[i]==nums[i+1]:
#                 nums.remove(nums[i+1])
#         return len(nums),nums
#
# if __name__ == '__main__':
#         s = Solution()
#         print(s.removeDuplicates([1,2,2,3,3,4]))
class Solution:
    def removeDuplicates(self, nums:[int]) -> int:
        ls=len(nums)
        fast=slow=1
        while fast<ls:
            if nums[fast]!=nums[fast-1]:
                nums[slow]=nums[fast]
                slow+=1
            fast+=1
        return slow

if __name__ == '__main__':
        s = Solution()
        print(s.removeDuplicates([1,2,2,3,3,4]))