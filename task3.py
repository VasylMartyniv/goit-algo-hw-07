class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def sum_of_values(node):
    if node is None:
        return 0
    return node.value + sum_of_values(node.left) + sum_of_values(node.right)


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.left.left = TreeNode(2)
root.left.right = TreeNode(8)
root.right.left = TreeNode(15)
root.right.right = TreeNode(25)

print(sum_of_values(root))
