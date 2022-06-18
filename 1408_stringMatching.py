class Solution:
    def stringMatching(self, words: [str]) -> [str]:
        ls=len(words)
        res=[]
        for i in range(ls):
            for j in range(ls):
                if words[i] in words[j] and words[i]!=words[j]:
                    res.append(words[i])
                    break
        return res
if __name__ == '__main__':
        s = Solution()
        print(s.stringMatching(words = ["mass","as","hero","superhero"]))
