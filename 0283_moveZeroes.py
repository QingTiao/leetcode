class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        ls=len(nums)
        for i in range(ls):
            if nums[i]==0:
                nums.remove(nums[i])
                nums.append(0)
                i-=1

        return nums


if __name__ == '__main__':
                    s = Solution()
                    print(s.moveZeroes([1,2,3,0,4,5,0,0,6,0]))