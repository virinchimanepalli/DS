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
        # print(root.val)  
        # print(root)

def right_l(root):
    current = Node
    while root.left is not None:
        current = current.left
    return current




def find(root,key):
    while True:
        # if root is None:
        #     return key
        
        if key < root.val:
            root = root.left

        elif key > root.val:
            root = root.right
        else: 
            print(root.val)
            break
    # temp1 = right_l(root.right)
    # print(temp1.val)
    # current = Node
    ex = root.right
    # temp = root.right
    while temp.left is not None:
        ex = ex.left
    print(ex.val)

    
            

r = Node(50) 
insert(r,Node(30)) 
insert(r,Node(20)) 
insert(r,Node(40)) 
insert(r,Node(70)) 
insert(r,Node(60)) 
insert(r,Node(80)) 

# inorder(r)
find(r,50)


