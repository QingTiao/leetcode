class Solution:
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1
        total = start = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                start = i + 1
        return start

if __name__ == '__main__':
            s = Solution()
            print(s.canCompleteCircuit([5,1,2,3,4],[4,4,1,5,1]))



