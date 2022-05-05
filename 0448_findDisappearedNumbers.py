class Solution:
    def findDisappearedNumbers(self, nums: [int]) -> [int]:
        ls=len(nums)
        nums=list(set(nums))
        nums3=[]

        for i in range(1,ls+1):
            if (i not in nums):
                nums3.append(i)
        return nums3



if __name__ == '__main__':
            s = Solution()
            print(s.findDisappearedNumbers([1,1]))
            # [4, 3, 2, 7, 8, 2, 3, 1]