class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_max_value(node):
    if node is None:
        return None
    current = node
    while current.right is not None:
        current = current.right
    return current.value


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(25)

print(find_max_value(root))
