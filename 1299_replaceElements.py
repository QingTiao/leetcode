class Solution:
    def replaceElements(self, arr: [int]) -> [int]:
        res=[]
        for i in range(len(arr)):
            if i==len(arr)-1:
                res.append(-1)
            else:
                res.append(max(arr[i+1:]))
        return res
if __name__ == '__main__':
            s = Solution()
            print(s.replaceElements(arr = [17,18,5,4,6,1]))

