class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ls1=len(jewels)
        ls2=len(stones)
        list1=list(jewels)
        list2=list(stones)
        res=0
        for i in range(ls1):
            res+=list2.count(list1[i])
        return res

if __name__ == '__main__':
            s = Solution()
            print(s.numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))