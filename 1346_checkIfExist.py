class Solution:
    def checkIfExist(self, arr: [int]) -> bool:
        ls=len(arr)
        arr.sort()
        if arr.count(0)>1:return True
        for i in range(ls):
            l=0
            r=ls-1
            while l<=r:
                mid=(l+r)//2
                if arr[mid]==arr[i]*2 and arr[mid]!=0:
                    return True
                elif arr[mid]<arr[i]*2:
                    l=mid+1
                else:
                    r=mid-1
        return False

if __name__ == '__main__':
                    s = Solution()
                    print(s.checkIfExist([10,2,5,3]))