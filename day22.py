# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        curr = deque([root]) if root else None
        result,zig=[],True
        while curr:
            level=[node.val for node in (curr if zig else reversed(curr))]
            result.append(level)
            next=[]
            for node in curr:
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            curr=next
            zig=not zig
        return result    
                
        
