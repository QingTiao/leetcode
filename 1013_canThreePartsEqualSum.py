class Solution:
    def canThreePartsEqualSum(self, arr: [int]) -> bool:
        if sum(arr)%3==-1 or sum(arr)%3==-2 or sum(arr)%3==1 or sum(arr)%3==2:return False
        if sum(arr)%3!=0:return False
        if list(set(arr))==[0]:return True
        ls=len(arr)
        a=sum(arr)/3
        b=c=d=0
        l=0
        m=0
        r=0
        for i in range(ls):
            if arr==[]:
                return False
            elif l==a and b!=0:
                break
            elif l!=a or l==a==0:
                l+=arr[0]
                b+=1
                arr.remove(arr[0])
        for i in range(ls):
            if arr==[]:
                return False
            if m==a and arr!=[] and c!=0:
                break
            elif (m!=a and arr!=[]) or m==a==0:
                m+=arr[0]
                c+=1
                arr.remove(arr[0])
        for i in range(ls):
            if r==a and arr==[]:
                break
            else:
                r+=arr[0]
                arr.remove(arr[0])
                d+=1
        if l==m==r==a and b+c+d==ls and b!=0 and c!=0 and d!=0:return True


        return False
if __name__ == '__main__':
            s = Solution()
            print(s.canThreePartsEqualSum([10,-10,10,-10,10,-10,10,-10]))