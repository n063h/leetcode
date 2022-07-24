#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def swap(l):
    second=l.next
    if not second:
        return l
    l.next=second.next
    second.next=l
    return second
    
def swapPairs(l):
    p=h=ListNode(0,l)
    while p and p.next:
        p.next=swap(p.next)
        p=p.next.next
    return h.next
    
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        return swapPairs(head)
# @lc code=end

