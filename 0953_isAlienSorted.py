# class Solution:
#     def isAlienSorted(self, words: [str], order: str) -> bool:
#         ls=len(words)
#         order=list(order)
#         a=[]
#         b=[]
#         for ch in words:
#             if a!=[] and order.index(ch[0]==a[-1]):
#                 if
#
#             else:
#                 a.append(order.index(ch[0]))
#         for ch2 in a:
#             b.append(ch2)
#         b.sort()
#         if a==b:return True
#         return False
class Solution:
    def isAlienSorted(self, words: [str], order: str) -> bool:
        mp = {c: i for i, c in enumerate(order)}
        for i, w in enumerate(words[:-1]):
            j = 0
            while j < len(w):
                if j == len(words[i + 1]) or (a := mp[w[j]] - mp[words[i + 1][j]]) > 0:
                    return False
                elif a < 0:
                    break
                j += 1
        return True
if __name__ == '__main__':
            s = Solution()
            print(s.isAlienSorted(["word","world","row"],"worldabcefghijkmnpqstuvxyz"))