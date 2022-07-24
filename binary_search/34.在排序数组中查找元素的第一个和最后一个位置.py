#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start

def searchRange1(nums, target):
    start,end=-1,-1
    l,r=0,len(nums)-1
    while l<=r:
        mid=(l+r)//2
        if nums[mid]==target and (mid-1<0 or nums[mid-1]!=target):
            start=mid
            break
        elif nums[mid]>=target:
            r=mid-1
        else:
            l=mid+1
    if start==-1:
        return [-1,-1]
    
    l,r=start,len(nums)-1
    while l<=r:
        mid=(l+r)//2
        v=nums[mid]
        if v==target and (mid+1>=len(nums) or nums[mid+1]!=target):
            end=mid
            break
        elif v<=target:
            l=mid+1
        else:
            r=mid-1
    return [start, end]
    
def searchRange2(nums, target):
    def binarySearchLeft(nums, target): # 找左边界，向左收缩
        l,r=0,len(nums)-1
        while l<r:
            mid=(l+r)//2 # mid靠左，使r=mid时,[1,1]r也向左走
            if nums[mid]==target: # 等于target时不退出，继续搜索
                r=mid    # r可以不变,例如[1,2,3]@2,向左收缩后是[1,2],若-1可能使nums[r]<target。使用靠左mid保证向左收缩。
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
        return l
    def binarySearchRight(nums, target): # 找右边界，向右收缩
        l,r=0,len(nums)-1
        while l<r:
            mid=(l+r+1)//2 # mid靠右，使l=mid时,[1,1]l也向右走
            if nums[mid]==target: # 等于target时不退出，继续搜索
                l=mid # l可以不变,
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return l
    l,r=binarySearchLeft(nums, target),binarySearchRight(nums, target)
    if nums and nums[l]==target==nums[r]:
        return [l,r]
    return [-1,-1]

def searchRange3(nums, target): # 左闭右开
    def binarySearchLeft(nums, target): # 找左边界，向左收缩
        l,r=0,len(nums)
        while l<r:
            mid=(l+r)//2
            if nums[mid]==target: # 等于target时不退出，继续搜索
                r=mid  
            elif nums[mid]>target:
                r=mid
            else:
                l=mid+1
        return l
    
    def binarySearchRight(nums, target): # 找右边界，向右收缩
        l,r=0,len(nums)
        while l<r:
            mid=(l+r)//2
            if nums[mid]==target: # 等于target时不退出，继续搜索
                l=mid+1
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid
        return r
    l,r=binarySearchLeft(nums, target),binarySearchRight(nums, target)
    if r<=len(nums) and l<len(nums) and nums[l]==target==nums[r-1]: # 左闭右开，r-1是右闭的target
        return [l,r-1]
    return [-1,-1]

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return searchRange3(nums, target)
    
# @lc code=end

"""
方法2:
l<r保证l==mid==r取到target时能退出。
mid分别取靠左和靠右,保证收缩。
nums[mid]==target时不退出,继续搜索,向left收缩则r边界不变,因为没看r朝left方向的下一位,可能取到非target。
方法3:
左闭右开,故超右走时才+1,取到的r是最后符合target的idx+1
"""