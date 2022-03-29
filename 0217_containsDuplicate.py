class Solution:
    def containsDuplicate(self, nums: [int]) -> bool:
        ls=len(nums)
        nums = list(set(nums))
        ls2=len(nums)
        if ls==ls2:
            return False
        else:
            return True



if __name__ == '__main__':
            s = Solution()
            print(s.containsDuplicate([5, 1, 2, 3, 4]))