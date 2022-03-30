class Solution:
    def containsNearbyDuplicate(self, nums: [int], k: int) -> bool:
        pos = {}
        for i, num in enumerate(nums):
            if num in pos and i - pos[num] <= k:
                return True
            pos[num] = i
        return False

if __name__ == '__main__':
            s = Solution()
            print(s.containsNearbyDuplicate(nums = [1,0,1,1], k = 1))