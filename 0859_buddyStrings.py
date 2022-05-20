class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        list1=list(s)
        list2=list(goal)
        list3=[]
        nums1=[]
        nums2=[]
        a=0
        for ch in list1:
            list3.append(ch)
        list3=list(set(list3))
        if len(list1)!=len(list2):
            return False
        if list1==list2:
            if len(list1)!=len(list3):
                return True
            else:
                return False
        if list1!=list2:
            for i in range(len(list1)):
                if list1[i]!=list2[i]:
                    nums1.append(list1[i])
                    nums2.append(list2[i])
                    a+=1
                if a==3:
                    return False
        if a!=2:return False
        if nums1[0]==nums2[1] and nums1[1]==nums2[0]:
            return True
        return False




if __name__ == '__main__':
            s = Solution()
            print(s.buddyStrings("acccccb","bccccca"))