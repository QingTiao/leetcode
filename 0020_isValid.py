# 第一次的错误思路,未考虑{}[]((((类似和其他多种情况
# class Solution:
#     def isValid(self, s: str) -> bool:
#         ls=len(s)
#         for i in range(ls):
#             a1=s[i] == '(' and s[i + 1] == ')'
#             a2=s[i] == '[' and s[i + 1] == ']'
#             a3=s[i] == '{' and s[i + 1] == '}'
#             if a1 or a2 or a3 or (a1 and a2) or (a1 and a3) or (a2 and a3) or (a1 and a2 and a3):
#                 return True
#             else:
#                 return False
# if __name__ == '__main__':
#     s = Solution()
#     print( s.isValid('()[]{}'))
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = list()  # 创建stack为空列表
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return not stack


if __name__ == '__main__':
    s = Solution()
    print( s.isValid(']['))
