class Solution:
    def average(self, salary:[int]) -> float:
        salary.sort()
        sum=0
        for i in range(1,len(salary)-1):
            sum+=salary[i]
        res=sum/(len(salary)-2)
        return res
if __name__ == '__main__':
            s = Solution()
            print(s.average([4,3,1,2]))