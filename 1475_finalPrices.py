class Solution:
    def finalPrices(self, prices: [int]) -> [int]:
        res=[]
        a=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j]<=prices[i]:
                    res.append(prices[i]-prices[j])
                    a=1
                    break
            if a==0:
                res.append(prices[i])
            a=0
        return res



if __name__ == '__main__':
            s = Solution()
            print(s.finalPrices(prices = [8,4,6,2,3]))