#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
m=0
def diameterOfBinaryTree(root):
    global m
    if not root:
        return 0
    l,r=diameterOfBinaryTree(root.left),diameterOfBinaryTree(root.right)
    # 在后序遍历退出时，检查左右路径长度。
    m=max(m,l+r)
    # 返回的是最大子树深度而非最大路径长度，为了方便计算左右路径长度。
    return max(l,r)+1
    
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global m 
        m=0
        diameterOfBinaryTree(root)
        return m
        
# @lc code=end

