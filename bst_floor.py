class Node:
    def __init__(self,key):
        self.left = None
        self.right =None
        self.val = key
        # self.count =0
    
def insert(root,node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
               root.right = node
            else:
                insert(root.right,node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left,node)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


def floor(root,key):
    if root.right is None:
        return root.val
    if root.val == key:
        return root.val
    if key < root.val:
        return floor(root.left,key)
    value = floor(root.right,key)
    return value if value <=key else root.val

r = Node(8)
insert(r,Node(4))
insert(r,Node(12))
insert(r,Node(2))
insert(r,Node(6))
insert(r,Node(10))
insert(r,Node(14))


print(floor(r,7))