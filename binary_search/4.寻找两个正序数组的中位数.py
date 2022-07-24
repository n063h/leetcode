#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

#test_case=([1,3],[2])

# [2] [1,3]

# @lc code=start

# Kst starts from 1
def findKstNumber(nums1, nums2, k):
    if len(nums1)>len(nums2):
        nums1,nums2=nums2,nums1
    if not nums1:
        return nums2[k-1]
    if k==1:
        return min(nums1[0],nums2[0])
    kk=k//2
    idx1=kk-1 if kk<=len(nums1) else len(nums1)-1
    idx2=kk-1 if kk<=len(nums2) else len(nums2)-1
    if nums1[idx1]<nums2[idx2]:
        return findKstNumber(nums1[idx1+1:], nums2, k-(idx1+1))
    return findKstNumber(nums1, nums2[idx2+1:], k-(idx2+1))

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1,l2=len(nums1),len(nums2)
        mid=(l1+l2)//2
        if (l1+l2)%2 == 0:
            return (findKstNumber(nums1, nums2, mid)+findKstNumber(nums1, nums2, mid+1))/2
        return findKstNumber(nums1, nums2, mid+1)
# @lc code=end

"""
找到第K小的数字,K从1开始,更符合直觉,否则idx计算时极容易出错
每次排除K//2个数字,两数组比较更小的那个数组的前K//2个数字必定小于第K个数字。
不能试图排除len(nums1)//2,因为要分4种情况处理K的落值,很麻烦。
要规避K//2比某个数组还长的问题。
"""