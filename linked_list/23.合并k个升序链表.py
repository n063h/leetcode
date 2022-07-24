#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue

def pop(q,k):
    _,_,node=q.get()
    if node.next:
        q.put((node.next.val,k['v'],node.next))
        k['v']+=1
    return node

def mergeKLists(lists):
    k={'v':0}
    q=PriorityQueue()
    for l in lists:
        if not l:
            continue
        q.put((l.val,k['v'], l))
        k['v']+=1
    h=ListNode()
    p=h
    while not q.empty():
        p.next=pop(q,k)
        p=p.next
    return h.next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return mergeKLists(lists)
# @lc code=end

