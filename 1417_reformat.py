class Solution:
    def reformat(self, s: str) -> str:
        nums='0123456789'
        s=list(s)
        sz=[]
        zm=[]
        res=''
        for i in s:
            if i in nums:
                sz.append(i)
            else:
                zm.append(i)
        if abs(len(sz)-len(zm))>1:
            return ''
        elif len(sz)>len(zm):
            for i in range(len(zm)):
                res+=sz[i]
                res+=zm[i]
            res+=sz[-1]
        elif len(sz)<len(zm):
            for i in range(len(sz)):
                res+=zm[i]
                res+=sz[i]
            res+=zm[-1]
        elif len(sz)==len(zm):
            for i in range(len(sz)):
                res+=zm[i]
                res+=sz[i]
        return res
if __name__ == '__main__':
            s = Solution()
            print(s.reformat(s = "a0b1c2"))
