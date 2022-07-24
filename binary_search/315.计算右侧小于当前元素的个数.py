#
# @lc app=leetcode.cn id=315 lang=python3
#
# [315] 计算右侧小于当前元素的个数
#

# @lc code=start

def merge(n1,n2):
    l,r=0,0
    total=[]
    while l<len(n1) and r<len(n2):
        v1,v2=n1[l],n2[r]
        if  v1['val']>v2['val']:
            v1['k']+=(len(n2)-r)
            total.append(v1)
            l+=1
        else :
            total.append(v2)
            r+=1
            
    if l<len(n1):
        total+=n1[l:]
    if r<len(n2):
        total+=n2[r:]
    return total
            
def mergeSort(nums):
    if len(nums) <=1:
        return nums
    mid=len(nums)//2
    l=mergeSort(nums[:mid])
    r=mergeSort(nums[mid:])
    res=merge(l,r)
    return res
    
class Solution:
    def countSmaller(self, nums) :
        nums=[{'val':v,'k':0,'idx':idx}for idx,v in enumerate(nums)]
        total=mergeSort(nums)
        res=[0]*len(nums)
        for i in total:
            idx,k=i['idx'],i['k']
            res[idx]=k
        return res
        
# @lc code=end

"""
归并排序时,因为能比较两个数组l,r对应元素大小,所以能知道l对应元素在r数组里有多少逆序对,就知道对应ij两个数组的count.
因为超右看求更小值的数量,所以降序归并.
l>r时, 降序对数量可以看r右有多少元素.
l<=r时,不是降序对,跳过.
以左数组为主求idxi对于右数组idxr的降序对个数,方向不能改.
"""
