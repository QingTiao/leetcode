class Solution:
    def kLengthApart(self, nums: [int], k: int) -> bool:
        a=k+1
        for i in range(len(nums)):
            if nums[i]==1:
                if a<k and i!=0:
                    return False
                a=0
            else:
                a+=1
        return True

if __name__ == '__main__':
        s = Solution()
        print(s.kLengthApart([0,1,0,0,1,0,0,1],2))