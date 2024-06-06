class TreeNode:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None

#   def PrintTree(self):


def Insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if key < root.key:
            root.left = Insert(root.left, key)           
        elif key > root.key:
            root.right = Insert(root.right, key)
    return root

root = None
root = Insert(root, 5)
root = Insert(root, 6)
root = Insert(root, 8)

