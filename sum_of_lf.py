class Node:
    def __init__(self,key):
        self.left = None
        self.right =None
        self.val = key
        self.count =0
    
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
        
def sum(rootl,count):   
    print(count) 
    if rootl.left is None and rootl.right is None:
        count = count +rootl.val
        # empty =count
        # print(count)
        return count.val
    # elif rootl.left or rootl.right is not None:
    #     if rootl.left is None:
    #         rootl.left = rootl.right
    #     elif rootl.right is None:
    #         rootl = rootl.left
    else:
        current = rootl
        if current.left is None:
            sum(current.right,count)
        elif current.right is None:
            sum(current.left,count)
        else:
            currentl = current.left
            currentr = current.right
            sum(currentl,count)
            sum(currentr,count)
    # print(count)
            


        
        



def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

r = Node(50) 
insert(r,Node(30)) 
insert(r,Node(20)) 
insert(r,Node(40)) 
insert(r,Node(70)) 
insert(r,Node(60)) 
insert(r,Node(80)) 

# inorder(r)
k=(r,0)
print(k)
