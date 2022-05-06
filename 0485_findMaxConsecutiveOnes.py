class Solution:
    def findMaxConsecutiveOnes(self, nums: [int]) -> int:
        nums.append(0)
        ls=len(nums)
        a=b=0
        for i in range(ls):
            if nums[i]==1:
                a+=1
            else:
                if a>=b:
                    b=a
                a=0
        return b


if __name__ == '__main__':
            s = Solution()
            print(s.findMaxConsecutiveOnes([1,1,0,1,0,1,1,1,1,1,0,1]))
