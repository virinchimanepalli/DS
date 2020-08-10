class Node: 
  
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None


def height(root):
    if root is None:
        return 0
    return 1+max(height(root.left),height(root.right))
    

def diameter(l,m):
    return l+m +1

root = Node(10)  
root.left = Node(11)  
root.left.left = Node(7) 
root.left.left.left = Node(45)

root.right = Node(9)  
root.right.left = Node(15)  
root.right.right = Node(8)     
root.right.right.right = Node(81)   
root.right.right.right.right =Node(123)
root.right.right.right.right.left =Node(1253)


l = height(root.left)
m = height(root.right)
k= diameter(l,m)
print("The Diameterof a given tree is:{}".format(k))





