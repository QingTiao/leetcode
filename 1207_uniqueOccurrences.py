class Solution:
    def uniqueOccurrences(self, arr: [int]) -> bool:
        a=[]
        for ch in arr:
            a.append(ch)
        a=list(set(a))
        nums=[]
        for ch in a:
            nums.append(arr.count(ch))
        nums2=[]
        for ch in nums:
            nums2.append(ch)
        nums2=list(set(nums2))
        return len(nums)==len(nums2)
if __name__ == '__main__':
            s = Solution()
            print(s.uniqueOccurrences([1,2,2,1,1,3]))