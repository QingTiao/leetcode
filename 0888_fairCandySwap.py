class Solution:
    def fairCandySwap(self, aliceSizes: [int], bobSizes: [int]) -> [int]:
        ls1=len(aliceSizes)
        ls2=len(bobSizes)
        sum1=sum2=0
        aliceSizes.sort()
        bobSizes.sort()
        for j in range(ls1):
            sum1 += aliceSizes[j]
        for n in range(ls2):
            sum2 += bobSizes[n]
        for i in range(ls1):
            l = 0
            r = ls2 - 1
            while l<=r:
                mid = (l + r) // 2
                if sum1-aliceSizes[i]+bobSizes[mid]==sum2+aliceSizes[i]-bobSizes[mid]:
                    return [aliceSizes[i],bobSizes[mid]]
                elif sum1-aliceSizes[i]+bobSizes[mid]<sum2+aliceSizes[i]-bobSizes[mid]:
                    l=mid+1
                else:
                    r=mid-1
if __name__ == '__main__':
            s = Solution()
            print(s.fairCandySwap([1,2,5],[2,4]))


