class Solution:
    def shuffle(self, nums: [int], n: int) -> [int]:
        res=[0]*2*n
        res[0]=nums[0]
        res[1]=nums[n]
        for i in range(2,2*n):
            if i%2==0:
                res[i]=nums[i//2]
            elif i%2==1:
                res[i]=nums[i//2+n]
        return res
if __name__ == '__main__':
            s = Solution()
            print(s.shuffle([2,5,1,3,4,7],3))