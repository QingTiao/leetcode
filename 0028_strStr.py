# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         ls=len(needle)
#         j=0
#         if ls==0:
#             return 0
#         for i in range(ls):
#             a=i
#             while j<ls:
#                 if haystack[a]==needle[j]:
#                     j+=1
#                 a+=1
#
#
#             return ls
#         return -1
#
#
# if __name__ == '__main__':
#         s = Solution()
#         print(s.strStr('hello','lle'))
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ls=len(needle)
        j=0
        if ls==0:
            return 0
        if needle in haystack:

            return haystack.find(needle)
        else:
            return -1


if __name__ == '__main__':
        s = Solution()
        print(s.strStr('hello','lo'))
