class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence=sentence.split()
        for i in range(len(sentence)):
            if searchWord in sentence[i]:
                if sentence[i][:len(searchWord)]==searchWord:
                    return i+1
        return -1


if __name__ == '__main__':
            s = Solution()
            print(s.isPrefixOfWord("hellohello hellohellohello","ell"))