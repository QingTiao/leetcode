class Solution:
    def tribonacci(self, n: int) -> int:
        a=[]
        if n==0:return 0
        if n==1:return 1
        if n==2:return 1
        for i in range(n+1):
            a.append(0)
        a[0]=0
        a[1]=1
        a[2]=1
        for j in range(3,n+1):
            a[j]=a[j-1]+a[j-2]+a[j-3]
        return a[-1]


if __name__ == '__main__':
            s = Solution()
            print(s.tribonacci(25))