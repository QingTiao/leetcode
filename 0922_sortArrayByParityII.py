class Solution:
    def sortArrayByParityII(self, nums: [int]) -> [int]:
        ji=[]
        ou=[]
        res=[]
        j=0
        o=0
        for ch in nums:
            if ch==0:
                ou.append(ch)
            elif ch%2==0:
                ou.append(ch)
            else:
                ji.append(ch)
        for i in range(len(nums)):
            if i==0:
                res.append(ou[o])
                o+=1
            elif i%2==0:
                res.append(ou[o])
                o+=1
            else:
                res.append(ji[j])
                j+=1
        return res
if __name__ == '__main__':
            s = Solution()
            print(s.sortArrayByParityII([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3]))
