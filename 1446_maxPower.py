class Solution:
    def maxPower(self, s: str) -> int:
        s=list(s)
        s.append('1')
        nums=[]
        for i in range(len(s)):
            if i==0:
                num=1
            elif s[i]!=s[i-1]:
                nums.append(num)
                num=1
            elif s[i]==s[i-1]:
                num+=1
        return max(nums)



if __name__ == '__main__':
            s = Solution()
            print(s.maxPower('l'))