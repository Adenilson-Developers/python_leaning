class TNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def __str__(selft):
        return str(selft.data)

class BinaryTree: 
    def __init__(self, data=None):
        if data:
            node = TNode(data)
            self.root = node
        else:
            self.root = None

    # Percurso em ordem simetrica ( " inorder" in English)
    def simetric_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            print('(', end='')
            self.simetric_traversal(node.left)
        print(node, end='')
        if node.right:
            self.simetric_traversal(node.right)
            print(')', end='')

    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node)
if __name__ == "__main__":
    # tree = BinaryTree(7)
    # tree.root.left = TNode(18)
    # tree.root.right = TNode(14)

    # print(tree.root)
    # print(tree.root.right)
    # print(tree.root.left)

    tree = BinaryTree()
    n1 = TNode('a')
    n2 = TNode('+')
    n3 = TNode('*')
    n4 = TNode('b')
    n5 = TNode('-')
    n6 = TNode('/')
    n7 = TNode('c')
    n8 = TNode('d')
    n9 = TNode('e') 

    n6.left = n7
    n6.right = n8
    n5.left = n6
    n5.right = n9
    n3.left = n4
    n3.right = n5
    n2.left = n1
    n2.right = n3

    tree.root = n2

    tree.simetric_traversal()
    print()