class Solution:
    def lastStoneWeight(self, stones:[int]) -> int:
        stones.sort()
        a=0
        for i in range(len(stones)):
            if len(stones)==1:
                return stones[0]
            elif stones==[]:
                return 0
            elif stones[-1]==stones[-2]:
                stones=stones[0:-2]
            elif stones[-1]>stones[-2]:
                a=stones[-1]-stones[-2]
                stones=stones[0:-2]
                stones.append(a)
                stones.sort()

if __name__ == '__main__':
            s = Solution()
            print(s.lastStoneWeight([2,7,4,1,8,1]))