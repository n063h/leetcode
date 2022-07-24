#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def mergeTwoLists(l1,l2):
    if not l2:
        return    
    if not l1.next:
        l1.next = l2
        return
    v1,v2 = l1.next.val, l2.val
    if v1>v2:
        l2Next=l2.next
        l2.next=l1.next
        l1.next=l2
        mergeTwoLists(l1.next,l2Next)
    else:
        mergeTwoLists(l1.next,l2)

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 or list2
        if list1.val>list2.val:
            list1,list2=list2,list1
        mergeTwoLists(list1, list2)
        return list1
# @lc code=end

