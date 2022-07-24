#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start

def searchMatrix(matrix, target):
    m,n=len(matrix),len(matrix[0])
    l,r=0,m
    while l < r:
        mid=(l+r)//2
        if matrix[mid][0]>=target:
            r=mid
        else:
            l=mid+1
    if l>=m:
        l-=1
    if matrix[l][0]>target: # not found target in 1st col
        if l==0:
            return False
    while l>0 and matrix[l][0]>target:
        l-=1
        
    row=l
    l,r=0,n
    while l < r:
        mid=(l+r)//2
        if matrix[row][mid]==target:
            return True
        if matrix[row][mid]>target:
            r=mid
        else:
            l=mid+1
    return False
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return searchMatrix(matrix, target)

# @lc code=end

"""
注意边界条件,l跳出可能比m更大
"""