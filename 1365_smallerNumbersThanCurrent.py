class Solution:
    def smallerNumbersThanCurrent(self, nums: [int]) -> [int]:
        nums2=[]
        res=[]
        ls=len(nums)
        for num in nums:
            nums2.append(num)
        nums2.sort(reverse=False)
        for num in nums:
            res.append(nums2.index(num))
        return res
if __name__ == '__main__':
        s = Solution()
        print(s.smallerNumbersThanCurrent(nums = [8,1,2,2,3]))

