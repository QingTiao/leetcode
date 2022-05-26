class Solution:
    def addToArrayForm(self, num: [int], k: int) -> [int]:
        ls=len(num)-1
        a=0
        res=[]
        for ch in num:
            a+=ch*10**ls
            ls-=1
        b=a+k
        b=str(b)
        b=list(b)
        for ch2 in b:
            res.append(int(ch2))
        return res


if __name__ == '__main__':
            s = Solution()
            print(s.addToArrayForm([1,2,0,0],34))