class Solution:
    def busyStudent(self, startTime: [int], endTime: [int], queryTime: int) -> int:
        res=0
        for i in range(len(startTime)):
            if startTime[i]<=queryTime<=endTime[i]:
                res+=1
        return res


if __name__ == '__main__':
            s = Solution()
            print(s.busyStudent('l'))