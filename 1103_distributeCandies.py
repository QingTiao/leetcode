class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> [int]:
        ans=[]
        i=0
        for j in range(num_people):
            ans.append(0)
        while candies>=i+1:
            if i<(num_people):
                ans[i]+=i+1
                i+=1
                candies-=i
            elif i>=(num_people):
                ans[i%num_people]+=i+1
                i+=1
                candies-=i
        if i>=num_people:
            if candies!=0:
                ans[i%num_people]+=candies
        else:
            if candies!=0:
                ans[i]+=candies
        return ans

if __name__ == '__main__':
        s = Solution()
        print(s.distributeCandies(90,4))

