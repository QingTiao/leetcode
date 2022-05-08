# 我的代码
# class Solution:
#     def bulbSwitch(self, n: int) -> int:
#         if n==0:return 0
#         if n==1:return 1
#         nums=[]
#         for i in range(n):
#             nums.append(1)
#         for i in range(2,n):
#             for j in range(n):
#                 if (j+1)%i==0 and (j+1)>=i:
#                     if nums[j]==1:
#                         nums[j]=0
#                     else:
#                         nums[j]=1
#         if nums[-1] == 1:
#             nums[-1] = 0
#         else:
#             nums[-1] = 1
#         return nums.count(1)
import math
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(pow(n + 0.5,0.5))




if __name__ == '__main__':
            s = Solution()
            print(s.bulbSwitch(16))
