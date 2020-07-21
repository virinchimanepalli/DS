class Node:     #reversing of linkedlist
    def __init__(self,data):
        self.data =data
        self.next =None


class LinkedList:
    def __init__(self):
        self.head = None


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

    def printList(self):
        if self.head is None:
            print("list is empty")
            return
       
        currentNode = self.head
        while True:
            if currentNode is None: #if it reaches end it will break
                break
            print(currentNode.data)#present value
            currentNode = currentNode.next #increment

    def reverse(self):
        prev =None
        current = self.head
        while current is not None:
            next = current.next #next is pointer points to next
            current.next = prev #pionts to previous value
            prev = current #previous value is stored in current value
            current = next #both current and prev pointer will move 
        self.head = prev  #not prev =self.head 



linkedList = LinkedList()
firstNode =Node(1)
linkedList.insert(firstNode)
secondNode =Node(2)
linkedList.insert(secondNode)
thirdNode =Node(3)
linkedList.insert(thirdNode)
fourthNode = Node(45)
linkedList.insert(fourthNode)
fifthnode = Node(8)
linkedList.insert(fifthnode)

linkedList.reverse()
linkedList.printList()