class Solution:
    def largestSumAfterKNegations(self, nums: [int], k: int) -> int:
        nums.sort()
        ls=len(nums)
        for i in range(ls):
            # while k>0:
                if nums[i]<0 and k>0:
                    nums[i]=-nums[i]
                    k-=1
                elif nums[i]>=0 and k>0:
                    if k%2==0:
                        return sum(nums)
                    else:
                        if nums[i]<nums[i-1]:
                            nums[i]=-nums[i]
                        else:
                            nums[i-1]=-nums[i-1]
                        return sum(nums)
        if k%2==1:
            nums.sort()
            nums[0]=-nums[0]
        return sum(nums)

if __name__ == '__main__':
            s = Solution()
            print(s.largestSumAfterKNegations([-4,-2,-3],4))