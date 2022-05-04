class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ls=len(ransomNote)
        ls1=len(magazine)
        for i in range(ls):
            if ransomNote[i] in magazine:
                a=magazine.find(ransomNote[i])
                magazine=magazine[:a]+magazine[a+1:]
                ls2=len(magazine)
                if ls1-ls2==ls:
                    return True
        return False





if __name__ == '__main__':
            s = Solution()
            print(s.canConstruct("aa","aab"))