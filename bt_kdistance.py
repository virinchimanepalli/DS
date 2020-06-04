class Node: 
  
    def __init__(self, data): 
        self.val = data 
        self.left = None
        self.right = None
        self.count = 0


def kcount(root,k):
    if root is None:
        return
    if k ==0:
        print(root.val)
        return
    else:
        kcount(root.left,k-1)
        kcount(root.right,k-1)



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


key = int(input("enter kth number:" ))
# kcount(root,key)
print(kcount(root,key))
# mcount(root,2)