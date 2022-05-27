from collections import Counter

class Solution:
    def commonChars(self, words: [str]) -> [str]:
        res = None
        for a in words:
            c = Counter(a)
            if res is None:
                res = c
            else:
                res &= c
        return list(res.elements())


if __name__ == '__main__':
            s = Solution()
            print(s.commonChars(words = ["bella","label","roller"]))