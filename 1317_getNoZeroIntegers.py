class Solution:
    def getNoZeroIntegers(self, n: int) -> [int]:
        for i in range(1,n):
            j=n-i
            if '0' not in str(i)+str(j):
                return [i,j]
        return []


if __name__ == '__main__':
            s = Solution()
            print(s.getNoZeroIntegers())
