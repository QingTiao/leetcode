class Solution:
    def kidsWithCandies(self, candies: [int], extraCandies: int) -> [bool]:
        m=max(candies)
        res=[]
        for candie in candies:
            if candie+extraCandies>=m:
                res.append(True)
            else:
                res.append(False)
        return res


if __name__ == '__main__':
            s = Solution()
            print(s.reformat(s="a0b1c2"))