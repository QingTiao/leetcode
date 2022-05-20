class Solution:
    def peakIndexInMountainArray(self, arr: [int]) -> int:
        a=max(arr)
        return arr.index(a)

if __name__ == '__main__':
            s = Solution()
            print(s.peakIndexInMountainArray(arr = [24,69,100,99,79,78,67,36,26,19]))