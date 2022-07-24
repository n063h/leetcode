#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
lenList=lambda l:1+lenList(l.next) if l else 0
KstListNode=lambda x,k: KstListNode(x.next,k-1) if (k!=1 and x) else x


def rotateRight(l,k):
    if k==0 or not l:
        return l
    length=lenList(l)
    if k>=length:
        k%=length
    h=ListNode(0,l)
    prev=KstListNode(h.next,length-k)
    last=KstListNode(h.next,length)
    last.next=h.next
    h.next=prev.next
    prev.next=None
    return h.next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        return rotateRight(head, k)
        
# @lc code=end

