class Solution:
    def sortArrayByParity(self, nums: [int]) -> [int]:
        a=[]
        b=[]
        for ch in nums:
            if ch==0:
                a.append(ch)
            elif ch%2==0:
                a.append(ch)
            else:
                b.append(ch)
        return a+b



if __name__ == '__main__':
            s = Solution()
            print(s.sortArrayByParity([1,2,2,3]))