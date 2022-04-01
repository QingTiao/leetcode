class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            sum = 0
            while num:
                sum += num % 10
                num //= 10
            num = sum
        return num


if __name__ == '__main__':
            s = Solution()
            print(s.addDigits(21))