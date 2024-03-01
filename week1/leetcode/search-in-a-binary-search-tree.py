# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def search(root,val):
            if not root:
                return None
            elif root.val == val:
                return root
            elif root.val>val:
                root.left = search(root.left,val)
                return root.left
            else:
                root.right = search(root.right,val)
                return root.right
        return search(root,val)