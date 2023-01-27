from tree import BinaryTree, TNode
#          '3'
#        /     \
#       /       \
#     'E'       '5'
#    /   \      /
#   'I'  'R'   'A'
#        /  \    \
#      'N'  'C'  'V'
#             \
#             'S'

def postorder_exemple_tree():
    tree = BinaryTree()
    n1 = TNode('I')
    n2 = TNode('N')
    n3 = TNode('S')
    n4 = TNode('C')
    n5 = TNode('R')
    n6 = TNode('E')
    n7 = TNode('V')
    n8 = TNode('A')
    n9 = TNode('5')
    n0 = TNode('3')

    n0.left = n6
    n0.right = n9
    n6.left = n1
    n6.right = n5
    n5.left = n2
    n5.right = n4
    n4.right = n3
    n9.left = n8
    n8.right = n7

    tree.root = n0
    return tree


if __name__ == "__main__":
    tree = postorder_exemple_tree()
    print("Percurso em pós ordem:")
    tree.postorder_traversal()
    print("Altura:", tree.height())



