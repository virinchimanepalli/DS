class Node:
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


    def insertatHead(self,newNode):
        tempNode = self.head
        self.head = newNode
        newNode.next = tempNode #or self.Head.next = tempNode
        del tempNode


    def insert(self,newNode):
        if self.head is None:
            #head => john =>points to None
            self.head = newNode
        else:
            lastNode = self.head # to start from beggining 
            while True:# loop runs untill it finds last element
                if lastNode.next is None: #means linked list is at end then i will breeak
                    break
                lastNode = lastNode.next # increment lastnone value for checking(here it is second value (ram))
            lastNode.next = newNode #last value
   
   
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



#Node =>data , next
#firstNode.data = data ,firstnode.next= None
firstNode =Node('john')
linkedList = LinkedList()
linkedList.insert(firstNode)
secondNode =Node('ram')
linkedList.insert(secondNode)
thirdNode =Node('rishi')
linkedList.insert(thirdNode)
fourthNode = Node('virinchi')
linkedList.insert(fourthNode)
startNode = Node('boom')
linkedList.insertatHead(startNode)
linkedList.printList()
