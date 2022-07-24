#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

lenList=lambda l:1+lenList(l.next) if l else 0

def reverseList(h,prev=None,k=-1): # return new head and the next after orginal last
    if not h: # if h is None, return last element to the head
        return prev,h
    _next=h.next
    h.next=prev
    if k==1:
        return h,_next
    return reverseList(_next,h,k-1)
    
def reverseKGroup(l,k):
    p=h=ListNode(0,l)
    length=lenList(p.next)
    while p and p.next and length>=k:
        cur=p.next
        length-=k
        newHead,_next=reverseList(p.next,None,k)
        p.next.next=_next
        p.next=newHead
        p=cur
    return h.next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        return reverseKGroup(head,k)
# @lc code=end

