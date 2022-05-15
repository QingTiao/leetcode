class Solution:
    def findMaxAverage(self, nums:[int], k: int) -> float:
        ls=len(nums)
        a=b=c=0
        for i in range(k):
            a+=nums[i]
            b=c=a
        for j in range(k,ls):
            a=a+nums[j]-nums[j-k]
            if a>b:
                b=a
        return b/k



if __name__ == '__main__':
            s = Solution()
            print(s.findMaxAverage([1,12,-5,-6,50,3],4))