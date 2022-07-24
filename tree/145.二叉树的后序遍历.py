#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def postorderTraversal1(root):
    if not root:
        return []
    l,r=postorderTraversal1(root.left),postorderTraversal1(root.right)
    return [*l,*r,root.val]

def postorderTraversal2(root):
    s,res=[],[]
    if root:
        # store node and visited
        s.append((root, False))
    while s:
        node,visited=s.pop()
        if not node:
            continue
        if not visited:
            # hasn't visited, visit left,right ,then back to node itself
            s.append((node,True))
            s.append((node.right,False))
            s.append((node.left,False))
        else:
            # has visited left and right, visit current
            res.append(node.val)
    return res

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return postorderTraversal1(root)
        #return postorderTraversal2(root)
# @lc code=end

