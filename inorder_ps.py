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
    # current = Node
    # current = None
    while root.left is not None:
        # current = root
        root = root.left
    return root

def  left_r(root):
    while root.right is not None:
        root=root.right
    return root




def find(root,key):
    current = root
    while True:
        # if root is None:
        #     return key
        
        if key < current.val:
            current = current.left

        elif key > current.val:
            current = current.right
        else: 
            # print(current.val)
            break
        
    temp1 = right_l(current.right)
    temp2 =left_r(current.left)
    print(temp1.val)
    print(temp2.val)
    # print(temp1.val)
    # current = Node
    # # ex = root.right
    # # temp = root.right
    # while temp.left is not None:
    #     ex = ex.left
    # print(ex.val)

    
current = Node           

r = Node(50) 
insert(r,Node(30)) 
insert(r,Node(20)) 
insert(r,Node(40)) 
insert(r,Node(70)) 
insert(r,Node(60)) 
insert(r,Node(80)) 

# inorder(r)
find(r,50)


