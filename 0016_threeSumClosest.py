class Solution:
    def threeSumClosest(self, nums: [int], target: int) -> int:
        ls=len(nums)
        nums.sort()
        best=10**7

        def update(cur):
            nonlocal best
            if abs(cur - target) < abs(best - target):
                best = cur

        for i in range(ls):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=ls-1
            while l<r:
                s=nums[i] + nums[l] + nums[r]
                if s==target:
                    return s
                update(s)
                if s<target:
                    l0=l+1
                    while l0<r and nums[l0]==nums[l]:
                        l+=1
                    l=l0
                else:
                    r0=r-1
                    while l<r0 and nums[r0]==nums[r]:
                        r0-=1
                    r=r0

        return best


if __name__ == '__main__':
            s = Solution()
            print(s.threeSumClosest([1,1,1,1], 0))

        # a=2**32
        # if ls==3:return nums[0]+nums[1]+nums[2]
        # b=[]
        #
        # for i in range(ls):
        #     if i<ls-2:
        #         num = nums[i] + nums[i + 1] + nums[i + 2]
        #         d=c=num-target
        #         if c<0:
        #             c=-c
        #
        #         if c<=a:
        #             a=c
        #             e=d
        # return e+target

