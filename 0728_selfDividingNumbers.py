class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> [int]:
        res=[]
        a=0
        b=True
        for ch in range(left,right+1):
            ch,a=str(ch),ch
            for i in range(len(ch)):
                c=(ch[i])
                if int(c)==0:
                    b=False
                elif a%int(c)!=0:
                    b=False
            if b:
                res.append(a)
            b=True
        return res


if __name__ == '__main__':
            s = Solution()
            print(s.selfDividingNumbers(left = 1, right = 22))