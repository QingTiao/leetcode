class Solution:
    def nextGreaterElement(self, nums1: [int], nums2: [int]) -> [int]:
        ls=len(nums1)
        ls2=len(nums2)
        nums4=[]
        for i in range(ls):
            b=0
            a=nums2.index(nums1[i])
            nums3=nums2[a+1:ls2]
            ls3=len(nums3)
            for j in range(ls3):
                if nums3[j]>nums1[i]:
                    nums4.append(nums3[j])
                    b=1
                    break
            if b==0:
                nums4.append(-1)

        return nums4


if __name__ == '__main__':
            s = Solution()
            print(s.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))
