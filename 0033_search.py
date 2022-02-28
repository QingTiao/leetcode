class Solution:
    def search(self, nums: [int], target: int) -> int:
        if target not in nums:
            return -1
        else:
            # x=nums.index(target)
            l=0
            r=len(nums)-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    return mid
                if nums[0]<=nums[mid]:
                    if nums[0]<=target<nums[mid]:
                        r=mid-1
                    else:
                        l=mid+1
                else:
                    if nums[mid]<target<=nums[len(nums)-1]:
                        l=mid+1
                    else:
                        r=mid-1
            return -1


if __name__ == '__main__':
            s = Solution()
            print(s.search([1,3],3))
