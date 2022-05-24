class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        s=list(s)
        r=len(s)-1
        l=0
        while l<=r:
            if s[l] not in a:
                l+=1
            elif s[r] not in a:
                r-=1
            elif s[l] in a and s[r] in a:
                s[l],s[r]=s[r],s[l]
                l+=1
                r-=1
        res=''
        for ch in s:
            res+=ch
        return res


if __name__ == '__main__':
            s = Solution()
            print(s.reverseOnlyLetters("a-bC-dEf-ghIj"))