class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ls=len(s)
        if ' '==s:return 1
        if ls==1:return 1
        a=[]
        b=[]
        for i in range(ls):

            for j in range(i,ls):
                if s[j] not in a:
                    a.append(s[j])
                else:
                    if len(a)>len(b):
                        b=a
                    a=[]
                    break
        return len(b)
if __name__ == '__main__':
            s = Solution()
            print(s.lengthOfLongestSubstring('abcacdfg'))