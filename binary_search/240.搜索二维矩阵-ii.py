#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

# @lc code=start

import numpy as np

def binarySearch(line,target):
    l,r=0,len(line)
    while l < r:
        mid=(l+r)//2
        if line[mid]<=target:
            l=mid+1
        else:
            r=mid
    return r

def searchMatrix(matrix,target):
    m,n = len(matrix), len(matrix[0])
    row,col=binarySearch(matrix[:,0].reshape((-1)),target),binarySearch(matrix[0].reshape((-1)),target)
    if row==0 or col==0:
        return False
    for i in range(row):
        if matrix[i][col-1]<target:
            continue
        j=binarySearch(matrix[i,:col].reshape(-1),target)
        if matrix[i][j-1]==target:
            return True
    return False
        

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return searchMatrix(np.array(matrix),target)
        
# @lc code=end

