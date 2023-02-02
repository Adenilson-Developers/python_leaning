from tree import BinaryTree, TNode
#           'O'
#        /       \
#       /         \
#     'D'         'N'
#    /   \        /  \
#   'E'  'N'    'S'  'O'
#        /              \
#      'I'              'N'
#               
# ADENILSON

def exemple_name_tree():
    tree = BinaryTree()
    n1 = TNode('A')
    n2 = TNode('D')
    n3 = TNode('E')
    n4 = TNode('N')
    n5 = TNode('I')
    n6 = TNode('L')
    n7 = TNode('S')
    n8 = TNode('O')
    n9 = TNode('N')

    n2.left = n6
    n2.right = n1


    
    

if __name__ == "__main__":
    tree = exemple_name_tree()
    print("Percurso em pós ordem:")
    tree.postorder_traversal()


    
    
