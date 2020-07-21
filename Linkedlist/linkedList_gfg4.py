class Node:          #sorted linkedlist
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

    def sortedduplicate(self):
        temp = self.head
        if temp is None:
            return
        while temp.next is not None:
            if temp.data == temp.next.data: #while comparing value we should compare with data
                new = temp.next.next
                temp.next = None
                temp.next = new
            else:
                temp = temp.next
        return self.head


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

linkedList.sortedduplicate()
linkedList.printList()