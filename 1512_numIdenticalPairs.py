class Solution:
    def numIdenticalPairs(self, nums: [int]) -> int:
        res=0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    res+=1
        return res


if __name__ == '__main__':
            s = Solution()
            print(s.numIdenticalPairs(nums = [1,2,3,1,1,3]))