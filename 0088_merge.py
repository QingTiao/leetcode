class Solution:
    def merge(self, nums1:[int], m: int, nums2:[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 这是我写的  应该是地址改变了  所以不行
        # nums1=nums1[:m]+nums2
        # nums1.sort()

        # 这是答案
        nums1[m:] = nums2
        nums1.sort()

if __name__ == '__main__':
            s = Solution()
            print(s.merge([1,2,3,0,0,0],3,[2,5,6],3))
