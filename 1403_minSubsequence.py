class Solution:
    def minSubsequence(self, nums: [int]) -> [int]:
        nums.sort(reverse=True)
        all=sum(nums)
        ls=len(nums)
        if ls==1:return nums
        half=[]
        for i in range(ls):
            if sum(half)>all-sum(half):
                return half
            else:
                half.append(nums[i])
        return nums




if __name__ == '__main__':
            s = Solution()
            print(s.minSubsequence([1,2,3]))