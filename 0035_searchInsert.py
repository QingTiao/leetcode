class Solution:
    def searchInsert(self, nums:[int], target: int) -> int:
        ls=len(nums)
        if target in nums:
            for i in range(ls):
                if nums[i]==target:
                    return i
        if target not in nums:
            for i in range(ls):
                if i<ls-1 and nums[i+1]>target and nums[i]<target:
                    return i+1
                elif nums[ls-1]<target:
                    return ls
                elif nums[0]>target:
                    return 0

if __name__ == '__main__':
        s = Solution()
        print(s.searchInsert([1],2))
