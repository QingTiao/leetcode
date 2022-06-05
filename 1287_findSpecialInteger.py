class Solution:
    def findSpecialInteger(self, arr: [int]) -> int:
        a=len(arr)/4
        for ch in arr:
            if arr.count(ch)>a:
                return ch



if __name__ == '__main__':
            s = Solution()
            print(s.findSpecialInteger(arr = [1,2,2,6,6,6,6,7,10]))
