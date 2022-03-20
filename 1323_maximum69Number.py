class Solution:
    def maximum69Number (self, num: int) -> int:
        num=str(num)
        ls=len(num)
        for i in range(ls):
            if i==ls-1 and num[i]==num[ls-1]=='6':
                return int(num)+3
            elif i==ls-1 and num[i]==num[ls-1]=='9':
                return int(num)

            if num[i]=='6':
                return int(num[0:i]+'9'+num[i+1:-1]+num[-1])


if __name__ == '__main__':
            s = Solution()
            print(s.maximum69Number(9996))