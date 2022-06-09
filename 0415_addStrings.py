class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ls1=len(num1)
        ls2=len(num2)
        nums1=[]
        nums2=[]
        for i in range(ls1):
            c=int(num1[i])
            nums1.append(c)
        for j in range(ls2):
            d=int(num2[j])
            nums2.append(d)
        a=b=0
        if ls1==5:
            a=nums1[0]*10000+nums1[1]*1000+nums1[2]*100+nums1[3]*10+nums1[4]
        if ls1==4:
            a=nums1[0]*1000+nums1[1]*100+nums1[2]*10+nums1[3]
        if ls1==3:
            a=nums1[0]*100+nums1[1]*10+nums1[2]
        if ls1==2:
            a=nums1[0]*10+nums1[1]
        if ls1==1:
            a=nums1[0]
        if ls2==5:
            b=nums2[0]*10000+nums2[1]*1000+nums2[2]*100+nums2[3]*10+nums2[4]
        if ls2==4:
            b=nums2[0]*1000+nums2[1]*100+nums2[2]*10+nums2[3]
        if ls2==3:
            b=nums2[0]*100+nums2[1]*10+nums2[2]
        if ls2==2:
            b=nums2[0]*10+nums2[1]
        if ls2==1:
            b=nums2[0]
        return str(a+b)



if __name__ == '__main__':
            s = Solution()
            print(s.addStrings(num1 = "456", num2 = "77"))