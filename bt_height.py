class Node: 
  
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None


def height(root):
    if root is None:
        return 0
    return 1+ max(height(root.left),height(root.right))


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


# print(height(root))
k = height(root)
print("height of a given tree is :{}".format(k))