class Solution:
    def isMonotonic(self, nums: [int]) -> bool:
        a=[]
        for ch in nums:
            a.append(ch)
        nums.sort()
        if nums==a:
            return True
        nums.sort(reverse=True)
        if nums==a:
            return True
        return False



if __name__ == '__main__':
            s = Solution()
            print(s.isMonotonic([1,2,2,3]))