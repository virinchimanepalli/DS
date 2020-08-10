class Node():
    def  __init__(self,data):
        self.val = data
        self.left = None
        self.right = None

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

def insert(root,key):
    temp = root
    q = []
    q.append(temp)

    while len(q):
        temp = q[0]
        q.pop(0)

        if not temp.left:
            temp.left = Node(key)
            break
        else:
            q.append(temp.left)

        if not temp.right:
            temp.right = Node(key)
            break
        else:
            q.append(temp.right)
            
root = Node(10)  
root.left = Node(11)  
root.left.left = Node(7) 
root.right = Node(9)  
root.right.left = Node(15)  
root.right.right = Node(8)     


inorder(root)#before insertion 
insert(root,12)
inorder(root)#after insertion














            