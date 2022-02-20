class Solution:
    def maxArea(self, height: [int]) -> int:
        ls=len(height)
        left=0
        right=ls-1
        nums=[]
        while left!=right:
            num=min(height[left],height[right])*(right-left)
            nums.append(num)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max(nums)




if __name__ == '__main__':
            s = Solution()
            print(s.maxArea([2,3,4,5,18,17,6]))