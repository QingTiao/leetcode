class Solution:
    def judgeCircle(self, moves: str) -> bool:
        list1=list(moves)
        u=list1.count('U')
        d=list1.count('D')
        l=list1.count('L')
        r=list1.count('R')
        if u==d and l==r:
            return True
        return False

if __name__ == '__main__':
            s = Solution()
            print(s.judgeCircle(moves = "UUD"))