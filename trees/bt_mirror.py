# import time
from datetime import datetime
start_time = datetime.now()

class Node: 
  
    def __init__(self, data): 
        self.val = data 
        self.left = None
        self.right = None

def isMirror(root1,root2):
    if root1 is None and root2 is None:
        return True
    
    if root1 is not None and root2 is not None and root1.val == root2.val:
        # if root1.val == root2.val:
        return isMirror(root1.left,root2.right) and isMirror(root1.right,root2.left)
    return False


def mirror(root):
    return isMirror(root,root)




root = Node(10)  
root.left = Node(11)  
root.right =Node(11)
root.left.left = Node(7) 
root.right.right =Node(7)
# root.left.left.left = Node(45)

print(mirror(root))
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
