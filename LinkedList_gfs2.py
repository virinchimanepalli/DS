class Node:
    def __init__(self,data):
        self.data =data
        self.next =None
        


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0


    def isListEmpty(self):
        if self.head is None:
            print("list is empty")
            return True
        else:
            return False

    def insert(self,newNode):
        if self.head is None:
            self.head = newNode

        else:
            lastNode = self.head
            while True:
                if lastNode.next is None :
                    break
                else:
                    lastNode = lastNode.next
            lastNode.next = newNode

    def repeat(self,key):
        
        if self.head is None:
            print("list is empty")
            return
        c = 0
        currentNode = self.head
        while True:
            if currentNode is None: #if it reaches end it will break
                break
            k = currentNode.data#present value
            if k == key:
                c = c+1
            currentNode = currentNode.next #increment
        # print(c)
        return c


linkedList = LinkedList()
firstNode =Node(1)
linkedList.insert(firstNode)
secondNode =Node(1)
linkedList.insert(secondNode)
thirdNode =Node(2)
linkedList.insert(thirdNode)
fourthNode = Node(3)
linkedList.insert(fourthNode)
            
l =linkedList.repeat(8)
print(l)