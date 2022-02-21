class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        # ls=len(nums)
        # if ls<3:return []
        # if ls==3:
        #     if nums[0]+nums[1]+nums[2]==0:return nums
        #     else:return []
        # list=[]
        # lists=[]
        # for i in range(ls-3):
        #     left=i+1
        #     right=i+2
        #     while left!=ls-1 and right!=ls:
        #         if nums[i]+nums[left]+nums[right]==0 :
        #                 list.append(nums[i])
        #                 list.append(nums[left])
        #                 list.append(nums[right])
        #                 if list not in lists:
        #                     lists.append(list)
        #                 list=[]
        #         right-=1
        #     left+=1
        # return lists



        # nums.sort()
        # ls=len(nums)
        # list=[]
        # lists=[]
        # if ls<3:return []
        # if ls==3:
        #     if nums[0]+nums[1]+nums[2]==0:return nums
        #     else:return []
        # for i in range(ls-2):
        #     left=i+1
        #     right=ls-1
        #     if nums[i]+nums[left]+nums[right]==0:
        #         list.append(nums[i])
        #         list.append(nums[left])
        #         list.append(nums[right])
        #         if list not in lists:
        #             lists.append(list)
        #         list=[]
        #         right-=1
        #     elif nums[i]+nums[left]+nums[right]<0:
        #         left+=1
        #     else:right-=1
        # return lists
        if len(nums) < 3:
            return []

        nums.sort()

        res = []
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue
            target = -nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    res.append([nums[i], nums[left], nums[right]])
                    # 去重
                    while left < right:
                        left = left + 1
                        if nums[left - 1] != nums[left]: break
                    while left < right:
                        right = right - 1
                        if nums[right + 1] != nums[right]: break
                elif s < target:
                    left = left + 1
                else:
                    right = right - 1
        return res
if __name__ == '__main__':
            s = Solution()
            print(s.threeSum([-1,0,1,2,-1]))