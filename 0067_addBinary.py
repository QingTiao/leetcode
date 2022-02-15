class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a=int(a,2)
        b=int(b,2)
        c=str(bin(a+b))

        return c[2:]




if __name__ == '__main__':
            s = Solution()
            print(s.addBinary('1010','1011'))