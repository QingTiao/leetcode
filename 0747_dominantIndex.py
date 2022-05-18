class Solution:
    def dominantIndex(self, nums: [int]) -> int:
        if len(nums)==1:return 0
        a=[]
        for ch in nums:
            a.append(ch)
        nums.sort()
        if nums[-1]>=2*nums[-2]:
            return a.index(nums[-1])
        else:
            return -1

if __name__ == '__main__':
            s = Solution()
            print(s.dominantIndex([1,2,3,4]))