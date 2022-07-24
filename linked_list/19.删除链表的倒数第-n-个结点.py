#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def lenList(h):
    if not h:
        return 0
    return 1+lenList(h.next)

def findKstNode(h,k):
    if not h:
        return None
    if k<=1:
        return h
    return findKstNode(h.next,k-1)

def removeNthFromEnd(h,n):
    h=ListNode(0,h)
    l=lenList(h)
    k=l-n+1
    prev=findKstNode(h, k-1)
    prev.next=prev.next.next
    return h.next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        return removeNthFromEnd(head, n)
# @lc code=end

