# Tree
谨记：递归就是树的遍历。而遍历分自顶向下和自底向上。

如果子树情况会影响，一般是自底向上，即后序遍历。

确定遍历方向，明确需要返回什么，即可列出模板。
例如链表题，找到第k个元素是先序，不依赖后续子树，找到倒数第k个元素是后序，依赖子树。
```python
def findKstNode(root,k):
    if not root:
        return None
    return root if k==0 else findKstNode(root.next,k-1)

# return reversed_k and that node
def findReversedKstNode(root,k):
    if not root:
        return 0,None
    reversed_k,node=findReversedKstNode(root.next)
    return reversed_k+1,root if reversed_k+1==k else reversed_k+1,node
```

```python
# [652] 寻找重复的子树

# 这里显然自顶向下需要多配一个path的参数，
# 选择自底向上的方式，节省形参
def findDuplicateSubtrees(root):
    global m,res
    if not root:
        return "#"
    l,r=findDuplicateSubtrees(root.left),findDuplicateSubtrees(root.right)
    s=f"{root.val} {l} {r}"
    if s not in m:
        m[s]=1
    else:
        if m[s]==1: 
            res.append(root)
        m[s]+=1
    # 返回值不一定是想求的目标，
    # 在这里返回序列化的子树
    return s

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        global res,m
        res,m=[],dict()
        findDuplicateSubtrees(root)
        return res
```

迭代遍历树时，模拟栈比较麻烦，可以手动添加注释，判定是否访问过
```python
# [145] 二叉树的后序遍历

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
        return postorderTraversal2(root)
```