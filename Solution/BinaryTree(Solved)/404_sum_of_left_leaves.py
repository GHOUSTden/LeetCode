class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def sumOfLeftLeaves(root: TreeNode) -> int:
    if not root:
        return 0

    result = 0

    if root.left and not root.left.left and not root.left.right:
        result += root.left.val

    result += sumOfLeftLeaves(root.left)
    result += sumOfLeftLeaves(root.right)

    return result

if __name__ == "__main__":
    tree = TreeNode(3)
    tree.left = TreeNode(9)
    tree.right = TreeNode(20)
    tree.right.left = TreeNode(15)
    tree.right.right = TreeNode(7)

    print(sumOfLeftLeaves(tree))