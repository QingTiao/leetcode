class Solution:
    def minimumAbsDifference(self, arr: [int]) -> [[int]]:
        arr.sort()
        a=arr[1]-arr[0]
        res=[[arr[0],arr[1]]]
        for i in range(1,len(arr)-1):
            if arr[i+1]-arr[i]<a:
                res=[[arr[i],arr[i+1]]]
                a=arr[i+1]-arr[i]
            elif arr[i+1]-arr[i]==a:
                res.append([arr[i],arr[i+1]])
        return res


if __name__ == '__main__':
            s = Solution()
            print(s.minimumAbsDifference([40,11,26,27,-20]))