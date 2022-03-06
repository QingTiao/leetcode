class Solution:
    def canJump(self, nums:[int]) -> bool:
        ls=len(nums)
        maxs=0
        for i in range(ls):
            if i<=maxs:
                maxs=max(maxs,i+nums[i])
                if maxs>=ls-1:
                    return True
        return False

if __name__ == '__main__':
                    s = Solution()
                    print(s.canJump([4,5,8]))


