from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> Optional[TreeNode]:
        ansroot = TreeNode()
        global p
        p = ansroot
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            global p
            p.right = TreeNode(root.val)
            p = p.right
            inorder(root.right)
        inorder(root)
        return ansroot.right
