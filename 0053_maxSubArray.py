class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        t=0
        maxs=[]
        ls=len(nums)
        if ls==1:
            return nums[0]
        if max(nums)<1:
            return max(nums)
        for i in range(ls):
            t+=nums[i]
            if t<0:
                t=0
            else:
                maxs.append(t)
        return max(maxs)
if __name__ == '__main__':
        s = Solution()
        print(s.maxSubArray([-2,-1]))

