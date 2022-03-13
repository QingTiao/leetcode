class Solution:
    def diStringMatch(self, s: str) -> [int]:
        ls=len(s)
        res=[]
        nums=[]
        left=0
        right=ls
        for i in range(ls):
            nums.append(i)
        nums.append(ls)
        for i in range(ls):
            if s[i]=='I':
                res.append(nums[0])
                nums.remove(nums[0])
            else:
                res.append(nums[-1])
                nums.remove(nums[-1])

        res.append(nums[0])


        return res



if __name__ == '__main__':
            s = Solution()
            print(s.diStringMatch('III'))