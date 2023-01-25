class TNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.rght = None
    def __str__(selft):
        return str(selft.data)

class BinaryTree: 
    def __init__(self, data):
        node = TNode(data)
        self.root = node

if __name__ == "__main__":
    tree = BinaryTree(7)
    tree.root.left = TNode(18)
    tree.root.right = TNode(14)

    print(tree.root)
    print(tree.root.right)
    print(tree.root.left)