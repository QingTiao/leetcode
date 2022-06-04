class Solution:
    def checkStraightLine(self, coordinates: [[int]]) -> bool:
        # y=ax+b
        # 4=3a+b
        # 2=a+b
        if coordinates[0][0]==coordinates[1][0]:
            for ch in coordinates:
                if ch[0]!=coordinates[0][0]:
                    return False
            return True
        a=(coordinates[0][1]-coordinates[1][1])/(coordinates[0][0]-coordinates[1][0])
        b=coordinates[0][1]-coordinates[0][0]*a
        for ch in coordinates:
            if ch[1]!=ch[0]*a+b:
                return False
        return True
if __name__ == '__main__':
            s = Solution()
            print(s.checkStraightLine([[2,4],[2,5],[2,8]]))
