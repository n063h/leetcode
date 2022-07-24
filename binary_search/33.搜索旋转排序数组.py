#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start


# [10,100,0,9]
def binarySearch1(nums, target):
    l,r=0,len(nums)-1
    while l <= r:
        mid=(l+r)//2
        left,cur,right=nums[l],nums[mid],nums[r]
        if cur==target:
            return mid
        if cur>right: # mid in left
            if target>cur: # in which case target must at right side of mid
                l=mid+1
            else:
                left=binarySearch(nums[:mid], target)
                right=binarySearch(nums[mid+1:], target)
                if left is not None:
                    return left
                if right is not None:
                    return right+mid+1
                return None
        else: # mid in right
            if target<cur: # in which case target must at left side of mid
                r=mid-1
            else:
                left=binarySearch(nums[:mid], target)
                right=binarySearch(nums[mid+1:], target)
                if left is not None:
                    return left
                if right is not None:
                    return right+mid+1
                return None
    return None

def binarySearch2(nums, target):
    l,r=0,len(nums)-1
    while l <= r:
        mid=(l+r)//2
        left,cur,right=nums[l],nums[mid],nums[r]
        if cur==target:
            return mid
        if cur>right:# mid in left
            if left<=target<cur:
                r=mid-1
            else:
                l=mid+1
        else:
            if cur<target<=right:
                l=mid+1
            else:
                r=mid-1
    return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # res=binarySearch1(nums, target)
        # return res if res is not None else  -1
        return binarySearch2(nums, target)
# @lc code=end

"""
方法1:
区分mid在左边还是右边。
区分target在cur左边还是右边。
有时候,比如[10,100,0,9],cur=100,target=0,此时只有target>100的才知道一定扫描右边,target<100的可能在左边也可能在右边,这时候只能扫两次。
此时找不到应返回None,应容许l==r,否则[1]这种情况会返回None。

方法2:
实际上,只要扫一遍,就可以了。因为mid在左可以知道mid左边的值域,mid在右可以知道mid右边的值域,target在不在该值域中总能确定。
对于[10,100,0,9],cur=100,target=0,此时cur在左边,只有[10,cur]之间的才在左边扫描,不管是小于10还是大于cur的都在右边。
对于[10,100,0,9],cur=0,target=9,此时cur在右边,只有[cur,9]之间的才在右边扫描,不管是小于cur还是大于9的都在右边。
"""