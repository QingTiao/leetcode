class Solution:
    def longestWord(self, words: [str]) -> str:
        words.sort(key=lambda x: (-len(x), x), reverse=True)
        longest = ""
        candidates = {""}
        for word in words:
            if word[:-1] in candidates:
                longest = word
                candidates.add(word)
        return longest

if __name__ == '__main__':
            s = Solution()
            print(s.longestWord(words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]))