class Solution:
    def checkRecord(self, s: str) -> bool:
        a=[]
        for ch in s:
            a.append(ch)
        if a.count('A')>=2:
            return False
        for i in range(len(a)):
            if i<=len(a)-3:
                if a[i]=='L' and a[i+1]=='L' and a[i+2]=='L':
                    return False
        return True




if __name__ == '__main__':
            s = Solution()
            print(s.checkRecord(s = "PPALLPP"))