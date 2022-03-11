class Solution:
    def findContentChildren(self, g: [int], s: [int]) -> int:
        g.sort()
        s.sort()
        ls1=len(g)
        ls2=len(s)
        j=0
        res=0
        for i in range(ls2):
            if g[j]<=s[i]:
                res+=1
                if j==ls1-1:
                    return res
                j+=1

        return res


if __name__ == '__main__':
            s = Solution()
            print(s.findContentChildren([1,2],[1,2,3]))