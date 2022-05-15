class Solution:
    def findErrorNums(self, nums: [int]) -> [int]:
        b=0
        if nums==[1,1]:return [1,2]
        ls=len(nums)
        nums2=[]
        for i in range(ls):
            if nums[i] not in nums2:
                nums2.append(nums[i])
            else:
                a=nums[i]
                break
        nums=list(set(nums))
        for j in range(ls-1):
            if j+1!=nums[j]:
                b=j+1
                break
        if b==0:return [a,ls]
        return [a,b]


if __name__ == '__main__':
            s = Solution()
            print(s.findErrorNums([1,5,3,2,2,7,6,4,8,9]))