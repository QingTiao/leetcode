class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ls=len(s)
        l=r=res=0
        for i in range(ls):
            if s[i]=='L':
                l+=1
            elif s[i]=='R':
                r+=1
            if l==r:
                res+=1
        return res





if __name__ == '__main__':
            s = Solution()
            print(s.balancedStringSplit("RLRRLLRLRL"))