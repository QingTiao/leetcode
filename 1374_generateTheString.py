class Solution:
    def generateTheString(self, n: int) -> str:
        if n==1:return 'a'
        if n%2==0:
            res=['a']*(n-1)
            res.append('b')
            return ''.join(res)
        elif n%2!=0:
            res=['a']*n
            return ''.join(res)
if __name__ == '__main__':
            s = Solution()
            print(s.generateTheString(9))
