class Solution:
    def longestCommonPrefix(self, strs:[str]) -> str:
        t=''
        for i in zip(*strs):
            if len(set(i))==1:
                t+=i[0]
            else:
                break
        return t

if __name__ == '__main__':
    s = Solution()
    print( s.longestCommonPrefix(['flower','flow','float']))
