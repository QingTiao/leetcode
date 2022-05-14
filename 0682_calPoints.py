
class Solution:
    def calPoints(self, ops: [str]) -> int:
        ans = 0
        points = []
        for op in ops:
            if op == '+':
                pt = points[-1] + points[-2]
            elif op == 'D':
                pt = points[-1] * 2
            elif op == 'C':
                ans -= points.pop()
                continue
            else:
                pt = int(op)
            ans += pt
            points.append(pt)
        return ans


if __name__ == '__main__':
            s = Solution()
            print(s.calPoints(["5","2","C","D","+"]))
