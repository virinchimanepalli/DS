class Node:
    def __init__(self,key):
        self.val = key
        self.left = None
        self.right =None
        
    
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

def min(root):
    current = Node
    
    while root.left is not None:
        current = current.left
    return current

def inorder(root):
    if root:
        # print(inorder.roo)
        print(root.val)
        inorder(root.left)
        
        inorder(root.right)

def delete(root,key):
    if root is None:
        return root
    if key <root.val:
        root.left = delete(root.left,key)
    elif key> root.val:
        root.right = delete(root.right,key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = min(root.right)
        root.val = temp.val
        root.right = delete(root.right,temp.val)
    return root


r = Node(50) 
insert(r,Node(30)) 
insert(r,Node(20)) 
insert(r,Node(40)) 
insert(r,Node(70)) 
insert(r,Node(60)) 
insert(r,Node(80)) 

# inorder(r)
delete(r,60)
delete(r,40)
# delete(r,50)

inorder(r)