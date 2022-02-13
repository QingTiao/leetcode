class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        ls=len(digits)
        if digits==[9]:
            return [1,0]
        if  (1 not in digits) and (2 not in digits) and (3 not in digits) and (4 not in digits) and (5 not in digits) and (6 not in digits) and (7 not in digits)and (8 not in digits) and (0 not in digits):
            a=''
            b=[]
            for i in range(ls):
                a+=str(digits[i])
            c=int(a)+1
            d=str(c)
            for i in range(ls+1):
                b.append(int(d[i]))
            return b
        if ls==1:
            a=[]
            a.append(digits[0]+1)
            return a
        else:
            a=''
            b=[]
            for i in range(ls):
                a+=str(digits[i])
            c=int(a)+1
            d=str(c)

            for i in range(ls):
                b.append(int(d[i]))
            return b




if __name__ == '__main__':
            s = Solution()
            print(s.plusOne([8,9,9,9]))