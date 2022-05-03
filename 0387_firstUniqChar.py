class Solution:
    def firstUniqChar(self, s: str) -> int:
        ls=len(s)
        for i in range(ls):
            a=s[:i]+s[i+1:]
            if s[i] not in a:
                return i
        return -1




if __name__ == '__main__':
            s = Solution()
            print(s.firstUniqChar('loveleetcode'))