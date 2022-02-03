# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x>=0 and x<=9:
#             return True
#         elif x<0:
#             return False
#         else:
#             x=str(x)
#             n=len(x)
#             a=0
#             for i in range(n//2):
#                 if x[a]!=x[n-1]:
#                     print(a)
#                     return False
#                 n -= 1
#                 a += 1
#         return True
# if __name__ == '__main__':
#     s = Solution()
#     print( s.isPalindrome(13231))
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        n=len(x)
        a=0
        for i in range(n):
            if x[a]==x[n-1]:
                n-=1
                a+=1
            else:return False
        return True
if __name__ == '__main__':
    s = Solution()
    print( s.isPalindrome(13431))