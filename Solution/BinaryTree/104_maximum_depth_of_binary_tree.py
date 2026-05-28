class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0

    return max(maxDepth(root.left) + 1, maxDepth(root.right) + 1)

if __name__ == "__main__":
    tree = TreeNode(3)
    tree.left = TreeNode(9)
    tree.right = TreeNode(20)
    tree.right.left = TreeNode(15)
    tree.right.right = TreeNode(7)

    print(maxDepth(tree))