#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start

def twoSum(numbers,target):
    l,r=0,len(numbers)
    start,end=l,r
    target=target-numbers[start]
    while start<end:
        l,r=start,end
        while l < r:
            mid=(l+r)//2
            v=numbers[mid]
            if v==target:
                return [start+1,mid+1]
            if v>target:
                r=mid
            else:
                l=mid+1
        target+=numbers[start]
        start,end=start+1,l
        target-=numbers[start]
    return [-1,-1]
        
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        return twoSum(numbers, target)
# @lc code=end

"""
左边依次+1,右边根据左边的值修改target二分,跳出时满足或稍大,既然稍大,则右闭边界idx取值应该是l-1,又因为右开边界,所以取值l。
"""