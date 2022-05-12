class Solution:
    def findRelativeRanks(self, score: [int]) -> [str]:
        a=[]
        for ch in score:
            a.append(ch)
        res=[]
        score.sort()
        print(a)
        for i in range(len(score)):
            if a[i]==score[-1]:
                res.append('Gold Medal')
            elif a[i]==score[-2]:
                res.append('Silver Medal')
            elif a[i]==score[-3]:
                res.append('Bronze Medal')
            else:
                b=score.index(a[i])
                res.append(str(len(score)-b))
        return res


if __name__ == '__main__':
            s = Solution()
            print(s.findRelativeRanks([1,2,3,4,5,7,6]))