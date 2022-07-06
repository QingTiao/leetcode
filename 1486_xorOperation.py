class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums=[0]*n
        res=0
        for i in range(n):
            ans ^= (start + i * 2)
        return ans
