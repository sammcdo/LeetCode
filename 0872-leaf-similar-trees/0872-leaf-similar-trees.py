# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        a = self.getEnds(root1)
        b = self.getEnds(root2)

        return a == b
    
    def getEnds(self, node):
        l = []
        if node.left == None and node.right != None:
            l.extend(self.getEnds(node.right))
            return l
        elif node.right == None and node.left != None:
            l.extend(self.getEnds(node.left))
            return l
        elif node.right == None and node.left == None:
            return [node.val]
        else:
            l.extend(self.getEnds(node.left))
            l.extend(self.getEnds(node.right))
            return l
