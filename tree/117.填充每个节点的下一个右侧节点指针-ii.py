#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
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
def connect2(root):
    q=[]
    if root:
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
    def connect(self, root: 'Node') -> 'Node':
        connect2(root)
        return root
        
        
# @lc code=end

