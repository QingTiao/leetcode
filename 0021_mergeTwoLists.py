# 按数组做的 数组和链表不一样
# class Solution:
#     def mergeTwoLists(self, list1: [], list2: []) :
#         # if list1 == [] and list2 != []:
#         #     return list2
#         # elif list2 == [] and list1 != []:
#         #     return list1
#         # elif list1==list2==[]:
#         #     return []
#         # elif list1[-1]>list2[-1]:
#         #     list3=list2+list1
#         # else:
#             list3=list1+list2
#             list3.sort()
#             return list3
# Definition for singly-linked list.


# class Solution(object):
#     def mergeTwoLists(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def list2link(list_):
    head = ListNode(list_[0])
    p = head
    for i in range(1, len(list_)):
        p.next = ListNode(list_[i])
        p = p.next
    return head



class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

if __name__ == '__main__':
    s = Solution()
    print(s.mergeTwoLists(list2link([1,4,5]),list2link([1,2,3,4,5])))
