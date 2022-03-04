# class Solution:
#     def findTheDistanceValue(self, arr1: [int], arr2: [int], d: int) -> int:
#         ls=len(arr1)
#         ls2=len(arr2)
#         arr2.sort()
#         res=0
#         for i in range(ls):
#             for j in range(ls2):
#                 if -d<=arr1[i]-arr2[j]<=d:
#                     break
#                 res+=1
#         return res

class Solution:
    def findTheDistanceValue(self, arr1: [int], arr2: [int], d: int) -> int:
        cnt = 0
        for x in arr1:
            if all(abs(x - y) > d for y in arr2):
                cnt += 1
        return cnt



if __name__ == '__main__':
                    s = Solution()
                    print(s.findTheDistanceValue([4,5,8],[10,9,1,8],2))