class Solution:
    def jump(self, nums: [int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step

if __name__ == '__main__':
            s = Solution()
            print(s.jump([1,2,3]))