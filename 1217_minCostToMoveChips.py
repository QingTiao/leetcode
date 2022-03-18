class Solution:
    def minCostToMoveChips(self, position: [int]) -> int:
        position.sort()
        position.append(position[-1])
        ls=len(position)
        ji=ou=0
        a=b=c=0
        nums=[]
        if len(list(set(position)))==1:
            return 0
        for i in range(ls-1):
            if position[i]==1:
                ji+=1
            elif position[i]%2==0:
                ou+=1
            else:
                ji+=1
        # if ji> 0:
        #     nums.append(ji)
        # if ou> 0:
        #     nums.append(ou)
        # d=position.count(1)
        #
        # for i in range(ls-1):
        #     if position[i]==position[i+1] and position[i]%2==0 and position[i]!=1:
        #         b+=1
        #     elif position[i]==position[i+1] and position[i]%2==1 and position[i]!=1:
        #         c+=1
        #     elif position[i]!=position[i+1]:
        #         if position[i]==1 and ji-d>0:
        #             nums.append(ji-d)
        #
        #         if ou-b>0:
        #             nums.append(ou-b)
        #         if ji-c>0:
        #             nums.append(ji-c)
        return min(ji,ou)





if __name__ == '__main__':
            s = Solution()
            print(s.minCostToMoveChips([10,3,3,1,6,2,1,10,6,6]))