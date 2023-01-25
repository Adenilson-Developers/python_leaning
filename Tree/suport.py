from tree import BinaryTree, TNode
#         '+'
#      /       \
#    'a'       '*'
#            /    \
#          'b'    '-'
#                /   \
#              '/'   'e'
#             /   \
#            'c'  'd'

# expressão matemática (a + (b*(c/d)-e))

if __name__ == "__main__": 
    tree = BinaryTree
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
    n3.rught = n5
    n2.left = n1
    n2.right = n3
    tree.root = n2
    
