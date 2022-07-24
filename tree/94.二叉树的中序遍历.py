#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def inorderTraversal1(root):
    if not root:
        return []
    l,r=inorderTraversal1(root.left),inorderTraversal1(root.right)
    return [*l,root.val,*r]

def inorderTraversal2(root):
    s,res=[],[]
    if root:
        # store node and visited
        s.append((root, False))
    while s:
        node,visited=s.pop()
        if not node:
            continue
        if not visited:
            # hasn't visited left, visit left
            s.append((node,True))
            s.append((node.left,False))
        else:
            # has visited left, visit current, then visit right
            res.append(node.val)
            s.append((node.right,False))
    return res

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # return inorderTraversal1(root)
        return inorderTraversal2(root)
# @lc code=end

