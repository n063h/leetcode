#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


removeSame=lambda l,val: removeSame(l.next,val) if l and l.val==val else l
    
def deleteDuplicates(l):
    h=ListNode(0,l)
    p=h
    while p:
        first=p.next
        if first and first.next and first.val==first.next.val:
            p.next=removeSame(first,first.val)
        else:
            p=p.next
    return h.next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        return deleteDuplicates(head)
# @lc code=end

