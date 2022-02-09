class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        ls=len(nums)
        fast=slow=0
        while fast<ls:
            if nums[fast]!=val:
                nums[slow]=nums[fast]
                slow+=1
            fast+=1
        return slow


if __name__ == '__main__':
        s = Solution()
        print(s.removeElement([1,2,2,2,2,2,3,3,4],2))

