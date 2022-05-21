class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> [str]:
        s1=s1.split()
        s2=s2.split()
        a=[]
        res=[]
        for ch in s1:
            a.append(ch)
        for i in range(len(s1)):
            b=s1[i]
            a.pop(i)
            if b not in a:
                if b not in s2:
                    res.append(b)
            a=[]
            for ch in s1:
                a.append(ch)
        a=[]
        for ch in s2:
            a.append(ch)
        for i in range(len(s2)):
            b=s2[i]
            a.pop(i)
            if b not in a:
                if b not in s1:
                    res.append(b)
            a=[]
            for ch in s2:
                a.append(ch)


        return res




if __name__ == '__main__':
            s = Solution()
            print(s.uncommonFromSentences(s1 = "apple apple", s2 = "banana"))