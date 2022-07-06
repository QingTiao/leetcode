class Solution:
    def canBeEqual(self, target: [int], arr: [int]) -> bool:
        target.sort()
        arr.sort()
        if target==arr:
            return True
        return False


if __name__ == '__main__':
            s = Solution()
            print(s.canBeEqual([3,7,9],[3,7,11]))