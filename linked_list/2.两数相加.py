#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
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

def addFunc(num):
    k={'val':num}
    def addon(h,val):
        h.val+=k['val']+val
        if h.val>=10:
            h.val-=10
            k['val']=1
        else:
            k['val']=0
        if k['val']>0 and h.next is None:
            h.next=ListNode(0)
        return k['val']
    return addon

def addTwoNumbers(l1, l2):
    if lenList(l1)<lenList(l2):
        l1,l2=l2,l1
    p1,p2=l1,l2
    addon=addFunc(0)
    while p2:
        addon(p1,p2.val)
        p1,p2=p1.next,p2.next
    while p1 and addon(p1,0)>0:
        p1=p1.next
    return l1

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return addTwoNumbers(l1, l2)
# @lc code=end

