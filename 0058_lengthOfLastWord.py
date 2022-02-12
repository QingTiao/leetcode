class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ls=len(s)
        if ' ' not in s:
            return ls
        else:
            s=s[::-1]
            if s[0]!=' ':
                for i in range(ls):
                    if s[i]==' ':
                        return i
            else:
                s=s.strip()
                if ' ' not in s:
                    return len(s)
                else:
                    for i in range(ls):
                        if s[i]==' ':
                            return i





                # for a in range(ls):
                #     if s[a]==' ':
                #         s.replace(s[a])
                #     else:
                #         for j in range(ls):
                #             if s[j]==' ':
                #                 return j


if __name__ == '__main__':
        s = Solution()
        print(s.lengthOfLastWord('a '))

