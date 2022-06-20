class Solution:
    def countLargestGroup(self, n: int) -> int:
        res=[0]*10000
        a=0
        for num in range(1,n+1):
            if 1<=num<=9:
                res[num]+=1
            elif 10<=num<=99:
                res[num%10+num//10]+=1
            elif 100<=num<=999:
                res[num%10+(num%100)//10+num//100]+=1
            elif 1000<=num<=9999:
                res[num%10+num//1000+(num//100)%10+(num%100)//10]+=1
            elif num==10000:
                res[1]+=1
        return res.count(max(res))




if __name__ == '__main__':
            s = Solution()
            print(s.countLargestGroup(3853))