class Solution:
    def romanToInt(self, s: str) -> int:
        ls=len(s)
        dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        t=0
        for i in range(ls):
            v1=dict.get(s[i])
            if i<ls-1 and v1<dict.get(s[i+1]):


                t-=v1
            else:
                t+=v1
        return t
if __name__ == '__main__':
    s = Solution()
    print( s.romanToInt('MII'))


