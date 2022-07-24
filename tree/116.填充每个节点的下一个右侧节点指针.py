#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# 看作三叉树的遍历
def connect1(a,b):
    if not a or not b: return
    c1,c2,c3=(a.left,a.right),(a.right,b.left),(b.left,b.right)
    a.next,b.next = b,None
    connect(*c1)
    connect(*c2)
    connect(*c3)
    
def connect2(root):
    q=[]
    q.append(root)
    while q:
        size=len(q)
        for idx in range(size):
            node=q.pop(0)
            if idx!=size-1:
                node.next=q[0]
            else:
                node.next=None
            if node.left:q.append(node.left)
            if node.right:q.append(node.right)

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        # connect1(root.left,root.right)
        connect2(root)
        return root
            
        
# @lc code=end

