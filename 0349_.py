class Solution:
    def intersection(self, nums1: [int], nums2: [int]) -> [int]:
        nums1=list(set(nums1))
        nums2=list(set(nums2))
        nums3=[]
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                nums3.append(nums1[i])
        return nums3







if __name__ == '__main__':
            s = Solution()
            print(s.intersection([1,1,1,2,3,4],[1,2]))