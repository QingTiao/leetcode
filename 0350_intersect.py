class Solution:
    def intersect(self, nums1: [int], nums2: [int]) -> [int]:
        nums1.sort()
        nums2.sort()
        nums3=[]
        ls1=len(nums1)
        ls2=len(nums2)
        index1=index2=0
        while index1<ls1 and index2<ls2:
            if nums1[index1]<nums2[index2]:
                index1+=1
            elif nums1[index1]>nums2[index2]:
                index2+=1
            else:
                nums3.append(nums1[index1])
                index1+=1
                index2+=1
        return nums3




if __name__ == '__main__':
            s = Solution()
            print(s.intersect([0,2,3,4],[1,2,0]))