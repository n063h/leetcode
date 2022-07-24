#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



def partition(p,x):
    low,high =ListNode(),ListNode()
    plow,phigh=low,high
    while p:
        if p.val<x:
            plow.next=p
            plow=p
        else:
            phigh.next=p
            phigh=p
        p=p.next
    phigh.next=None
    plow.next=high.next
    return low.next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        return partition(head, x)
# @lc code=end

