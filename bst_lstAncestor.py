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

def inorder(root):
    if root:
        print(root.val)        
        inorder(root.left)
        inorder(root.right)

r = Node(50) 
insert(r,Node(30)) 
insert(r,Node(20)) 
insert(r,Node(40)) 
insert(r,Node(70)) 
insert(r,Node(60)) 
insert(r,Node(80)) 

def ancestor(root,n1,n2):
    if root is None:
        return None
    
    if root.val < n1 and root.val<n2:
        root = root.right
        ancestor(root)
    
    if root.val> n1 and root.val>n2:
        root = root.left
        ancestor(root,20,40)

    return root.val

k = ancestor(r,30,60)
print(ancestor(r,30,60))
print(k)




