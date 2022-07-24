#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def preorderTraversal1(root):
    if not root:
        return []
    l,r=preorderTraversal1(root.left),preorderTraversal1(root.right)
    return [root.val,*l,*r]
    
def preorderTraversal2(root):
    s,res=[],[]
    if root:
        s.append(root)
    while s:
        node=s.pop()
        if not node:
            continue
        res.append(node.val)
        s.append(node.right)
        s.append(node.left)
    return res
        

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # return preorderTraversal1(root)
        return preorderTraversal2(root)
# @lc code=end

