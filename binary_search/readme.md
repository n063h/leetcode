# Binary Search

边界原则[左闭,右开)是最佳实践。

模板：

```python
#求左起第一个>=target的值,从右往左收缩.
#即应该插入target的idx,对应bisect.bisect_left
def binary_searchL(nums:list[int],target:int):
  l,r=0,len(nums) # r是能取到的下标后一位
  while l<r: # l!=r
    mid=(l+r)//2
    v=nums[mid]
    if v>=target: #  mid取太右，向左收缩
      r=mid # r开区间取不到，故直接等于mid
    else:
      l=mid+1
  return l 
```

```python
#求左起第一个>target的idx，从左往右收缩.
#对应bisect.bisect_right.
#target在list的最右idx即r开区间-1
def binary_searchR(nums:list[int],target:int):
  l,r=0,len(nums) # r是能取到的下标后一位
  while l<r: # l!=r
    mid=(l+r)//2
    v=nums[mid]
    if v<=target: #  mid取太左，向右收缩
    	l=mid+1
    else:
      r=mid # r开区间取不到，故直接等于mid
  return r
```

只要符合原则，一定会到想要的位置。
