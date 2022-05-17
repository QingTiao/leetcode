class Solution:
    def nextGreatestLetter(self, letters:[str], target: str) -> str:
        ls=len(letters)
        b=int(ord(target))
        for ch in letters:
            a=int(ord(ch))
            if a>b:
                return ch
        for ch2 in letters:
            a=int(ord(ch2))+26
            if a>b:
                return ch2



if __name__ == '__main__':
            s = Solution()
            print(s.nextGreatestLetter( letters = ["c", "f", "j"],target = "a"))