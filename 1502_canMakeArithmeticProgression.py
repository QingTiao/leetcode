class Solution:
    def canMakeArithmeticProgression(self, arr: [int]) -> bool:
        arr.sort()
        n=arr[1]-arr[0]
        for i in range(1,len(arr)-1):
            if arr[i+1]-arr[i]!=n:
                return False
        return True

if __name__ == '__main__':
            s = Solution()
            print(s.canMakeArithmeticProgression([1,2,3,-1,3,5,-4,5]))