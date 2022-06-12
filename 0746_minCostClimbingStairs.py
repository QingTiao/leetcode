class Solution:
    def minCostClimbingStairs(self, cost: [int]) -> int:
        if len(cost)==2:
            return min(cost)
        dp=[0]*(len(cost)+1)
        for i in range(2,len(cost)+1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[len(cost)]
if __name__ == '__main__':
        s = Solution()
        print(s.minCostClimbingStairs([4,10,1,3,4]))