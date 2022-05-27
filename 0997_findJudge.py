class Solution:
    def findJudge(self, n: int, trust: [[int]]) -> int:
        a=0
        b=[]
        for i in range(1,n+1):
            for ch in trust:
                if i == ch[1]:
                    a+=1
            if a==n-1:
                for ch2 in trust:
                    b.append(ch2[0])
                if i not in b:
                    return i
            a=0
        return -1
if __name__ == '__main__':
            s = Solution()
            print(s.findJudge(3,[[1,3],[2,3],[3,1]]))
#         a=[]
#         b=[]
#         nums=[]
#         for ch in trust:
#             a.append(ch[0])
#             b.append(ch[1])
#         for i in range(1,n+1):
#             nums.append(i)
#         a=list(set(a))
#         b=list(set(b))
#
#         if (a==nums and len(b)==1):
#             return b[0]
#         return -1
#
#
#
#
# if __name__ == '__main__':
#             s = Solution()
#             print(s.findJudge(n = 2, trust = [[1,2]]))