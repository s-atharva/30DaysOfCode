class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.previous = None
        self.successor = None

    def inorder_successor_helper(self, node, p):
        if node is None:
            return

        # Left
        self.inorder_successor_helper(node.left, p)

        # Process
        if self.previous == p and self.successor is None:
            self.successor = node
            return

        self.previous = node

        # Right
        self.inorder_successor_helper(node.right, p)

    def inorder_successor(self, root, p):
        self.previous = None
        self.successor = None

        self.inorder_successor_helper(root, p)

        return self.successor


# Create BST
root = TreeNode(20)

root.left = TreeNode(10)
root.right = TreeNode(30)

root.left.left = TreeNode(5)
root.left.right = TreeNode(15)

root.right.left = TreeNode(25)
root.right.right = TreeNode(40)

# p = 15
p = root.left.right

# Find successor
solution = Solution()
result = solution.inorder_successor(root, p)

# Print result
if result:
    print("Inorder successor of", p.val, "is", result.val)
else:
    print("No inorder successor")
