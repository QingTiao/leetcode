class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ls=len(s)
        ls2=len(t)
        for i in range(ls):
            if s[i] in t:
                for j in range(ls2):
                    if s[i]==t[j]:
                        t=t[:j]+t[j+1:]
                        ls2=len(t)
                        break
            elif s[i] not in t:
                return s[i]
        return t



if __name__ == '__main__':
            s = Solution()
            print(s.findTheDifference(s = "abcd", t = "abcde"))